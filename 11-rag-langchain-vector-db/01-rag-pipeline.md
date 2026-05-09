# RAG Pipeline

## 1. What a RAG pipeline is

A RAG pipeline is the step-by-step process that turns documents and a user question into a grounded answer.

Simple meaning:

```text
RAG pipeline = load documents -> retrieve useful chunks -> generate answer using those chunks
```

It is called a pipeline because each step passes output to the next step.

## 2. The most important beginner idea

RAG is not one command and not one library.

It is a flow of smaller parts.

If the final answer is bad, you must debug the pipeline step by step instead of only blaming the LLM.

Mental model:

```text
documents -> chunks -> retrieval -> context -> prompt -> generated answer -> evaluation
```

## 3. Why the pipeline exists

The pipeline exists because raw documents are not directly useful to an LLM application.

Problems:

- documents may be long
- documents may contain irrelevant text
- user questions need only some parts
- LLM context window is limited
- answer should be based on source material

The pipeline prepares and selects the right information before generation.

## 4. Step-by-step flow

### Step 1: Load documents

Load text from files, PDFs, markdown, web pages, or databases.

Beginner example:

```text
data/notes.txt -> Python reads text
```

Common mistake:

Reading from the wrong folder and getting `FileNotFoundError`.

### Step 2: Clean text

Remove or normalize messy text.

Examples:

- remove repeated blank lines
- remove page headers
- normalize spacing
- remove irrelevant boilerplate

Common mistake:

Cleaning too aggressively and removing useful context.

### Step 3: Split into chunks

Break text into smaller pieces.

Why:

The retriever searches chunks, not usually full documents.

Common mistake:

Chunks too small lose context. Chunks too large reduce retrieval precision.

### Step 4: Create embeddings

Convert chunks into numeric vectors.

Mock-first note:

The current implementation uses keyword retrieval, not real embeddings. This is intentional for beginner learning.

### Step 5: Store vectors

Store embeddings, text, and metadata in a vector database such as ChromaDB.

Mock-first note:

The current implementation stores chunks in memory as a Python list.

### Step 6: Retrieve similar chunks

Find chunks relevant to the user question.

Real RAG:

```text
question embedding -> vector DB similarity search -> top chunks
```

Mock RAG:

```text
question words -> keyword check over chunks -> matching chunks
```

### Step 7: Build grounded prompt

Put retrieved chunks into the prompt.

Example:

```text
Use only this context:
<retrieved chunks>

Question:
<user question>
```

### Step 8: Generate answer

Call a mock LLM or real LLM to write the answer.

### Step 9: Evaluate answer quality

Check:

- Did retrieval find useful chunks?
- Did the answer use the chunks?
- Did the answer invent information?
- Are sources visible?
- Is the answer useful?

## 5. Mock retrieval example

File name:

`rag_pipeline.py`

Folder path:

`11-rag-langchain-vector-db/implementation/local-rag-notes-assistant/rag_pipeline.py`

Relevant code:

```python
def retrieve(question: str, chunks: list[str]) -> list[str]:
    words = [word.lower() for word in question.split()]
    matches = []
    for chunk in chunks:
        chunk_lower = chunk.lower()
        if any(word in chunk_lower for word in words):
            matches.append(chunk)
    return matches[:3]
```

What this function is for:

It performs beginner-friendly keyword retrieval over text chunks.

Line-by-line explanation:

- `def retrieve(question: str, chunks: list[str]) -> list[str]:` creates a function named `retrieve`.
- `question: str` means the question should be text.
- `chunks: list[str]` means chunks should be a list of text strings.
- `-> list[str]` means the function returns a list of strings.
- `question.split()` breaks the question into words.
- `word.lower()` converts each word to lowercase.
- `words = [...]` stores the lowercase question words.
- `matches = []` creates an empty list for matching chunks.
- `for chunk in chunks:` loops through every chunk.
- `chunk.lower()` creates a lowercase copy for comparison.
- `any(...)` checks whether at least one question word appears in the chunk.
- `matches.append(chunk)` adds a matching chunk to the result list.
- `return matches[:3]` returns at most the first three matches.

What learner creates manually:

- function name
- matching logic
- number of chunks returned

What Python gives automatically:

- list behavior
- string `.split()`
- string `.lower()`
- loop execution
- list slicing with `[:3]`

## 6. Syntax breakdown: list comprehension

Code:

```python
words = [word.lower() for word in question.split()]
```

Read it in this order:

```text
question.split() -> for word in ... -> word.lower() -> collect into list
```

Meaning:

- `question.split()` breaks text into words.
- `for word in question.split()` loops through those words.
- `word.lower()` converts each word to lowercase.
- Square brackets collect the converted words into a new list.

Example:

```python
question = "How should Login be tested?"
words = [word.lower() for word in question.split()]
print(words)
```

Expected output:

```text
['how', 'should', 'login', 'be', 'tested?']
```

Common mistake:

This simple version keeps punctuation such as `tested?`. A production retriever may need better cleaning.

## 7. Small full example

Question:

```text
How should login be tested?
```

Available chunks:

```text
Login should accept valid username and password.
Login should reject invalid passwords.
Password reset should send a secure link to registered users.
```

Retrieved chunks should include login-related lines:

```text
Login should accept valid username and password.
Login should reject invalid passwords.
```

Grounded prompt idea:

```text
Use only this context:
Login should accept valid username and password.
Login should reject invalid passwords.

Question:
How should login be tested?
```

Expected answer idea:

```text
Test valid username/password login and invalid password rejection.
```

## 8. How to run the implementation

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

Run after reading the pipeline explanation to see the mock RAG flow work locally.

What each part means:

- `python` starts Python.
- `main.py` is the entry file for the local mock RAG assistant.

Expected output:

```text
Mock answer for 'How should login be tested?' using context: Login should accept valid username and password...
```

The exact context preview may vary based on chunking.

How to verify:

The output should include the question and context from `data/notes.txt`.

Common beginner mistake:

Running from the wrong folder and causing file path or import errors.

## 9. What can fail in each step

Document loading:

- wrong file path
- unsupported file type
- encoding issue

Cleaning:

- removed useful data
- left too much noise

Chunking:

- chunks too small
- chunks too large
- related information split badly

Embedding:

- wrong embedding model
- embedding service unavailable
- high cost if using hosted embeddings

Vector storage:

- database not persisted
- metadata missing
- index deleted

Retrieval:

- irrelevant chunks returned
- useful chunks missed
- too many chunks returned

Prompt:

- context not clearly separated
- model not told to use only context
- output format missing

Generation:

- hallucination
- incomplete answer
- bad formatting

Evaluation:

- no source check
- no manual review
- no test questions

## 10. Common mistakes

- Not printing retrieved chunks during debugging.
- Trusting the final answer without checking source context.
- Asking the LLM to answer from context but not actually passing context.
- Confusing keyword retrieval with semantic vector retrieval.
- Thinking LangChain automatically fixes bad data.
- Thinking ChromaDB is the generator.

## 11. Where used in AI Engineer work

The RAG pipeline appears in:

- knowledge assistants
- QA assistants
- requirement-based test generation
- policy Q&A bots
- final POC RAG component
- LangGraph generation workflows
- FastAPI AI endpoints
- interview architecture discussions
