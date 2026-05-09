# local-rag-notes-assistant

## 1. Project goal

Build a local mock RAG assistant that:

- loads a local text file
- splits text into chunks
- retrieves chunks related to a question
- sends the retrieved context to a mock LLM
- prints a mock grounded answer

This project is intentionally mock-first.

It teaches the RAG flow without requiring:

- real embeddings
- ChromaDB
- LangChain
- OpenAI/Gemini keys
- internet access
- paid APIs

## 2. Beginner mental model

```text
notes.txt -> load text -> split into chunks -> retrieve matching chunks -> join context -> mock LLM answer
```

This is a simplified version of real RAG.

Real RAG later:

```text
notes.txt -> chunks -> embeddings -> vector DB -> similarity search -> context -> real LLM answer
```

## 3. Project structure

```text
local-rag-notes-assistant/
  README.md
  main.py
  rag_pipeline.py
  mock_llm.py
  data/
    notes.txt
  requirements.txt
  .env.example
```

## 4. What each file does

### `main.py`

Purpose:

This is the entry point for the demo.

It coordinates the flow:

```text
question -> load notes -> chunk notes -> retrieve chunks -> build context -> mock answer -> print
```

Important code:

```python
question = "How should login be tested?"
data_path = Path(__file__).parent / "data" / "notes.txt"
text = load_text(str(data_path))
chunks = chunk_text(text)
retrieved = retrieve(question, chunks)
context = "\n".join(retrieved)
answer = MockLLM().answer(question, context)
print(answer)
```

Line-by-line explanation:

- `question` stores the user question.
- `Path(__file__).parent` means the folder where `main.py` is located.
- `/ "data" / "notes.txt"` builds the path to the notes file.
- `load_text(...)` reads the notes file.
- `chunk_text(text)` splits the text into chunks.
- `retrieve(question, chunks)` finds chunks related to the question.
- `"\n".join(retrieved)` combines retrieved chunks into one context string.
- `MockLLM().answer(question, context)` creates a mock LLM object and calls its answer method.
- `print(answer)` displays the result.

What the learner creates manually:

- the question
- the data file
- the pipeline functions
- the mock LLM behavior

What Python gives automatically:

- file path handling through `pathlib`
- list handling
- string joining
- function calls

### `rag_pipeline.py`

Purpose:

This file contains the RAG helper functions.

Functions:

- `load_text(file_path)`: reads text from a file.
- `chunk_text(text, chunk_size=160)`: splits text into chunks.
- `retrieve(question, chunks)`: performs simple keyword retrieval.

Important distinction:

This is not real embedding search. It is beginner keyword retrieval.

### `mock_llm.py`

Purpose:

This file contains a fake LLM class that returns predictable text.

Important code:

```python
class MockLLM:
    def answer(self, question: str, context: str) -> str:
        return f"Mock answer for '{question}' using context: {context[:120]}"
```

Line-by-line explanation:

- `class MockLLM:` creates a class.
- `def answer(...)` creates a method.
- `question: str` means question should be text.
- `context: str` means context should be text.
- `-> str` means the method returns text.
- `context[:120]` keeps only the first 120 characters for preview.

### `data/notes.txt`

Purpose:

This is the local document used by the mock RAG assistant.

Current content includes:

```text
Login should accept valid username and password.
Login should reject invalid passwords.
Password reset should send a secure link to registered users.
API responses should include useful status codes.
```

### `requirements.txt`

Purpose:

This file is present for project structure consistency.

Current implementation uses only Python standard library, so no heavy packages are required for mock mode.

If optional real RAG is added later, this file may include packages such as:

- `langchain`
- `chromadb`
- embedding provider SDKs
- LLM provider SDKs

### `.env.example`

Purpose:

This file can document future configuration placeholders.

For mock mode, no real API key is needed.

## 5. How to run locally

Command:

```powershell
python main.py
```

Where to run:

Run from:

```text
11-rag-langchain-vector-db/implementation/local-rag-notes-assistant/
```

When to run:

Run after reading the module notes to see the RAG flow locally.

What each part means:

- `python` starts the Python interpreter.
- `main.py` is the entry file for the mock RAG assistant.

Expected output:

```text
Mock answer for 'How should login be tested?' using context: Login should accept valid username and password.
Login should reject invalid passwords.
```

The exact output may include a shortened context preview.

How to verify:

The output should include:

- the question `How should login be tested?`
- context from `data/notes.txt`
- a mock answer prefix

## 6. Optional setup command

If future packages are added to `requirements.txt`, install them with:

```powershell
pip install -r requirements.txt
```

Where to run:

Run from the project folder after activating `.venv`.

What each part means:

- `pip` installs packages.
- `install` means add packages.
- `-r` means read package names from a file.
- `requirements.txt` is the package list.

Expected output:

```text
Successfully installed ...
```

How to verify:

```powershell
pip list
```

Command explanation:

- `pip list` shows installed packages in the active environment.

Common beginner mistake:

Installing packages globally instead of inside the project virtual environment.

## 7. Mock LLM first

Mock LLM is used first because:

- it runs without paid keys
- output is predictable
- beginner can focus on RAG flow
- debugging is easier
- final POC can run during demos even without provider access

Mock LLM does not prove answer quality. It proves the pipeline wiring.

## 8. Optional real LLM later

A real LLM version would replace:

```text
MockLLM().answer(question, context)
```

with:

```text
llm_client.generate(prompt_with_context)
```

The prompt should include:

- role
- retrieved context
- user question
- instruction to answer only from context
- output format

Important:

Do not add real provider keys directly into Python files.

## 9. Optional real embeddings and ChromaDB later

Current retrieval:

```text
question words -> keyword match over chunks
```

Real retrieval later:

```text
question -> embedding -> ChromaDB similarity search -> relevant chunks
```

ChromaDB would store:

- chunk text
- embeddings
- metadata

LangChain could help with:

- document loading
- text splitting
- embedding calls
- ChromaDB retriever setup
- prompt templates

## 10. Common errors

### `FileNotFoundError`

Meaning:

Python cannot find `data/notes.txt`.

Likely cause:

The file was moved, deleted, or the path logic was changed.

### `ModuleNotFoundError`

Meaning:

Python cannot import `mock_llm` or `rag_pipeline`.

Likely cause:

You are running from the wrong folder or changed file names.

### No matching chunks found

Meaning:

The retriever did not find question words in chunks.

Likely cause:

The question and document use different wording, or keyword retrieval is too simple.

### Expecting semantic search

Meaning:

You expect embedding/vector behavior, but this implementation uses keyword matching.

Fix:

Treat this as mock-first. Add embeddings and ChromaDB later.

## 11. How this connects to the final POC

The final POC can use the same flow:

```text
requirement notes -> chunks -> retrieve relevant chunks -> build prompt -> LLM wrapper -> test cases/answer
```

This module prepares the learner to explain:

- why retrieved context matters
- why source chunks should be shown
- why mock mode is useful
- how RAG reduces hallucination risk
- how RAG connects to FastAPI and LangGraph

## 12. Beginner self-check

Before moving on, confirm you can answer:

- What file is the document?
- What is a chunk?
- What does `retrieve(...)` return?
- Why is this keyword retrieval, not vector search?
- What is context?
- What does the mock LLM do?
- What would ChromaDB add later?
- How would this connect to the final QA assistant POC?
