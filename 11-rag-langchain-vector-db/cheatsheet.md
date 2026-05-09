# RAG Cheatsheet

Use this after studying the detailed notes. It is concise, but not meant to be cryptic.

## RAG

Meaning:

Retrieval Augmented Generation. Retrieve relevant context first, then generate an answer using that context.

When to use:

Use when the app must answer from documents, notes, policies, or requirements.

Example:

```text
question -> retrieve login chunks -> prompt LLM -> answer with sources
```

Be careful:

RAG reduces hallucination risk but does not guarantee truth if retrieval is poor.

## Document

Meaning:

Original source text.

When to use:

Use as the knowledge source for RAG.

Example:

`data/notes.txt`

Be careful:

The model does not know the document unless your app loads/retrieves it.

## Chunk

Meaning:

A smaller piece of a document.

When to use:

Use for retrieval because full documents may be too long or too broad.

Example:

```text
Login should reject invalid passwords.
```

Be careful:

Too-small chunks lose meaning. Too-large chunks reduce precision.

## Metadata

Meaning:

Source information about a chunk.

When to use:

Use to show citations, debug retrieval, and support auditability.

Example:

```python
{"source": "notes.txt", "topic": "login", "chunk_id": 2}
```

Be careful:

Without metadata, you may not know where an answer came from.

## Embedding

Meaning:

Numeric representation of text meaning.

When to use:

Use for semantic search.

Example:

```text
"password reset" -> [0.12, -0.44, 0.91, ...]
```

Be careful:

Embedding is not the final answer. It is used for search.

## Vector database

Meaning:

Database optimized for storing and searching embedding vectors.

When to use:

Use when you need similarity search over documents.

Example:

ChromaDB stores chunks, embeddings, and metadata.

Be careful:

A vector DB retrieves context. It does not write the final answer.

## Retriever

Meaning:

Function or object that returns relevant chunks for a question.

When to use:

Use before generation.

Example:

```python
retrieved = retrieve(question, chunks)
```

Be careful:

Bad retrieval leads to bad answers.

## Generator

Meaning:

The LLM or mock LLM that writes the final answer.

When to use:

Use after relevant chunks are retrieved and placed into a prompt.

Example:

```text
context + question -> LLM -> answer
```

Be careful:

Tell the generator to use only the provided context when grounding matters.

## RAG pipeline

Meaning:

Step-by-step RAG flow.

When to use:

Use to build and debug document Q&A systems.

Example:

```text
load -> clean -> chunk -> embed -> store -> retrieve -> prompt -> generate -> evaluate
```

Be careful:

Debug each step separately.

## RAG vs fine-tuning

Meaning:

RAG retrieves external knowledge at runtime. Fine-tuning changes model behavior through training.

When to use:

Use RAG first for document Q&A.

Be careful:

Do not say RAG trains the model.

## Similarity search vs keyword search

Meaning:

Keyword search matches exact words. Similarity search matches meaning using embeddings.

When to use:

Use keyword search for simple mock learning. Use similarity search for more realistic RAG.

Be careful:

Keyword retrieval is easier to understand but less powerful.
