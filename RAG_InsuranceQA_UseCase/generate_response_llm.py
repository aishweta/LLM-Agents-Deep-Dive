import os
from langchain.prompts import PromptTemplate
from langchain.llms import Together
from langchain.chains import LLMChain

# Set API Key
os.environ["TOGETHER_API_KEY"] = "your_together_ai_api_key"

# Load Together AI LLM
llm = Together(model="mistralai/Mistral-7B-Instruct-v0.1", temperature=0.7)

# Define function for RAG-based response generation
def generate_rag_response(top_chunks, query):
    """
    Generates a response using Together AI LLM based on retrieved document chunks.

    Args:
        top_chunks (list): List of top 3 retrieved document chunks.
        query (str): User's input question.

    Returns:
        str: LLM-generated response.
    """
    # Create a Prompt Template
    prompt_template = """You are an AI assistant. Use the following retrieved documents to answer the question.

    Retrieved Documents:
    {context}

    Question: {query}

    Answer:"""

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "query"])

    # Define LLM Chain
    rag_chain = LLMChain(llm=llm, prompt=prompt)

    # Prepare context
    context = "\n".join(top_chunks)

    # Run the chain
    response = rag_chain.run({"context": context, "query": query})

    return response
