# RAG, LangChain, And Vector Database Overview

## 1. What RAG is

RAG means Retrieval Augmented Generation.

Do not memorize only the full form. Understand the two parts:

- Retrieval means finding relevant information.
- Generation means using an LLM to write an answer.

Simple beginner meaning:

```text
RAG = find useful document chunks first, then ask the LLM to answer using those chunks.
```

Without RAG:

```text
User question -> LLM answers from its general training/guessing
```

With RAG:

```text
User question -> retrieve relevant project notes -> put notes into prompt -> LLM answers using that context
```

## 2. The most important beginner idea

RAG does not permanently teach the model your documents.

RAG retrieves relevant pieces at answer time.

Think of it like an open-book exam:

```text
LLM alone = student answers from memory
RAG = student first opens the relevant notes, then answers using those notes
```

This one idea removes a lot of confusion.

## 3. Why RAG exists

RAG exists because LLMs have limits.

An LLM may not know:

- your private requirement notes
- your company policies
- your latest API documentation
- your current project decisions
- your test strategy
- local files on your machine

An LLM can also produce confident but unsupported answers. This is called hallucination.

RAG solves part of this problem by giving the model relevant source context before it answers.

## 4. What problem RAG solves

RAG helps when the question is:

```text
Answer using these documents.
```

Examples:

- "What does our login requirement say?"
- "Generate test cases from this requirement note."
- "What API status codes are mentioned in our notes?"
- "Answer from uploaded policy documents."
- "Summarize the test strategy from local files."

RAG is not a magic truth machine. It depends on retrieval quality and prompt quality.

## 5. Beginner mental model

Required mental model:

```text
User question
  -> convert question to embedding
  -> search vector DB
  -> retrieve relevant chunks
  -> put chunks into prompt
  -> LLM answers using context
```

Mock-first mental model used in this course:

```text
User question
  -> keyword search over chunks
  -> retrieve matching chunks
  -> put chunks into mock prompt/context
  -> mock LLM returns predictable answer
```

The mock version teaches the flow without requiring real embeddings or paid APIs.

## 6. Document

A document is the source text the RAG system can search.

Examples:

- `notes.txt`
- requirement document
- API specification
- policy PDF converted to text
- markdown course notes

Why it exists:

The document is where the knowledge comes from.

Beginner analogy:

The document is the original textbook.

Practical example:

```text
Login should accept valid username and password.
Login should reject invalid passwords.
```

Common mistake:

Thinking the model automatically knows the document. It does not unless your app loads and provides relevant text.

Where used in AI Engineer work:

Final POC requirement notes, policy assistants, QA knowledge assistants, internal document search.

## 7. Chunk

A chunk is a smaller piece of a document.

Why it exists:

Documents can be too long to send fully to the model or search effectively. Chunking breaks documents into searchable pieces.

Beginner analogy:

A chunk is like one paragraph or page section from a textbook.

Practical example:

```python
chunks = [
    "Login should accept valid username and password.",
    "Login should reject invalid passwords.",
]
```

Syntax breakdown:

- `chunks` is a Python variable.
- Square brackets `[]` create a list.
- Each quoted sentence is one string chunk.
- Commas separate list items.

Common mistake:

Chunks that are too small lose meaning. Chunks that are too large may include too much unrelated information.

Where used in AI Engineer work:

RAG retrievers usually retrieve chunks, not entire documents.

## 8. Cleaning

Cleaning means preparing text before chunking or embedding.

Why it exists:

Real documents may contain extra spaces, repeated headers, page numbers, broken lines, or irrelevant boilerplate.

Beginner analogy:

Cleaning is like removing dust and labels before organizing notes into folders.

Practical examples:

- remove empty lines
- normalize spaces
- remove repeated headers
- remove irrelevant footer text

Common mistake:

Over-cleaning and accidentally removing useful information.

Where used in AI Engineer work:

Before building a RAG index from PDFs, markdown, logs, API docs, or requirement notes.

## 9. Metadata

Metadata is information about a chunk.

It is not usually the answer itself. It describes where the chunk came from.

Example:

```python
metadata = {
    "source": "notes.txt",
    "topic": "login",
    "chunk_id": 1,
}
```

Syntax breakdown:

- Curly braces `{}` create a dictionary.
- `"source"`, `"topic"`, and `"chunk_id"` are keys.
- `"notes.txt"`, `"login"`, and `1` are values.
- Colons `:` separate keys and values.

Why it exists:

Metadata helps show sources and debug retrieval.

Beginner analogy:

Metadata is like a label on a file folder.

Common mistake:

Skipping metadata. Then the answer may use a chunk, but you cannot explain where it came from.

Where used in AI Engineer work:

Source citations, auditability, enterprise AI review, debugging RAG answers.

## 10. Embedding

An embedding is a list of numbers that represents the meaning of text.

Beginner mental model:

```text
"login password" -> embedding model -> [0.12, -0.44, 0.91, ...]
```

Why it exists:

Computers compare numbers more easily than meaning. Embeddings turn text meaning into numeric form so similar text can be searched.

Beginner analogy:

Embedding is like converting a sentence into a location on a meaning map.

Practical example:

Text A:

```text
Login should reject invalid passwords.
```

Text B:

```text
Wrong password should not allow access.
```

These do not use exactly the same words, but their embeddings may be close because the meaning is similar.

Common mistake:

Thinking embedding is the final answer. It is not. It is a numeric representation used for search.

Where used in AI Engineer work:

Vector search, RAG retrieval, semantic document search.

## 11. Vector

A vector is a list of numbers.

In RAG, a vector usually means the numeric embedding of a text chunk.

Example:

```text
[0.12, -0.44, 0.91, 0.03]
```

