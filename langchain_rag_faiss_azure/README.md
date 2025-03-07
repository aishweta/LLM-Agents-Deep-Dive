

### Install Dependencies (If Not Installed)
`pip install langchain langchain-community pypdf faiss-cpu openai azure-ai-openai`

### LangChain RAG Implementation
`python main.py'

### Code snippet
```
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

# Process querie
top_docs = retrieve_documents(query, retriever, N_TOP_DOCS)
response = generate_response(query, retriever)
```

