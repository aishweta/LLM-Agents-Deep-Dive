import os
import csv
import faiss
import pickle
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, WebBaseLoader
from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.schema import Document
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# ---- Azure OpenAI Config ----
AZURE_OPENAI_API_KEY = "your-azure-api-key"
AZURE_OPENAI_ENDPOINT = "https://your-endpoint.openai.azure.com/"
DEPLOYMENT_NAME = "text-embedding-ada-002"

PDF_FOLDER = "src/document"
WEB_URL = "https://www.langchain.com/langsmith"
N_TOP_DOCS = 3
FAISS_INDEX_PATH = "faiss_index.pkl"

QUERY_LIST = [
    "Why is the periodic income measurement necessary?",
    "How does limited liability encourage entrepreneurship?",
    "What are the key components of a blacksmith?",
    "What are Retrieval Challenges in RAG?",
    "What is the difference between RAG and Fine-tuning?",
]

# ---- Load Documents (PDF + Web) ----
def load_documents():
    documents = []

    # Load PDFs
    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(PDF_FOLDER, file))
            documents.extend(loader.load())

    # Load Web URL
    web_loader = WebBaseLoader(WEB_URL)
    documents.extend(web_loader.load())

    return documents

# ---- Text Chunking ----
def chunk_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return text_splitter.split_documents(documents)

# ---- Create FAISS Vector Store ----
def create_faiss_vectorstore(chunks, embeddings):
    vectorstore = FAISS.from_documents(chunks, embeddings)
    
    # Save FAISS index
    with open(FAISS_INDEX_PATH, "wb") as f:
        pickle.dump(vectorstore, f)
    
    return vectorstore

# ---- Load FAISS Index (If Exists) ----
def load_faiss_vectorstore():
    if os.path.exists(FAISS_INDEX_PATH):
        with open(FAISS_INDEX_PATH, "rb") as f:
            return pickle.load(f)
    return None

# ---- Retrieve Top-N Documents ----
def retrieve_documents(query, retriever, top_n):
    docs = retriever.get_relevant_documents(query)
    return [(doc.page_content, doc.metadata) for doc in docs[:top_n]]

# ---- Generate Response ----
def generate_response(query, retriever):
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(query)

# ---- Save Output to CSV ----
def save_to_csv(results):
    output_file = "src/FinalResponse.csv"
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["top_docs", "response"])
        writer.writerows(results)

# ---- Main Execution ----
if __name__ == "__main__":
    # Load documents and chunk them
    raw_documents = load_documents()
    chunked_documents = chunk_documents(raw_documents)
    
    # Initialize embeddings
    embeddings = AzureOpenAIEmbeddings(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        azure_deployment=DEPLOYMENT_NAME,
        api_key=AZURE_OPENAI_API_KEY
    )

    # Check if FAISS index exists, else create it
    vectorstore = load_faiss_vectorstore()
    if not vectorstore:
        vectorstore = create_faiss_vectorstore(chunked_documents, embeddings)

    retriever = vectorstore.as_retriever()

    # Process queries
    results = []
    for query in QUERY_LIST:
        top_docs = retrieve_documents(query, retriever, N_TOP_DOCS)
        response = generate_response(query, retriever)
        results.append((top_docs, response))

    # Save results to CSV
    save_to_csv(results)
    print(f"Results saved to 'src/FinalResponse.csv'")
