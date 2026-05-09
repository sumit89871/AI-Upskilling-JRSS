# RAG Interview Questions

## 1. What is RAG?

Short answer:

RAG retrieves relevant context from documents before asking an LLM to generate an answer.

Expanded answer:

RAG stands for Retrieval Augmented Generation. The application first searches documents for chunks related to the user's question. Those chunks are placed into the prompt as context. The LLM then generates an answer using that context.

Project example:

In the final QA assistant POC, requirement notes can be retrieved before generating test cases.

Common wrong answer:

"RAG means uploading documents into the model."

That is wrong. RAG retrieves context at answer time.

## 2. Why do we use RAG?

Short answer:

To answer from private or current documents and reduce hallucination.

Expanded answer:

LLMs may not know local project files, private policies, or recent requirements. If the model is not given context, it may guess. RAG gives the model relevant source text before it answers.

Project example:

A QA knowledge assistant can answer from `notes.txt` instead of inventing login rules.

Common wrong answer:

"RAG guarantees the answer is correct."

RAG helps, but retrieval and prompting can still fail.

## 3. What is the difference between RAG and fine-tuning?

Short answer:

RAG retrieves context at runtime. Fine-tuning changes model behavior through training.

Expanded answer:

Use RAG when the model needs access to documents. Use fine-tuning when you need to adjust style, behavior, or specialized patterns through training. For beginner POCs, RAG is usually simpler and safer.

Project example:

For the final POC, use RAG to answer from requirement notes rather than fine-tuning a model on those notes.

Common wrong answer:

"RAG and fine-tuning are the same because both use documents."

They are different approaches.

## 4. What is a chunk?

Short answer:

A chunk is a smaller piece of a document used for retrieval.

Expanded answer:

Documents can be too long or too broad. Chunking splits them into smaller meaningful pieces so the retriever can find relevant context for a question.

Project example:

`Login should reject invalid passwords.` can be one chunk from `notes.txt`.

Common wrong answer:

"A chunk is always one sentence."

Chunk size depends on the document and use case.

## 5. What is metadata?

Short answer:

Metadata is source information about a chunk.

Expanded answer:

Metadata may include source file, page number, topic, or chunk ID. It helps show citations, debug retrieval, and support auditability.

Project example:

`{"source": "notes.txt", "topic": "login"}` helps explain where a retrieved login rule came from.

Common wrong answer:

"Metadata is not needed because the answer is enough."

In enterprise AI, source traceability matters.

## 6. What is an embedding?

Short answer:

An embedding is a numeric vector representing text meaning.

Expanded answer:

Embedding models convert text into numbers so similar meanings can be compared mathematically. This helps retrieve relevant chunks even when exact words differ.

Project example:

The question "wrong password behavior" may retrieve a chunk saying "Login should reject invalid passwords."

Common wrong answer:

"Embedding is the generated answer."

Embedding is used for search, not final answer generation.

## 7. What is a vector database?

Short answer:

A vector database stores and searches embeddings.

Expanded answer:

Vector databases such as ChromaDB store text chunks, their embeddings, and metadata. They support similarity search so the app can find chunks close in meaning to the user question.

Project example:

A future version of the local RAG assistant could store note chunks in ChromaDB.

Common wrong answer:

"A vector database is the LLM."

The vector DB retrieves context. The LLM generates answers.

## 8. What is the difference between a retriever and a generator?

Short answer:

Retriever finds relevant chunks. Generator writes the answer.

Expanded answer:

The retriever searches documents or a vector DB and returns context. The generator is the LLM or mock LLM that uses that context to produce a response.

Project example:

`retrieve(question, chunks)` finds login chunks. `MockLLM().answer(question, context)` writes the mock answer.

Common wrong answer:

"Retriever and generator both answer the user."

The retriever does not write the final answer.

## 9. What is hallucination control in RAG?

Short answer:

It means reducing unsupported answers by grounding the model in retrieved context.

Expanded answer:

RAG controls hallucination by retrieving relevant chunks, putting them into the prompt, and instructing the model to answer only from that context. You should also check whether the final answer is supported by the retrieved source text.

Project example:

If context only says invalid passwords are rejected, the assistant should not invent account lockout rules.

Common wrong answer:

"RAG completely removes hallucination."

RAG reduces risk but does not eliminate it.

## 10. Where does LangChain fit in RAG?

Short answer:

LangChain helps wire RAG components together.

Expanded answer:

LangChain provides tools for document loading, text splitting, embeddings, vector stores, retrievers, prompt templates, and LLM calls. It helps assemble the workflow, but it is not the LLM or the vector database.

Project example:

A later version of the POC could use LangChain loaders and retrievers while keeping the same RAG mental model.

Common wrong answer:

"LangChain is the model."

LangChain is a framework/library layer, not the model.

## 11. Where does ChromaDB fit?

Short answer:

ChromaDB is a vector database used to store and search embeddings.

Expanded answer:

ChromaDB can store chunks, embeddings, and metadata locally. A retriever can use ChromaDB to find chunks similar to the user question.

Project example:

The local RAG assistant currently uses keyword retrieval. ChromaDB would be the optional next step for real vector search.

Common wrong answer:

"ChromaDB generates the answer."

ChromaDB retrieves context. The LLM generates the answer.

## 12. How would you debug a bad RAG answer?

Short answer:

Check retrieval first, then prompt, then generation.

Expanded answer:

Print the retrieved chunks. Verify whether they are relevant. Check metadata and source. Then inspect the prompt to ensure context is included and instructions are clear. Finally check whether the generator invented unsupported claims.

Project example:

If the QA assistant gives payment test cases for a login question, inspect retrieved chunks before changing the prompt.

Common wrong answer:

"Just use a better LLM."

A better LLM cannot fix missing or irrelevant context reliably.
