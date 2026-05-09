# RAG Cheatsheet

## RAG Flow

Syntax: `Question -> retrieve chunks -> add context to prompt -> LLM answers`

Meaning: Retrieval Augmented Generation.

Use when: Answers must come from documents.

Example: QA assistant over requirement notes.

Be careful: RAG does not train the model permanently.

## Chunk

Meaning: Smaller piece of a document.

Use when: Long files need searchable sections.

Example: split policy into paragraphs.

Be careful: Chunks too small lose context; too large may add noise.

## Embedding

Meaning: Numeric vector representing text meaning.

Use when: Similarity search is needed.

Example: store document chunk embeddings in ChromaDB.

Be careful: Embedding is not the final answer.

## Retriever

Meaning: Component that finds relevant chunks.

Use when: Building RAG pipeline.

Example: retrieve top 3 chunks for question.

Be careful: Bad retrieval causes weak answers.
