# FastAPI Implementation Guide

## Project included

```text
implementation/fastapi-ai-helper-api/
```

This is the runnable FastAPI practice project for the module.

## What each file is for

- `.env.example`: example environment variable file. It should not contain real secrets.
- `requirements.txt`: Python packages needed by the project.
- `main.py`: FastAPI application code.
- `README.md`: project-specific notes.

## How to install requirements

Command:

```powershell
pip install -r requirements.txt
```

Where to run:

Run from:

```text
06-fastapi/implementation/fastapi-ai-helper-api/
```

What each part means:

- `pip` installs Python packages.
- `install` tells pip to install.
- `-r` means read package names from a file.
- `requirements.txt` is the dependency list.

Expected output:

You should see packages being installed or already satisfied.

Common mistake:

Running the command from the wrong folder, so `requirements.txt` is not found.

## How to run the API

Command:

```powershell
uvicorn main:app --reload
```

Where to run:

Run from:

```text
06-fastapi/implementation/fastapi-ai-helper-api/
```

What each part means:

- `uvicorn` runs the ASGI server.
- `main` means `main.py`.
- `app` means the FastAPI object inside `main.py`.
- `--reload` restarts the server when code changes.

Expected output:

```text
Uvicorn running on http://127.0.0.1:8000
```

How to verify:

Open:

```text
http://127.0.0.1:8000/docs
```

You should see Swagger UI.

## Common errors

If `uvicorn` is not recognized, install requirements or activate the correct virtual environment.

If port `8000` is already in use, stop the other server or run on another port.

## AI Engineer connection

FastAPI is the backend layer for AI apps. It receives user requests, validates input with Pydantic, calls RAG/LLM/workflow logic, and returns JSON responses to UI or clients.
