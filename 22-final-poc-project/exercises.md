# Final POC Exercises

## Exercise 1: Create The Python Environment

Task:

Create and activate a virtual environment for the POC project.

Where to run:

```text
22-final-poc-project/ai-engineer-poc-qa-assistant
```

Commands:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

What each command means:

- `python -m venv .venv` creates a local Python environment folder named `.venv`
- `.\.venv\Scripts\Activate.ps1` activates that environment in PowerShell
- `pip install -r requirements.txt` installs all packages listed in `requirements.txt`

Expected output:

```text
The prompt shows (.venv), and pip installs FastAPI, Uvicorn, Pydantic, Streamlit, and requests.
```

Self-check:

```powershell
pip show fastapi
pip show streamlit
```

Solution outline:

Run all three commands from the project folder. Do not run them from the course root.

Common mistake:

Creating `.venv` in the wrong folder and then wondering why commands do not find the project.

## Exercise 2: Run The FastAPI Backend

Task:

Start the backend server.

Command:

```powershell
uvicorn backend.main:app --reload
```

What each part means:

- `uvicorn` is the server that runs FastAPI
- `backend.main` means `main.py` inside the `backend` folder
- `app` is the FastAPI object inside `main.py`
- `--reload` restarts the server when files change

Expected output:

```text
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

How to verify:

Open:

```text
http://127.0.0.1:8000/docs
```

Self-check:

Can you explain why the command says `backend.main:app` and not only `main.py`?

Solution outline:

Run the command from `ai-engineer-poc-qa-assistant`, then open the FastAPI docs page.

Common mistake:

Running the command from `22-final-poc-project` instead of the POC project folder.

## Exercise 3: Call The Health Endpoint

Task:

Call the backend health endpoint.

Browser option:

```text
http://127.0.0.1:8000/health
```

PowerShell option:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/health
```

What the command means:

- `Invoke-RestMethod` sends an HTTP request
- `-Uri` gives the URL
- `/health` is the endpoint path

Expected output:

```json
{
  "status": "ok"
}
```

Self-check:

Can you explain why health endpoints are useful in demos and deployments?

Solution outline:

Keep the backend running and call `/health` from a browser or another terminal.

Common mistake:

Closing the backend terminal before calling the endpoint.

## Exercise 4: Ask The Knowledge Base

Task:

Send a question to the `/ask` endpoint.

Command:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/ask -Method Post -ContentType "application/json" -Body '{"question":"What should be tested for login?"}'
```

What each part means:

- `-Method Post` means send data to the backend
- `-ContentType "application/json"` tells FastAPI the body is JSON
- `-Body` contains the request data
- `question` must match the field in `AskRequest`

Expected output:

```text
The response includes the original question, a mock answer, and context_used.
```

Self-check:

Change the question and see whether `context_used` changes.

Solution outline:

Use a non-empty `question` field. Then compare the response with `data/requirements_notes.txt`.

Common mistake:

Using the wrong field name, such as `prompt` instead of `question`.

## Exercise 5: Generate Test Cases

Task:

Send a requirement to `/generate-test-cases`.

Command:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/generate-test-cases -Method Post -ContentType "application/json" -Body '{"requirement":"User can reset password using registered email"}'
```

Expected output:

```text
The response includes requirement, test_cases, context_used, and mode.
```

Expected fields:

- `requirement`
- `test_cases`
- `title`
- `type`
- `priority`
- `expected_result`
- `context_used`
- `mode`

Self-check:

Can you identify which fields come from the user, which come from retrieval, and which come from the workflow generator?

Solution outline:

Call the endpoint with a non-empty requirement and inspect the returned JSON.

Common mistake:

Expecting a real LLM answer. This POC defaults to mock mode.

## Exercise 6: Run The Streamlit UI

Task:

Start the UI and call the backend visually.

Where to run:

Open a second terminal in:

```text
22-final-poc-project/ai-engineer-poc-qa-assistant
```

Commands:

```powershell
.\.venv\Scripts\Activate.ps1
streamlit run frontend/app.py
```

Expected output:

```text
Local URL: http://localhost:8501
```

How to verify:

Open the Streamlit URL, type a question or requirement, and click the button.

Self-check:

Can you explain why the backend must already be running before clicking the Streamlit button?

Solution outline:

Keep FastAPI running in terminal 1. Run Streamlit in terminal 2.

Common mistake:

Starting only Streamlit and forgetting FastAPI.

## Exercise 7: Explain The Architecture In Two Minutes

Task:

Speak the architecture out loud without reading the code.

Required words to include:

- Streamlit
- FastAPI
- Pydantic
- REST endpoint
- RAG
- local documents
- MCP-style tool
- mock LLM
- LangGraph-style workflow
- Docker
- Kubernetes/minikube

Expected answer:

```text
The user enters a question in Streamlit. Streamlit sends a REST request to FastAPI. Pydantic validates the request. A workflow controls the steps. RAG retrieves context from local notes. A tool provides helper test data. The mock LLM generates predictable output. FastAPI returns JSON and Streamlit displays it. Docker and Kubernetes files show deployment awareness.
```

Self-check:

Record yourself once. If the explanation sounds like a list of buzzwords, redo it using the request flow.

Solution outline:

Explain the journey of one request from UI to response.

Common mistake:

Explaining every technology separately but not explaining how the request flows through the system.

## Exercise 8: Debug A 422 Validation Error

Task:

Send an invalid request and understand the error.

Command:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/generate-test-cases -Method Post -ContentType "application/json" -Body '{"requirement":""}'
```

Expected output:

```text
FastAPI returns a validation error because requirement has min_length=1.
```

Self-check:

Open `backend/models.py` and find the rule that caused the error.

Solution outline:

`TestCaseRequest` uses `Field(min_length=1)`, so an empty string is rejected.

Common mistake:

Thinking the workflow failed. The workflow did not run because Pydantic stopped the invalid request first.

## Exercise 9: Read The Dockerfile

Task:

Explain each Dockerfile instruction.

File:

```text
ai-engineer-poc-qa-assistant/Dockerfile
```

Expected explanation:

- `FROM python:3.11-slim` starts from a small Python image
- `WORKDIR /app` sets the working folder inside the container
- `COPY requirements.txt .` copies dependency list
- `RUN pip install -r requirements.txt` installs dependencies
- `COPY . .` copies project files
- `CMD [...]` starts the FastAPI backend

Self-check:

Can you explain the difference between an image and a container?

Solution outline:

Image is the packaged result. Container is the running instance.

Common mistake:

Thinking Docker automatically runs Streamlit too. This Dockerfile starts the backend.

## Exercise 10: Prepare The Final Demo

Task:

Prepare a live demo sequence.

Demo checklist:

- backend starts successfully
- `/health` works
- `/docs` opens
- Streamlit opens
- `/ask` flow works
- `/generate-test-cases` flow works
- you can explain the returned JSON
- you can explain mock mode
- you can explain production improvements

Expected output:

```text
A two-minute demo that shows one working happy path and one clear explanation of productionization.
```

Self-check:

Can someone understand the business value without reading your code?

Solution outline:

Use the script in `01-architecture-and-demo-script.md`.

Common mistake:

Spending the whole demo on setup commands and not showing the actual business flow.
