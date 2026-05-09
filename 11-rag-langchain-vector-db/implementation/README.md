# RAG Implementation Guide

## Project included

```text
implementation/local-rag-notes-assistant/
```

This project demonstrates a beginner local RAG notes assistant.

## What each file is for

- `.env.example`: placeholder configuration file. Do not store real keys.
- `requirements.txt`: package list.
- `data/notes.txt`: local notes used as knowledge source.
- `rag_pipeline.py`: loads notes, chunks text, and retrieves relevant context in a simple way.
- `mock_llm.py`: returns mock answers so the project works without paid API keys.
- `main.py`: entry point that connects retrieval and mock answer generation.
- `README.md`: project-specific instructions.

## Beginner RAG mental model

```text
notes.txt -> chunks -> retrieve relevant chunks -> prompt/mock LLM -> answer
```

This beginner project may use simple retrieval first. The production-style version can later use embeddings and ChromaDB.

## How to install requirements

Command:

```powershell
pip install -r requirements.txt
```

Where to run:

Run from:

```text
11-rag-langchain-vector-db/implementation/local-rag-notes-assistant/
```

What each part means:

- `pip` installs Python packages.
- `install` tells pip to install.
- `-r` means read dependencies from a file.
- `requirements.txt` contains the package names.

Expected output:

Packages are installed or shown as already satisfied.

## How to run locally

Command:

```powershell
python main.py
```

Where to run:

Run from:

```text
11-rag-langchain-vector-db/implementation/local-rag-notes-assistant/
```

What each part means:

- `python` runs Python.
- `main.py` is the entry file.

Expected output:

You should see a mock answer based on retrieved local notes.

How to verify:

Check that the answer references content related to `data/notes.txt`.

## Common errors

If `notes.txt` is missing, retrieval cannot find context.

If a package is missing, install requirements in the active environment.

If the answer is weak, inspect retrieved chunks before blaming the model.

## AI Engineer connection

RAG is used when the model should answer from project documents instead of guessing. In the final POC, this pattern supports requirement Q&A and grounded test generation.
