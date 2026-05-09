# Virtual Environment, pip, and requirements.txt

## 1. What It Is

A virtual environment is an isolated Python environment for one project.

`pip` is the Python package installer.

`requirements.txt` is a text file listing packages needed by a project.

## 2. Why It Matters

Without virtual environments, package versions from different projects can conflict.

Example:

- Project A needs `pydantic` version 1.
- Project B needs `pydantic` version 2.

A virtual environment lets each project keep its own dependencies.

## 3. How It Works

You create a `.venv` folder inside the project. When activated, `python` and `pip` point to that project environment.

Flow:

```text
Project folder
Create .venv
Activate .venv
Install packages
Run code
Freeze package list
```

## 4. How I Use It

Create environment:

```powershell
python -m venv .venv
```

Command breakdown:

- `python` runs Python.
- `-m` runs a Python module as a command.
- `venv` is the built-in module for creating virtual environments.
- `.venv` is the folder name where the environment is created.

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Command breakdown:

- `.` means current folder.
- `.venv` is the virtual environment folder.
- `Scripts` contains Windows activation scripts.
- `Activate.ps1` changes the current terminal session so it uses this environment.

Activate on macOS/Linux:

```bash
source .venv/bin/activate
```

Command breakdown:

- `source` runs a shell script in the current terminal session.
- `.venv/bin/activate` is the activation script on macOS/Linux.

Install packages:

```powershell
pip install requests python-dotenv
```

Command breakdown:

- `pip` installs Python packages.
- `install` tells pip to add packages.
- `requests` is a library for HTTP API calls.
- `python-dotenv` is a library for reading `.env` files.

Save dependencies:

```powershell
pip freeze > requirements.txt
```

Command breakdown:

- `pip freeze` prints installed packages and exact versions.
- `>` sends that output into a file.
- `requirements.txt` is the dependency file.

Install from dependencies:

```powershell
pip install -r requirements.txt
```

Command breakdown:

- `pip install` installs packages.
- `-r` means read package names from a file.
- `requirements.txt` is the file to read.

## 5. Syntax Breakdown

### Why `.venv` Starts With A Dot

The dot is a naming convention. It tells developers this is a tool/config folder, not project source code.

### Why `requirements.txt` Is Plain Text

It is intentionally simple:

```text
requests==2.32.3
python-dotenv==1.0.1
```

- `requests` is the package name.
- `==` pins an exact version.
- `2.32.3` is the version number.

## 6. Small Examples

File name: `practice/check_package.py`

Where to create it: inside `01-environment-setup/practice/`

```python
import requests

print("requests package imported successfully")
print(requests.__version__)
```

Important lines:

- `import requests` loads the installed package.
- `requests.__version__` reads the package version.

Run:

```powershell
python .\practice\check_package.py
```

## 7. Expected Output

The exact version may differ:

```text
requests package imported successfully
2.32.3
```

## 8. Quick Practice

- Create `.venv`.
- Activate `.venv`.
- Install `requests`.
- Run a Python file that imports `requests`.
- Generate `requirements.txt`.

## 9. Common Mistakes

### Activation Script Blocked

PowerShell may show an execution policy error.

Common local fix:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Command breakdown:

- `Set-ExecutionPolicy` changes script execution rules.
- `-ExecutionPolicy RemoteSigned` allows local scripts and signed remote scripts.
- `-Scope CurrentUser` applies the change only to your Windows user.

### Package Installed But Still Fails

Check:

```powershell
where python
where pip
```

- `where python` shows which Python executable is used.
- `where pip` shows which pip executable is used.

They should point inside `.venv` when the environment is active.

Expected output when `.venv` is active:

```text
C:\path\project\.venv\Scripts\python.exe
C:\path\project\.venv\Scripts\pip.exe
```

How to verify:

Look for `.venv` in both paths.

Common mistake:

If the paths point to a global Python installation instead of `.venv`, packages may install in the wrong place.

## 10. Where Used In AI Engineer Work

Every Python AI project uses this pattern:

- FastAPI backend: `fastapi`, `uvicorn`
- RAG app: `langchain`, `chromadb`
- LLM API app: `openai`, `google-genai`
- Streamlit demo: `streamlit`
- tests: `pytest`

## 11. Beginner Deep Dive

A virtual environment is a project-specific Python toolbox.

Beginner mental model:

```text
project folder -> .venv -> installed packages for this project only
```

`pip` installs packages into whichever Python environment is active. That is why activation matters.

`requirements.txt` is the replay list. Another learner can recreate the environment by installing packages from that file.

What the developer creates manually:

- project folder
- package choices
- `requirements.txt` update

What Python/pip creates automatically:

- `.venv` folder contents
- installed package folders
- dependency metadata

Common beginner confusion:

- `.venv` should not be committed to Git.
- `requirements.txt` should be committed.
- Installing a package once globally does not mean every virtual environment has it.
- `pip freeze` records exact installed versions, including dependencies.

Where this appears in AI Engineer work:

- FastAPI project setup
- RAG dependency setup
- Streamlit demo setup
- OpenAI/Gemini SDK setup
- pytest setup for programming assessment practice
