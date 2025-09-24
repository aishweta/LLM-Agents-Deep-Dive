## Generative ai Roapmap -->

Course 1 - [Langchain for LLM Application Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)

## Retrieval Augmented Generation: Question Answering Over Documents
RAG over documents has two phases. In the first phase the documents are processed and installed in a database, often a vector database. 
The second phase is retrieving the data as shown below:

<img width="1105" height="652" alt="image" src="https://github.com/user-attachments/assets/6d40d3d1-76eb-4579-91fe-0dfcbb06044f" />


- ### Extract: 
Documents come in all sorts of file formats (.doc, .pdf, etc.) and contain all sorts of data formats (text, tables, images, movies). These must be extracted and put into a format that can be processed by the next stages. 
- ### Chunking: 
Text data is broken into smaller chunks – a process inventively named ‘chunking’.
- ### Embedding:  
Converting a chunk into a ‘dense vector’ that represents the meaning of the text. 
Loading: Adding the embedding and original data to a database.
- ### Database: 
The database is going to provide storage for the embedding and data. Often these are vector databases due to the embedding, but graph databases and traditional databases are also used.
- ### Query
- - Embedding: The query is converted to a dense vector using the same embedding model.
- - Retrieval: Retrieval is the process of finding the k chunks in the database that are ‘closest’ to the query vector.
- - LLM + Prompt: k results are provided to an LLM along with prompt to generate the final response.

# RAG Courses:
- [LangChain: Chat with Your Data](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/)

# pipeline specific courses
- [Preprocessing Unstructured Data for LLM Applications
](https://www.deeplearning.ai/short-courses/preprocessing-unstructured-data-for-llm-applications/)
- [Large Language Models with Semantic Search](https://www.deeplearning.ai/short-courses/large-language-models-semantic-search/)
- [Vector Databases: from Embeddings to Applications](https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/)
- [vector db](https://www.deeplearning.ai/short-courses/advanced-retrieval-for-ai/)
- [Knowledge Graphs for RAG](https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/)

# Agets courses 
- [crewai](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/)
- [langgraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/)
