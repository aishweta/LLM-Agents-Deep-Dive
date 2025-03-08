# What is RAG
- Retrieval: Find References for the question asked in your Document.
- Augmented: Add References to your Prompt.
- Generation: Improve answers to the question asked.

### RAG painpoints
https://medium.com/@generative.ai/12-rag-pain-points-and-proposed-solutions-31280460b81c

### Advanced RAG
## 1. Re-ranking
Read Following resources:
1. https://www.reddit.com/r/LocalLLaMA/comments/1ayka0f/explain_reranking/
2. https://www.rungalileo.io/blog/mastering-rag-how-to-select-a-reranking-model
3. https://www.pinecone.io/learn/series/rag/rerankers/

## 2. Meta filtering 

## 3. Hybrid Search
1. VectorDB + Keywords (You should try Meilisearch Hybrid, the relevency is 🤯 compared to BM25 or SPLADE.)
2. VectorDB (Internal Search) + Internet Search

Milvus => Scalar Filtering
Weaviate => Sparse+Dense
Elastic => Keyword & RRF (Rank Fusion)
MS Azure Cognitive => Keyword & RRF (Rank Fusion)
https://blog.lancedb.com/hybrid-search-and-custom-reranking-with-lancedb-4c10a6a3447e/
https://blog.lancedb.com/hybrid-search-rag-for-real-life-production-grade-applications-e1e727b3965a/

## 4. Prompt Engineering
https://huggingface.co/docs/peft/en/conceptual_guides/prompting

## 5. Query Re-writing 

## 6. Response Cleaning / Post-Processing

## 7. fine-tuning custom embedding models
the original Dense passage retrieval paper by Meta super insightful

## 8. RAT
I think this is the way we should be developing our generation pipeline
It has a combination of Chain of Thought + Retrieval
Can handle rather complex queries
In a nutshell, it tackles many of the pain points we have such as:
Answering complex queries because of CoT
Dealing with vague queries (to a degree) because of CoT
Retrieval can be made much more precise of the breaking down of the query
https://craftjarvis.github.io/RAT/
https://cobusgreyling.medium.com/rat-retrieval-augmented-thoughts-c7eb0cf5547c

## 9. Chat history - semantic router
https://github.com/aurelio-labs/semantic-router/blob/main/docs/04-chat-history.ipynb

## 10. LLMOPS and On tracing and debugging LLM pipeline?
https://github.com/Arize-ai/phoenix --> Phoenix looks more tweakable and integrate with ragas
https://github.com/langfuse/langfuse
langsmith

What are the additional benefits these LLMOPS while the conventional MLOps tool like mlflow could not? is it mostly the visualisation of LLM / RAG specific results?
- MLFlow is typically used for tracking model training. Useful for training classical model, and deep learning model. Typically you can track train / validation loss, time to complete an epoch, learning rate, etc.
- But for LLM workflow, there is no model training, but more on calling API to different endpoints, such as LLM, query to DB for each run, so you cannot really force fit this use case to MLFlow.
![image](https://github.com/aishweta/Insurance-QA-RAG/assets/31302697/7cb60373-8a81-49a3-86ab-018432046e5a)

https://docs.arize.com/phoenix/tracing/llm-traces

## 11. hallucination and temporal misalignment

## 15 query routing - semantic router
https://github.com/aurelio-labs/semantic-router
It is just classification model
Plenty ways to do, train some supervised model, or cosine similarity with some labelled examples
sentence transformer embedding model to check if what you input is similar to what you've defined in its "training set"
Basically we use the aurelio-labs semantic router that i've done an experiment on. These will require a few utterances ("training examples") only. These will be deployed with the help of Marcus.
Semantic router will route to:
Visualization (mermaid)
RAG (question and answer)
"None" (defaults to RAG)
We tweak the system prompt to go do default ChatGPT responses for:
Nonsensical queries ("ff", "asdfhaksd", etc.)
Chitchat queries ("Hello", "Good morning", prompts that do not command or ask questions)
https://github.com/aurelio-labs/semantic-router/blob/main/docs/02-dynamic-routes.ipynb

## 16 semantic chunking 

## 17. chart generation
https://medium.com/@sumitsahoo/generate-charts-using-openai-code-interpreter-88cb93a06da0
