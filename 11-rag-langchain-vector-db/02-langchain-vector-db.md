# LangChain And Vector Databases

## 1. What this topic is

This topic explains where LangChain and vector databases fit in a RAG system.

Beginner warning:

LangChain is not RAG by itself.

ChromaDB is not RAG by itself.

An LLM is not RAG by itself.

RAG is the full pattern that connects documents, chunks, embeddings, retrieval, prompting, and generation.

## 2. The most important beginner idea

LangChain helps connect components.

ChromaDB stores and searches vectors.

The LLM writes the final answer.

Mental model:

```text
LangChain = wiring/helper framework
ChromaDB = local vector database
LLM = generator
Your code = decides the flow
```

## 3. Why LangChain exists

LangChain exists because LLM applications often repeat the same patterns:

- load documents
- split text
- call embedding models
- store vectors
- create retrievers
- build prompts
- call LLMs
- combine steps into chains/workflows

LangChain gives reusable building blocks for these steps.

Beginner analogy:

LangChain is like a toolbox for assembling LLM app workflows.

Common mistake:

Installing many LangChain packages before understanding what each RAG step does.

## 4. Where LangChain fits

Typical LangChain-style RAG flow:

```text
Document loader -> text splitter -> embedding model -> vector store -> retriever -> prompt -> LLM
```

What each part means:

- Document loader reads source files.
- Text splitter creates chunks.
- Embedding model converts chunks to vectors.
- Vector store saves vectors and text.
- Retriever searches relevant chunks.
- Prompt combines question and context.
- LLM generates the final answer.

LangChain can help with all of these, but you still need to understand the flow.

## 5. What ChromaDB is

ChromaDB is a vector database often used for local RAG practice.

It can store:

- document chunks
- embeddings
- metadata

It can retrieve:

- chunks similar to a user question

Beginner analogy:

ChromaDB is like a searchable shelf of meaning-based document cards.

Common mistake:

Thinking ChromaDB writes the answer. It does not. It retrieves relevant chunks.

## 6. Vector database vs normal database

Normal database:

```text
Find exact or structured values.
```

Example:

```sql
Find user where id = 123
```

Vector database:

```text
Find text with similar meaning.
```

Example:

```text
Question: "wrong password behavior"
Relevant chunk: "Login should reject invalid passwords."
```

Use a normal DB for structured business records.

Use a vector DB for semantic document search.

## 7. Similarity search vs keyword search

Keyword search:

```text
matches exact words
```

Similarity search:

```text
matches meaning using embeddings
```

Example:

Question:

```text
How do we test wrong password?
```

Document:

```text
Login should reject invalid passwords.
```

Keyword search may miss this if exact words do not overlap enough.

Similarity search may find it because the meaning is close.

## 8. Retriever object/function

A retriever is the interface used to get relevant documents/chunks.

In beginner code, a retriever may be a simple function:

```python
retrieved = retrieve(question, chunks)
```

In LangChain, a retriever may be an object created from a vector store.

Simple memory:

```text
retriever = thing you ask for relevant chunks
```

Common mistake:

Thinking retriever and generator are the same. Retriever finds chunks. Generator writes answers.

## 9. Persistence

Persistence means saved data stays available after the program stops.

Why it matters:

If you build a vector database every time the app starts, startup may be slow and costly.

Persistent vector DB:

```text
index documents once -> save vector DB -> reuse later
```

Common mistake:

Deleting the vector store folder and then wondering why retrieval returns nothing.

## 10. Mock-first vs real vector DB

Mock-first version:

```text
chunks in Python list -> keyword retrieval -> mock LLM
```

Real vector DB version:

```text
chunks -> embeddings -> ChromaDB -> similarity search -> LLM
```

Why mock-first:

- no heavy setup
- no paid embedding API
- easier to see the pipeline
- easier for beginners to debug

When to add ChromaDB:

- after the learner understands documents, chunks, retrieval, prompt, and generator
- when semantic search is needed
- when the POC needs more realistic RAG behavior

## 11. Small example

Mock retrieval:

```python
chunks = [
    "Login should accept valid username and password.",
    "Password reset should send a secure link.",
]

question = "How should login be tested?"
```

Expected retrieved chunk:

```text
Login should accept valid username and password.
```

Real vector retrieval idea:

```text
question -> embedding -> ChromaDB similarity search -> top matching chunks
```

## 12. Common mistakes

- Thinking LangChain is the model.
- Thinking ChromaDB is the model.
- Creating embeddings before cleaning/chunking properly.
- No metadata, so sources cannot be shown.
- Persisting stale indexes after documents changed.
- Adding rerankers before basic retrieval works.
- Not evaluating whether retrieval is good.

## 13. Where used in AI Engineer work

LangChain and vector databases appear in:

- RAG knowledge assistants
- document Q&A systems
- local RAG labs
- final QA Knowledge Assistant POC
- source-grounded enterprise AI apps
- interviews about hallucination control and retrieval quality
