# 7-Day Crash Plan

Use this plan when the exam, lab, or interview is close. Each day has a learning goal, files to read, a lab to run or simulate, expected output, and a self-check.

Do not mark a day complete only because you read the files. Mark it complete when you can explain the topic and perform the small task.

## Day 1: Setup, Python basics, and Git

Goal:

Build confidence with the terminal, Python files, variables, collections, and the Git save flow.

Read:

- `01-environment-setup/README.md`
- `01-environment-setup/00-overview.md`
- `02-python-beginner-to-advanced/00-overview.md`
- `02-python-beginner-to-advanced/01-core-syntax-data-types.md`
- `04-git-version-control/00-overview.md`

Practice:

```powershell
python --version
python 01-environment-setup\practice\hello_setup.py
git status
```

Expected output:

- Python version prints successfully.
- The setup script prints its message.
- `git status` shows current repository state.

Self-check:

- Can you explain `python`, `--version`, and `git status`?
- Can you explain Git vs GitHub?
- Can you explain variable, list, dictionary, and string in simple words?

Common mistake:

Reading Git commands without running `git status` before and after a file change.

## Day 2: Python functions, JSON, files, exceptions, and pytest

Goal:

Use Python for data handling like an AI Engineer: parse dictionaries, read files, return values, and handle errors.

Read:

- `02-python-beginner-to-advanced/02-control-flow-functions.md`
- `02-python-beginner-to-advanced/03-collections-json-files.md`
- `02-python-beginner-to-advanced/04-errors-modules-requests.md`
- `02-python-beginner-to-advanced/05-oop-type-hints-dataclasses-pytest.md`

Practice:

Create a small function that accepts a requirement string and returns a dictionary:

```python
def build_test_case(requirement):
    return {"title": "Validate requirement", "requirement": requirement}

print(build_test_case("User can login"))
```

Expected output:

```text
{'title': 'Validate requirement', 'requirement': 'User can login'}
```

Self-check:

- Can you explain `def`, parameter, `return`, dictionary braces, and `print`?
- Can you explain `return` vs `print`?
- Can you explain why JSON-like dictionaries appear in APIs and LLM responses?

Common mistake:

Printing a value inside a function but forgetting to `return` it for the caller.

## Day 3: REST API, FastAPI, and Pydantic

Goal:

Understand request/response flow and validation.

Read:

- `05-rest-api-fundamentals/00-overview.md`
- `06-fastapi/00-overview.md`
- `07-pydantic/00-overview.md`

Practice:

Run or review the FastAPI implementation:

```powershell
cd 06-fastapi\implementation\fastapi-ai-helper-api
pip install -r requirements.txt
uvicorn main:app --reload
```

Expected output:

```text
Uvicorn running on http://127.0.0.1:8000
```

Verification:

Open:

```text
http://127.0.0.1:8000/docs
```

Self-check:

- Can you explain FastAPI vs Uvicorn?
- Can you explain request body vs response body?
- Can you explain why a Pydantic validation error may return HTTP `422`?

Common mistake:

Running `uvicorn app:main` when the file is `main.py` and the FastAPI object is `app`.

## Day 4: LLM fundamentals, prompt engineering, and provider API pattern

Goal:

Understand model calls without getting blocked by real API keys.

Read:

- `08-llm-fundamentals/00-overview.md`
- `09-prompt-engineering/00-overview.md`
- `10-openai-gemini-api-python/00-overview.md`
- `10-openai-gemini-api-python/01-openai-gemini-patterns.md`

Practice:

Run the mock LLM example from module 10 if dependencies are available, or trace it manually.

Expected output style:

```text
Mock response for: Generate test cases for login
```

Self-check:

- Can you explain prompt vs response?
- Can you explain token vs word?
- Can you explain why mock mode is used before real provider mode?
- Can you explain what `client.generate("prompt")` means?

Common mistake:

Hardcoding an API key in Python code.

## Day 5: RAG, MCP, LangGraph, and A2A

Goal:

Understand how AI systems use context, tools, state, and agent collaboration.

Read:

- `11-rag-langchain-vector-db/00-overview.md`
- `12-mcp-fastmcp/00-overview.md`
- `13-langgraph-stateful-agents/00-overview.md`
- `14-agents-multi-agent-systems/00-overview.md`

Practice:

Explain these four mental models aloud:

```text
RAG: question -> retrieve context -> prompt -> answer
MCP: Python function -> exposed tool -> client calls tool
LangGraph: state -> node -> edge -> next node -> final answer
A2A: Agent A asks Agent B -> Agent B returns result -> Agent A continues
```

Expected result:

You can explain each model without reading the notes.

Self-check:

- Can you compare RAG vs fine-tuning?
- Can you compare MCP vs A2A?
- Can you compare LangGraph state vs a normal variable?

Common mistake:

Calling every multi-step prompt an "agent" without tools, state, or decisions.

## Day 6: Docker, Podman awareness, Kubernetes, and Streamlit

Goal:

Understand local demo packaging and deployment basics.

Read:

- `16-docker-basics/00-overview.md`
- `17-kubernetes-basics/00-overview.md`
- `18-streamlit-app-lab/00-overview.md`

Practice:

Review or run:

```powershell
docker --version
docker build -t fastapi-docker-example .
docker run -p 8000:8000 fastapi-docker-example
```

Expected output:

- Docker version prints.
- Build logs finish successfully.
- Container starts and exposes the app.

Self-check:

- Can you explain Dockerfile, image, and container?
- Can you explain `8000:8000`?
- Can you explain Podman as Docker-like container awareness?
- Can you explain pod vs deployment vs service?

Common mistake:

Forgetting that the first port is host port and the second port is container port.

## Day 7: POC, Mettl, interview, and IBM awareness

Goal:

Prepare for screening plus stand-and-deliver discussion.

Read:

- `21-ibm-ai-engineer-awareness/00-overview.md`
- `22-final-poc-project/README.md`
- `23-mettl-screening-prep/final-rapid-revision.md`
- `24-interview-prep/01-role-and-project-explanation.md`
- `24-interview-prep/02-technical-qa.md`
- `24-interview-prep/03-poc-demo-scripts.md`

Practice:

Give a two-minute POC explanation:

```text
Problem -> solution -> architecture -> demo flow -> risks -> production improvements
```

Expected result:

You can explain the POC without reading and can answer what you would improve for production.

Self-check:

- Can you explain IBM BOB safely without inventing details?
- Can you explain Agent Studio / Agentic Studio as awareness-level enterprise tooling?
- Can you discuss credentials honestly?
- Can you answer why your POC uses mock LLM first?

Common mistake:

Overclaiming internal IBM platform knowledge or completed credentials.
