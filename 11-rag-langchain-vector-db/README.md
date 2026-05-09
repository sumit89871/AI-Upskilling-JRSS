# 11 RAG, LangChain, And Vector Databases

## 1. What this module is

This module teaches Retrieval Augmented Generation, usually shortened to RAG.

RAG is a practical pattern for building AI applications that answer using documents instead of only relying on what the model already knows.

Simple meaning:

```text
Before asking the LLM to answer, retrieve useful document pieces and give them to the LLM as context.
```

This module also introduces LangChain and vector databases at beginner level.

## 2. Why it matters

LLMs do not automatically know your private requirement notes, company policies, API documentation, test strategy, or latest project files.

If you ask an LLM a question without giving it the right context, it may guess. That confident guess is often called hallucination.

RAG helps reduce that risk by giving the model relevant source text before it answers.

## 3. What the learner should finish knowing

After this module, the learner should understand:

- what RAG is
- why RAG exists
- why LLM alone may hallucinate
- RAG vs fine-tuning
- document
- chunk
- cleaning
- metadata
- embedding
- vector
- vector database
- similarity search
- retriever
- generator
- context
- reranking basics
- LangChain's role
- ChromaDB's role
- mock-first local RAG
- optional real embeddings and vector DB later
- how RAG appears in the final POC

## 4. Study order

1. `00-overview.md`
2. `01-rag-pipeline.md`
3. `02-langchain-vector-db.md`
4. `implementation/local-rag-notes-assistant/README.md`
5. `exercises.md`
6. `cheatsheet.md`
7. `interview-questions.md`

## 5. File list

- `README.md`: this module guide.
- `00-overview.md`: full beginner explanation of RAG and its building blocks.
- `01-rag-pipeline.md`: step-by-step RAG pipeline flow and debugging.
- `02-langchain-vector-db.md`: LangChain, ChromaDB, vector store, and retriever explanation.
- `exercises.md`: hands-on RAG practice with expected output, hints, and self-checks.
- `cheatsheet.md`: concise but meaningful RAG reference.
- `interview-questions.md`: interview answers with short answer, expanded answer, project example, and common wrong answer.
- `implementation/local-rag-notes-assistant/README.md`: runnable mock-first RAG project explanation.

## 6. Practical scope

This module is mock-first.

The implementation uses:

- local text file
- text chunking
- keyword-style retrieval
- mock LLM response

This is intentional. A beginner should understand the pipeline before adding real embedding models, ChromaDB, LangChain chains, rerankers, and paid/provider LLM calls.

Optional later:

- real embeddings
- ChromaDB
- LangChain document loaders/splitters
- real LLM generator
- reranking
- persistence

## 7. What not to over-focus on

Do not start with complex LangChain abstractions before understanding the pipeline.

Do not start with reranking before understanding retrieval.

Do not assume vector search automatically solves hallucination.

Do not confuse RAG with uploading documents permanently into the model.

## 8. How this helps in AI Engineer JRSS / Mettl / POC / interview

RAG is one of the most common AI Engineer POC patterns.

It helps you explain:

- how to answer from local/private documents
- how to reduce hallucination
- how to show sources
- how to connect retrieval to FastAPI
- how to pass context to an LLM wrapper
- how to use RAG inside LangGraph workflows
- how the final QA assistant answers from requirement notes
