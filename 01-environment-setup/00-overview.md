# Environment Setup Overview

## 1. What environment setup is

Environment setup means preparing your computer so Python projects can run in a predictable way.

For this course, setup does not only mean "install Python". It means knowing:

- where your project folder is
- which terminal you are using
- which Python interpreter is running your code
- which packages are installed for this project
- where configuration values such as API keys are stored
- how to run a Python file, API server, Streamlit app, or test command

This matters because AI Engineer work usually combines many moving parts: Python code, API keys, FastAPI servers, RAG libraries, Docker commands, Git commands, and sometimes local models.

## 2. The most important beginner idea

Your terminal has a current folder, and your Python command uses one specific Python environment.

Most beginner setup problems come from one of these two issues:

- the command was run from the wrong folder
- the package was installed into a different Python environment than the one running the code

Do not memorize commands blindly. Always ask:

- "Where am I running this command?"
- "Which Python environment is active?"
- "What should appear after this command runs?"

## 3. Why it matters

AI engineering projects use external libraries:

- `fastapi` for API backends
- `uvicorn` for running FastAPI locally
- `pydantic` for validation
- `requests` for calling APIs
- `python-dotenv` for reading `.env` files
- `langchain` and `chromadb` for RAG experiments
- `streamlit` for quick demo UIs

If you install everything globally, one project can accidentally break another project. A virtual environment prevents that by giving each project its own isolated package folder.

## 4. Beginner mental model

```text
Project folder
  -> .venv
  -> source code files
  -> requirements.txt
  -> .env
```

- The project folder is the workspace for one app or lab.
- `.venv` is the private Python toolbox for that project.
- Source code files are the `.py` files you write manually.
- `requirements.txt` is the package list needed to recreate the environment.
- `.env` stores local configuration values such as placeholder API keys.

The `.venv` folder is created by Python. You do not manually write code inside it.

The `.py`, `requirements.txt`, and `.env.example` files are usually created or edited by the developer.

## 5. Normal project setup flow

```text
Create project folder
Move terminal into that folder
Create virtual environment
Activate virtual environment
Install packages
Write code
Run code
Save dependency list
```

The flow matters because each step depends on the previous one.

If you create `.venv` in the wrong folder, your project will be messy. If you install packages before activating `.venv`, packages may go into the global Python installation. If you forget `requirements.txt`, another person cannot easily recreate your setup.

## 6. Full beginner command flow

Run these commands from the folder where you want to create a new practice project.

```powershell
mkdir my-ai-project
cd my-ai-project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install fastapi uvicorn python-dotenv
pip freeze > requirements.txt
```

Command explanation:

- `mkdir my-ai-project` creates a new folder named `my-ai-project`.
- `mkdir` means make directory.
- `cd my-ai-project` moves the terminal into that folder.
- `cd` means change directory.
- `python -m venv .venv` creates a virtual environment folder.
- `python` means run the Python interpreter.
- `-m` means run a Python module as a command.
- `venv` is Python's built-in virtual environment module.
- `.venv` is the folder name where the isolated environment is created.
- `.\.venv\Scripts\Activate.ps1` activates the virtual environment in Windows PowerShell.
- `.` means current folder.
- `Scripts` is the Windows folder that contains activation scripts.
- `Activate.ps1` is the PowerShell activation script.
- `pip install fastapi uvicorn python-dotenv` installs three packages into the active environment.
- `pip freeze` prints installed package names and exact versions.
- `>` redirects command output into a file.
- `requirements.txt` is the dependency file created from that output.

Expected output:

```text
Directory: C:\path\to\current\folder

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        ...                         my-ai-project
```

After activation, your prompt usually changes and shows `(.venv)` at the beginning:

```text
(.venv) PS C:\path\to\my-ai-project>
```

After `pip install`, you should see package download and install messages. The exact versions may differ.

How to verify:

```powershell
python --version
pip --version
Get-ChildItem
```

Command explanation:

- `python --version` prints the Python version available in this terminal.
- `pip --version` prints the pip version and usually shows which Python environment it belongs to.
- `Get-ChildItem` lists files and folders in the current folder.

Expected output:

```text
Python 3.x.x
pip x.x from ...\.venv\...
```

`Get-ChildItem` should show project files and folders such as `.venv` and `requirements.txt`.

What this verification does:

- `python --version` confirms Python can run.
- `pip --version` confirms `pip` belongs to the active Python environment.
- `Get-ChildItem` lists files and should show `.venv` and `requirements.txt`.

## 7. What happens if a step is skipped

If you skip `cd my-ai-project`, files may be created in the wrong folder.

If you skip `python -m venv .venv`, the project has no isolated package environment.

If you skip activation, `pip install` may install packages globally or into another environment.

If you skip `pip freeze > requirements.txt`, another learner or interviewer cannot quickly see which packages the project needs.

## 8. Local-only vs production-like

Local-only means the app runs on your laptop for learning, labs, and demos.

Production-like means the app is prepared for real users and usually needs stronger handling for:

- security
- logging
- monitoring
- secret management
- Docker images
- Kubernetes deployment
- API governance

This setup module is local-first. Later Docker and Kubernetes modules show production-style packaging basics.

## 9. Common beginner confusion

### Python installed but command not found

This usually means Python was not added to `PATH`.

`PATH` is the operating system list of folders searched when you type a command.

### Package installed but import fails

This usually means you installed the package in one environment but your editor or terminal is using another.

Example confusion:

```text
pip install fastapi worked, but import fastapi fails.
```

Check whether the virtual environment is activated and whether VS Code selected the same interpreter.

### `.venv` looks huge

That is normal. It contains Python executables and installed libraries. Do not edit files inside `.venv` manually.

### `.env` is not Python code

`.env` is a plain text configuration file:

```text
OPENAI_API_KEY=your_placeholder_key_here
USE_MOCK_LLM=true
```

Python code can read these values using `python-dotenv` or environment variable APIs.

### `.env` vs `.env.example`

`.env` is local and may contain private values. Do not commit it.

`.env.example` is safe to commit because it contains placeholder values that teach others what variables are needed.

## 10. Where used in AI Engineer work

Environment setup appears when you:

- create a FastAPI backend
- run a Streamlit demo
- build a RAG notebook or script
- run a LangGraph workflow
- start an MCP server
- install OpenAI or Gemini SDKs
- prepare a Docker image
- explain your POC setup in an interview

For Mettl and interview preparation, you should be able to explain not only the command, but also what folder or file changes after the command runs.
