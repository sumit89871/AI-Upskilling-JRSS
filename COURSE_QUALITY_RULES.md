# Course Quality Rules

This file is the permanent quality standard for future refinement of the `AI Engineer JRSS Reskilling Course`.

Use the teaching depth and beginner clarity shown in:

- `style_reference/01-playwright-and-browser-automation-basics.md`
- `style_reference/02-typescript-for-playwright.md`

Those reference files are style benchmarks only. Do not copy their Playwright or TypeScript content unless it is directly relevant.

## 1. Audience Rule

The course is for complete beginners.

Assume the learner may not yet understand:

- terminal commands
- Python syntax
- imports
- functions
- classes
- objects
- decorators
- type hints
- JSON
- APIs
- containers
- Kubernetes YAML
- LLM terminology
- embeddings
- RAG
- MCP tools
- LangGraph state
- agent workflows

The notes must teach the meaning, not only name the concept.

## 2. Learning Notes, Not Revision Notes

Course notes must be beginner-learning notes, not short revision notes.

Bad style:

```text
Docker is used to run containers.
```

Better style:

```text
Docker packages an application with the files and runtime setup it needs so it can run consistently. A Dockerfile is the recipe, an image is the packaged result, and a container is the running instance created from that image.
```

Short does not mean shallow.

Every important note should answer:

```text
What does this actually mean?
```

## 3. One-Sentence Definition Rule

No important concept should be explained in only one sentence.

A one-sentence definition may be used as the starting point, but it must be followed by:

- practical meaning
- beginner mental model
- example
- syntax or command breakdown when relevant
- common mistake
- where it appears in AI Engineer work

## 4. Required Concept Coverage

Every important concept must explain:

- what it is
- why it exists
- what problem it solves
- beginner mental model
- how it works
- how to use it
- syntax breakdown
- small example
- expected output where useful
- common mistakes
- similar concepts beginners confuse
- where used in AI Engineer work

Recommended structure for major concept files:

```text
# Topic Name

## 1. What it is
## 2. The most important beginner idea
## 3. Why it exists
## 4. What problem it solves
## 5. Beginner mental model
## 6. How it works
## 7. How to use it
## 8. Syntax breakdown
## 9. Small example
## 10. Expected output
## 11. How to verify it worked
## 12. Common mistakes
## 13. Similar concepts beginners confuse
## 14. Where used in AI Engineer work
```

The exact headings can vary, but the learning depth must not be skipped.

## 5. Syntax Decoding Rule

Any syntax that may confuse a beginner must be decoded slowly.

Examples that require explanation:

- `def`
- `return`
- `class`
- `self`
- `__init__`
- `from x import y`
- `with open(...) as file`
- `try` / `except`
- `async` / `await`
- `list[str]`
- `dict[str, int]`
- `str | None`
- decorators such as `@app.get(...)`
- decorators such as `@mcp.tool()`
- Dockerfile instructions such as `FROM`, `COPY`, `RUN`, `CMD`
- Kubernetes YAML fields such as `apiVersion`, `kind`, `metadata`, `spec`
- LangGraph terms such as state, node, edge, checkpoint, invoke
- MCP terms such as server, client, tool, resource, schema

Use the reference-note style:

```text
Read this line in this order:
await -> page -> getByRole(...) -> click()
```

For this course, adapt that style to AI Engineer syntax.

Example:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

Must explain:

- `@app.get("/health")` is a decorator
- `app` is the FastAPI application object
- `.get(...)` registers a GET route
- `"/health"` is the URL path
- `def health():` creates a Python function
- `return {"status": "ok"}` returns a dictionary
- FastAPI automatically converts the dictionary to JSON

## 6. Command Explanation Rule

Every command must explain:

- where to run it
- when to run it
- what each part means
- expected output
- how to verify it worked
- common beginner mistake

Required command explanation format:

```text
Command:

python -m venv .venv

Where to run:

Run this from the root folder of the project.

When to run:

Run this once when creating a new Python project environment.

What each part means:

- python means run Python
- -m means run a module as a command
- venv is Python's virtual environment module
- .venv is the folder where the environment is created

Expected output:

Usually no long success message appears. A `.venv` folder should be created.

How to verify:

Run `Get-ChildItem` in PowerShell and check that `.venv` exists.

Common beginner mistake:

Running the command in the wrong folder creates `.venv` in the wrong place.
```

This rule applies to:

- Python commands
- pip commands
- uvicorn commands
- git commands
- docker commands
- docker compose commands
- kubectl commands
- curl commands
- pytest commands
- ollama commands
- streamlit commands

## 7. Code Example Rule

Every code example must explain:

- file name
- folder path
- what the file is for
- full code
- line-by-line explanation
- what learner creates manually
- what framework/library gives automatically
- how to run
- expected output
- common error

Required code example format:

```text
File name:

main.py

Folder path:

06-fastapi/implementation/fastapi-basic-app/main.py

What this file is for:

This file creates a small FastAPI app with one health-check endpoint.

Full code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

Line-by-line explanation:

- `from fastapi import FastAPI` imports the FastAPI class
- `app = FastAPI()` creates the app object
- `@app.get("/health")` registers a GET endpoint
- `def health():` creates the function FastAPI will call
- `return {"status": "ok"}` returns a dictionary
- FastAPI converts the dictionary into JSON automatically

What learner creates manually:

- the file
- the route path
- the function
- the returned dictionary

What framework gives automatically:

- route registration behavior
- JSON conversion
- Swagger UI

How to run:

uvicorn main:app --reload

Expected output:

The server starts and `/health` returns `{"status": "ok"}`.

Common error:

`Error loading ASGI app` usually means `main:app` does not match the file name or app object.
```

