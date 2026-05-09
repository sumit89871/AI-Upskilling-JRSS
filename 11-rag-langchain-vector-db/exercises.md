# RAG Exercises

Use these exercises after reading the overview and pipeline notes.

The goal is to understand RAG step by step before adding real embeddings, ChromaDB, or LangChain abstractions.

## Exercise 1: Explain RAG vs fine-tuning

Task:

Write a short explanation comparing RAG and fine-tuning.

Expected answer structure:

```text
RAG retrieves relevant document chunks at runtime.
Fine-tuning changes model behavior through training.
Use RAG first when the app needs to answer from documents.
```

Expected output:

No command output is required. The expected result is a clear written explanation.

Hints:

- Use the open-book exam analogy.
- Explain that RAG does not permanently upload documents into the model.

Self-check:

Can you explain why a QA knowledge assistant should usually start with RAG instead of fine-tuning?

Solution outline:

- Define RAG.
- Define fine-tuning.
- Compare when to use each.
- Give one project example.

Common mistake:

Saying "RAG trains the model on documents." That is incorrect. RAG retrieves documents at answer time.

## Exercise 2: Create chunks from requirement notes

Task:

Take this requirement text and split it into useful chunks:

```text
Login should accept valid username and password.
Login should reject invalid passwords.
Password reset should send a secure link to registered users.
API responses should include useful status codes.
```

Expected chunks:

```text
Chunk 1: Login should accept valid username and password.
Chunk 2: Login should reject invalid passwords.
Chunk 3: Password reset should send a secure link to registered users.
Chunk 4: API responses should include useful status codes.
```

Expected output:

A list of chunks that each preserve a useful idea.

Hints:

- Do not split in the middle of a sentence.
- Keep related information together.

Self-check:

If the question is "How should login be tested?", which chunks should be retrieved?

Solution outline:

Login-related chunks should be separate enough to retrieve but complete enough to understand.

Common mistake:

Creating chunks that are too tiny, such as `Login`, `should`, `accept`, which destroys meaning.

## Exercise 3: Add metadata to chunks

Task:

Create metadata for two chunks.

Expected code:

```python
chunk_record = {
    "text": "Login should reject invalid passwords.",
    "metadata": {
        "source": "notes.txt",
        "topic": "login",
        "chunk_id": 2,
    },
}
```

Expected output:

No terminal output required. The expected result is a dictionary with text and metadata.

Hints:

- `text` stores the chunk.
- `metadata` stores source information.
- Metadata helps explain where the answer came from.

Self-check:

Can you explain why `source` matters in an enterprise AI answer?

Solution outline:

Metadata should include at least source file and topic. Add chunk ID when helpful.

Common mistake:

Storing only text with no source, making it hard to audit or cite later.

## Exercise 4: Run the local mock RAG assistant

Task:

Run the existing implementation.

Expected command:

```powershell
python main.py
```

Where to run:

Run from:

```text
11-rag-langchain-vector-db/implementation/local-rag-notes-assistant/
```

Command explanation:

- `python` runs the Python interpreter.
- `main.py` is the entry file for the mock RAG assistant.

Expected output:

```text
Mock answer for 'How should login be tested?' using context: ...
```

The output should mention the question and show context from `data/notes.txt`.

Hints:

- If the file cannot be found, check your current folder.
- This implementation uses keyword retrieval, not real embeddings.

Self-check:

Can you explain which file loads text, which file retrieves chunks, and which file creates the mock answer?

Solution outline:

- `main.py` coordinates the demo.
- `rag_pipeline.py` loads, chunks, and retrieves.
- `mock_llm.py` creates a mock answer.

Common mistake:

Expecting real vector database behavior from this mock-first implementation.

## Exercise 5: Decode the retriever function

Task:

Explain this function line by line:

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

Expected output:

No terminal output required. The expected result is a line-by-line explanation.

Hints:

- Identify the input values.
- Identify the return value.
- Explain `any(...)`.
- Explain `matches[:3]`.

Self-check:

Can you explain why this is keyword retrieval, not semantic similarity search?

Solution outline:

The function checks whether question words appear in chunks. It does not create embeddings or compare vectors.

Common mistake:

Calling this "vector search." It is not vector search. It is simple keyword-style matching.

## Exercise 6: Build a grounded prompt

Task:

Create a prompt that forces the LLM to answer using retrieved context.

Input:

```text
Context:
Login should accept valid username and password.
Login should reject invalid passwords.

Question:
How should login be tested?
```

Expected prompt:

```text
You are a QA assistant.
Use only the context below to answer.
If the context is not enough, say what is missing.

Context:
Login should accept valid username and password.
Login should reject invalid passwords.

Question:
How should login be tested?

Answer:
```

Expected output idea:

```text
Login should be tested with valid username/password and invalid password rejection scenarios.
```

Hints:

- Tell the model to use only the provided context.
- Include a fallback instruction for missing context.

Self-check:

Can you identify which part is context and which part is the task instruction?

Solution outline:

Write role, rule, context, question, and answer format.

Common mistake:

Passing chunks to the model without telling it to use them.

## Exercise 7: Evaluate RAG answer quality

Task:

Given this question and answer, evaluate whether the answer is grounded.

Context:

```text
Login should reject invalid passwords.
```

Question:

```text
Does the app lock the account after five failed logins?
```

Answer:

```text
Yes, the account locks after five failed logins.
```

Expected evaluation:

```text
Not grounded. The context says invalid passwords are rejected, but it does not mention account lockout.
```

Hints:

- Check whether every claim appears in context.
- Do not allow the answer to invent missing rules.

Self-check:

Can you rewrite the answer safely?

Solution outline:

Safer answer:

```text
The provided context only says invalid passwords are rejected. It does not state whether accounts lock after five failed logins.
```

Common mistake:

Accepting a confident answer without checking source support.