Why it exists:

Vectors allow similarity math.

Beginner analogy:

A vector is like coordinates on a map. Nearby coordinates mean similar meaning.

Common mistake:

Trying to read a vector like normal text. The numbers are for search math, not for humans.

Where used in AI Engineer work:

Vector databases, embeddings, similarity search, semantic retrieval.

## 12. Vector database

A vector database stores vectors and searches for similar vectors.

Why it exists:

Once documents become embeddings, you need a place to store and search those embeddings.

Beginner analogy:

A vector database is like a library catalog organized by meaning instead of exact words.

Examples:

- ChromaDB
- FAISS
- Pinecone
- Weaviate
- Milvus

Common mistake:

Thinking a vector DB is the LLM. It is not. It stores/searches embeddings. The LLM generates answers.

Where used in AI Engineer work:

RAG knowledge bases, semantic search, document assistants.

## 13. Similarity search

Similarity search finds chunks whose embeddings are close to the question embedding.

Mental model:

```text
question embedding -> find nearest chunk embeddings -> return matching chunks
```

Why it exists:

Users may ask questions using different words than the document.

Example:

Question:

```text
How do we test wrong password?
```

Relevant chunk:

```text
Login should reject invalid passwords.
```

Common mistake:

Assuming similarity search always returns the correct chunk. It can still return irrelevant chunks if embeddings, chunks, or query wording are poor.

Where used in AI Engineer work:

RAG retrieval step, semantic search, source lookup.

## 14. Retriever

A retriever is the part of the RAG system that returns relevant chunks for a question.

Why it exists:

The generator should not receive every document. It should receive only useful context.

Beginner analogy:

The retriever is the librarian who finds the most relevant pages.

Practical example:

```python
retrieved_chunks = retrieve(question, chunks)
```

Syntax breakdown:

- `retrieved_chunks` stores the result.
- `retrieve(...)` is a function.
- `question` is the user question.
- `chunks` is the list of available document chunks.

Common mistake:

Blaming the LLM when the retriever gave it bad context.

Where used in AI Engineer work:

LangChain retrievers, ChromaDB retriever interfaces, final POC context lookup.

## 15. Generator

The generator is the LLM step that writes the answer using the prompt and retrieved context.

Why it exists:

Retrieved chunks are raw text. The user needs a clear answer.

Beginner analogy:

Retriever finds the pages. Generator writes the final explanation using those pages.

Common mistake:

Letting the generator answer without telling it to use only retrieved context.

Where used in AI Engineer work:

OpenAI/Gemini wrapper, mock LLM, final POC answer/test-case generation.

## 16. Context

Context is the information given to the LLM along with the user question.

In RAG, context usually means retrieved chunks.

Example prompt:

```text
Use only this context:
Login should reject invalid passwords.

Question:
How should login be tested?
```

Why it exists:

Context grounds the answer in source material.

Common mistake:

Confusing context with prompt. Context is information. Prompt is the full instruction that may include context, task, format, and question.

Where used in AI Engineer work:

RAG prompts, LangGraph state, final POC answer generation.

## 17. Reranking basics

Reranking means reordering retrieved chunks after the first retrieval step.

Why it exists:

Initial retrieval may return many chunks, but the best chunk may not be first.

Beginner analogy:

The retriever collects candidate pages. The reranker sorts them from most useful to least useful.

Practical example:

```text
retrieve top 10 chunks -> rerank -> keep best 3 chunks
```

Common mistake:

Starting with reranking before understanding chunking and retrieval.

Where used in AI Engineer work:

More advanced RAG systems where answer quality matters.

## 18. Where LangChain fits

LangChain is a framework that helps connect RAG pieces.

It may help with:

- document loading
- text splitting
- embeddings
- vector store connection
- retriever creation
- prompt templates
- LLM calls

Important:

LangChain is not the LLM.

LangChain is not the vector database.

LangChain is a workflow/library layer that helps wire components together.

## 19. Where ChromaDB fits

ChromaDB is a vector database commonly used for local RAG practice.

It can store:

- text chunks
- embeddings
- metadata

It can search:

- similar chunks for a user question

Important:

ChromaDB does not write the final answer. The LLM or mock generator writes the answer after retrieval.

## 20. Required comparisons

### RAG vs fine-tuning

RAG retrieves external knowledge at runtime.

Fine-tuning changes model behavior through training.

Use RAG first when the model needs to answer from documents.

### Embedding vs token

Token is a small piece of text used by the model.

Embedding is a numeric vector representing meaning.

### Vector DB vs normal DB

Normal DB is good for exact structured queries.

Vector DB is good for similarity search over meaning.

### Retriever vs generator

Retriever finds context.

Generator writes the answer.

### Chunking vs summarization

Chunking splits text into pieces.

Summarization rewrites text into shorter form.

### Context vs prompt

Context is source information.

Prompt is the full instruction sent to the LLM.

### Similarity search vs keyword search

Keyword search matches words.

Similarity search matches meaning using embeddings.

## 21. Where this is used in the final POC

The final AI QA Knowledge Assistant can use RAG like this:

```text
Requirement notes
  -> chunks
  -> retrieve login/payment/API chunks
  -> build grounded prompt
  -> generate answer or test cases
  -> return structured response with sources
```

This lets the POC answer from local requirement notes instead of guessing.

## 22. Common mistakes

- Thinking RAG uploads documents permanently into the model.
- Confusing RAG with fine-tuning.
- Creating chunks without metadata.
- Trusting the answer without checking retrieved context.
- Sending too many chunks to the LLM.
- Using retrieved chunks but not instructing the model to use them.
- Not showing sources in a POC.
- Starting with advanced tools before understanding the pipeline.