## 8. Exercise Quality Rule

Exercises must not be only task names.

Every exercise should include:

- task
- expected commands or code
- expected output
- hints
- self-check
- solution outline
- common mistake

Good exercise structure:

```text
Exercise 1: Create and run a FastAPI health endpoint

Task:
Create a FastAPI app with `/health`.

Expected commands:
pip install fastapi uvicorn
uvicorn main:app --reload

Expected output:
GET /health returns `{"status": "ok"}`.

Hints:
Use `app = FastAPI()` and `@app.get("/health")`.

Self-check:
Can you explain where `app` comes from and what Uvicorn runs?

Solution outline:
Create `main.py`, define the app object, add route decorator, return dictionary.

Common mistake:
Running `uvicorn app:main` when the file is `main.py` and the object is `app`.
```

## 9. Interview Question Rule

Interview questions must include:

- short answer
- expanded answer
- project example
- common wrong answer

Good interview format:

```text
Question:
What is the difference between Git and GitHub?

Short answer:
Git is the version control tool. GitHub is a cloud platform for hosting Git repositories.

Expanded answer:
Git works locally on your machine and tracks file history through commits. GitHub stores a remote copy of the repository so teams can collaborate, review code, and share changes.

Project example:
In the final POC, Git tracks changes to FastAPI, RAG, Docker, and Streamlit files. GitHub could host the project remotely.

Common wrong answer:
Git and GitHub are the same thing.
```

## 10. Cheatsheet Quality Rule

Cheatsheets must be concise but not cryptic.

Every cheatsheet entry should include:

- command/syntax
- meaning
- when to use
- example
- be careful note

Good cheatsheet entry:

```text
git add .

Meaning:
Stages all changed files in the current folder.

When to use:
Use before `git commit` when you want current changes included in the next snapshot.

Example:
git add .

Be careful:
It may stage files you did not intend to commit. Run `git status` first.
```

## 11. Beginner Confusion Rule

Every note should actively answer common beginner confusion.

Ask before finalizing a file:

- What will a beginner misunderstand here?
- What syntax looks scary?
- Where does this object/function/class come from?
- What is automatic from the framework?
- What must the developer create manually?
- What is local-only?
- What is production-like?
- What is exam-important?
- What is interview-important?
- What is POC-important?

The note should answer these inside the content.

## 12. Comparison Rule

Whenever beginners commonly confuse two things, compare them clearly.

Required comparisons include:

- Git vs GitHub
- `git add` vs `git commit`
- commit vs push
- list vs tuple
- dictionary vs JSON
- function vs method
- class vs object
- return vs print
- REST endpoint vs function
- GET vs POST
- path parameter vs query parameter
- request body vs response body
- Pydantic model vs dictionary
- Uvicorn vs FastAPI
- RAG vs fine-tuning
- embedding vs token
- vector DB vs normal DB
- retriever vs generator
- MCP server vs MCP client
- tool vs resource
- node vs function
- state vs variable
- image vs container
- Dockerfile vs docker-compose.yml
- pod vs deployment
- service vs deployment
- ConfigMap vs Secret

## 13. Minimum Depth Target

Use these minimum depth targets:

- Major concept files: usually 1200 to 2500 words
- Exercises files: useful hands-on practice, not only task names
- Interview files: answers must explain, not only list questions
- Cheatsheets: concise but not cryptic

These are targets, not strict word-count padding rules. A file should be as long as needed to teach the concept clearly.

## 14. Practicality Rule

The course must stay practical, not academic.

Prefer:

- runnable examples
- local-first setup
- mock LLM first
- optional real API integration later
- expected output
- troubleshooting
- demo explanation
- interview framing

Avoid:

- vague definitions
- theory-heavy essays
- unexplained code
- unexplained commands
- hidden assumptions
- real API keys
- production claims without caveats

## 15. Final Quality Checklist

Before marking any file complete, verify:

- A complete beginner can understand it without asking "what does this actually mean?"
- Commands include purpose, breakdown, expected output, and verification.
- Code examples include file path, full code, line explanation, run command, and expected output.
- Exercises are actionable and include self-checks.
- Interview answers are expanded with project examples.
- Cheatsheets are compact but still meaningful.
- Similar concepts are compared where confusion is likely.
- The note explains how the topic appears in AI Engineer work, Mettl screening, POC demo, or interview discussion.

## 16. Organization Material Coverage Rule

When organization-provided material such as a PPT, lab guide, screening outline, or badge roadmap is available, the course must be checked against it explicitly.

For every term listed in the organization material, the course should contain at least one of these:

- a beginner-friendly concept note
- an awareness-level explanation if the term is platform-specific
- an MCQ or screening question
- an interview answer
- a POC/demo talking point

Do not invent internal platform details, private links, or confidential behavior. If a term is mentioned but not publicly explained, teach it as controlled awareness:

```text
This term appears in the provided program material. Explain only the safe known meaning, connect it to the broader AI Engineer role, and say you would validate exact internal usage from official organization resources.
```

This rule matters for terms such as:

- IBM BOB
- Agent Studio / Agentic Studio
- IBM watsonx credentials
- hyperscaler or ISV AI credentials
- A2A
- Podman

The learner should know what to say honestly if asked. Awareness-level coverage is acceptable for internal or tool-specific items when exact details are not available.
