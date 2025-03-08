

## Task 1:
Goal
- Gather information about various types of insurance from the internet upto  **150** insurances polcies.
- Store information locally at the moment, you may store information in .txt files.
- You can use library beautiful soap or any other of your choice.
  
Deliverables:
- Python notebook of your experiment
- Python module for easy use of data extraction
- python notebook that demonstrates the use of said module

Reference: [ps: I haven't ran it, just go throuth it first then decide which one to use]
1. https://github.com/pankajthakur3999/web-scrapping-insurance-company/blob/main/web-scrapping-finally-final.ipynb
2. https://github.com/SJohnston079/insurance_web-scraping/tree/main/Insurance_web-scraping

_________________________________________________________________
## Task2-PdfToText
Goal
- Collect at least 10 pdf files and store in int `./data/pdfs` folder 
- Extract infromation from pdf files and store it in .txt file in `./data/.txt` folder
  
Deliverables
- Python notebook of your experiment
- Python module for easy use of data extraction
- python notebook that demonstrates the use of said module
_________________________________________________________________
## Task3-Chunking
Goal
Implement document chunking functions that implement different chunking strategies. Such functions should take the following inputs:
- input: folder name where the documents are stored
- output_table_name: table(csv) name where to stor the chunks
- Parameters of the chunking strategy: use langchain text-splitters. Be mindful of the text-splitter parameters like chunk_size ,chunk_overlap, separators, length_function, etc.

Deliverables:
- Python notebook of your experiment
- Module implementing the functions above.
- Notebook showcasing the chunking functions described above
_________________________________________________________________
## Task5-Embeddings
Goal
- Implement bge-large huggingface embeddings.
- Implement word2vec embeddings
  
Deliverable’s
- Module with the implementation embeddings of the document chunks [List] and query
- Notebook showcasing the inplementation
_________________________________________________________________
## Task6-VectorDB Instanciation
Goal
Implement the instantiation and indexing of a vector DB with the embeddings obtained from the chunked documents.

Deliverable’s
- Module with the instantiation and indexing of a vector DB with the embeddings of the document chunks
- Notebook showcasing the inplementation

_________________________________________________________________
## Task7-Prompting
Goal
Implement a prompting strategy for querying the vector database and optimizing interactions with the LLM.

Deliverables
Module for constructing and optimizing prompts based on retrieved document embeddings.
Notebook showcasing the implementation and prompt effectiveness.

_________________________________________________________________
## Task8-LLM_Calll
Implement the mechanism for calling the LLM, utilizing the retrieved vector embeddings to generate responses.

Deliverables
Module handling LLM API interactions with contextual retrieval.
Notebook demonstrating LLM response generation using indexed embeddings.

