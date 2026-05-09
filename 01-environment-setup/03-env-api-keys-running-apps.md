# .env Files, API Keys, and Running Local Apps

## 1. What It Is

A `.env` file stores environment-specific values such as API keys, model names, and local settings.

Example:

```text
OPENAI_API_KEY=replace_with_your_key
APP_ENV=local
```

An API key is a secret token that allows your program to call a service.

## 2. Why It Matters

Never hardcode real API keys inside Python files.

Bad:

```python
api_key = "sk-real-secret-key"
```

Better:

```python
api_key = os.getenv("OPENAI_API_KEY")
```

The code reads the key from the environment instead of storing it directly.

## 3. How It Works

Typical flow:

```text
Create .env file
Put placeholder or real local key in .env
Install python-dotenv
Load .env in Python
Read key with os.getenv
Use key only if it exists
```

## 4. How I Use It

Install helper package:

```powershell
pip install python-dotenv
```

Command breakdown:

- `pip` installs Python packages.
- `install` means add the package to the environment.
- `python-dotenv` reads `.env` files and loads values into environment variables.

File name: `practice/read_env.py`

Where to create it: inside `01-environment-setup/practice/`

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API key found")
else:
    print("API key not found. Use mock mode.")
```

Important lines:

- `import os` loads Python's operating system helper module.
- `from dotenv import load_dotenv` imports one function from the `python-dotenv` package.
- `load_dotenv()` reads the `.env` file from the current project.
- `os.getenv("OPENAI_API_KEY")` reads a value by name.
- `if api_key:` checks whether the value exists and is not empty.

Run:

```powershell
python .\practice\read_env.py
```

Command breakdown:

- `python` runs Python.
- `.\practice\read_env.py` is the file path.

## 5. Syntax Breakdown

### Import

```python
import os
```

`import` means load code from another module.

### From Import

```python
from dotenv import load_dotenv
```

This imports only `load_dotenv` from the `dotenv` module.

### Function Call

```python
load_dotenv()
```

Parentheses mean "call this function now."

### String Key

```python
"OPENAI_API_KEY"
```

Quotes make it text. Environment variable names are text keys.

## 6. Small Examples

Create `.env` in the project root:

```text
OPENAI_API_KEY=placeholder_only
```

Run the file:

```powershell
python .\practice\read_env.py
```

## 7. Expected Output

If `.env` contains the key:

```text
API key found
```

If it does not:

```text
API key not found. Use mock mode.
```

## 8. Running A Local Web App

Later, FastAPI apps will run with:

```powershell
uvicorn main:app --reload
```

Command breakdown:

- `uvicorn` starts an ASGI Python web server.
- `main:app` means find the `app` object inside `main.py`.
- `--reload` restarts the server automatically when code changes.

Local URL:

```text
http://127.0.0.1:8000
```

Meaning:

- `http` is the protocol.
- `127.0.0.1` means your own machine.
- `8000` is the port number.

## 9. Common Mistakes

- Committing `.env` to Git.
- Naming the file `env` instead of `.env`.
- Adding spaces around `=` in `.env`.
- Running Python from a folder where `.env` cannot be found.
- Assuming an API key is available in production just because it works locally.

Use `.env.example` for safe sharing:

```text
OPENAI_API_KEY=replace_with_your_key
GEMINI_API_KEY=replace_with_your_key
```

## 10. Where Used In AI Engineer Work

Environment variables are used for:

- OpenAI API keys
- Gemini API keys
- model names
- vector database paths
- FastAPI configuration
- Docker container settings
- Kubernetes secrets

## 11. Beginner Deep Dive

Environment variables keep configuration outside source code.

Beginner mental model:

```text
.env.example -> shows required names
.env -> local private values
Python code -> reads values at runtime
```

API key safety rule:

Never put real keys inside `.py` files, markdown notes, screenshots, Git commits, or demo recordings.

What the developer creates manually:

- `.env.example` with placeholder values
- `.env` locally with real or placeholder values
- code that reads environment variables
- fallback behavior when values are missing

What libraries may provide:

- `python-dotenv` can load `.env` values locally
- cloud platforms and containers can inject environment variables

Common beginner confusion:

- `.env` is not Python code.
- `.env.example` is safe to share because it should not contain real secrets.
- A missing API key should usually trigger mock mode in beginner POCs.
- Running a local web app starts a process; closing the terminal usually stops it.

Where this appears in AI Engineer work:

- OpenAI/Gemini integration
- Docker environment configuration
- Kubernetes Secrets and ConfigMaps
- FastAPI settings
- safe POC demos
