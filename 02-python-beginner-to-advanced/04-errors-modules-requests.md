# Exceptions, Modules, Imports, And `requests`

## 1. What it is

An exception is an error that happens while Python code is running.

A module is a Python file or package you can load into another file.

`requests` is a popular third-party Python library used for calling HTTP APIs.

These ideas usually appear together in AI projects because AI apps often import libraries and call external services that can fail.

## 2. The most important beginner idea

Errors are not always bad. Some errors are expected situations that your code should handle clearly.

Example:

- API key is missing.
- Network is unavailable.
- API returns status code `429`.
- JSON response does not contain the key you expected.

Good code does not pretend these problems cannot happen. Good code handles them and returns useful messages.

## 3. Why it matters

AI apps call services such as OpenAI, Gemini, Ollama, vector databases, internal APIs, and MCP tools.

External calls can fail because:

- internet connection is down
- API key is wrong
- rate limit is reached
- server returns an error status
- response format changes
- local service is not running

If your POC crashes with a long traceback during a demo, it looks weak. If it returns a clear error message, it looks controlled.

## 4. Beginner mental model

```text
risky code -> try block
expected failure -> except block
safe cleanup/fallback -> return useful result
```

For imports:

```text
Python file/package -> import -> use its functions/classes
```

For API calls:

```text
Python code -> requests -> HTTP request -> server response -> parse result
```

## 5. How `try/except` works

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Syntax breakdown:

- `try` starts a block of code that may fail.
- The colon `:` starts the indented block.
- `result = 10 / 0` causes a runtime error.
- `except ZeroDivisionError:` catches that specific error type.
- The indented `print(...)` runs only if that error happens.

Expected output:

```text
Cannot divide by zero
```

What would happen without `try/except`:

Python would stop the program and print a traceback.

## 6. How imports work

```python
import json
```

Syntax breakdown:

- `import` tells Python to load a module.
- `json` is the module name.
- After import, you can use names inside the module with dot syntax.

Example:

```python
json.dumps({"status": "ok"})
```

- `json` is the module.
- `.` means access something inside the module.
- `dumps` is a function from the module.

Common mistake:

If you write `import requests` before installing `requests`, Python raises:

```text
ModuleNotFoundError: No module named 'requests'
```

Fix:

```powershell
pip install requests
```

Command explanation:

- `pip` installs Python packages.
- `install` tells pip to add a package.
- `requests` is the package name.
- Run this only after activating the correct virtual environment.

Expected output:

```text
Successfully installed requests-...
```

## 7. Calling an API with `requests`

```python
import requests

response = requests.get("https://example.com", timeout=10)
print(response.status_code)
```

Syntax breakdown:

- `requests.get(...)` sends an HTTP GET request.
- The URL string tells Python which server to call.
- `timeout=10` is a keyword argument.
- It prevents the request from waiting forever.
- `response` stores the server response object.
- `response.status_code` reads the HTTP status code.

What the developer writes manually:

- URL
- timeout
- response parsing logic
- error handling

What `requests` gives automatically:

- HTTP connection handling
- response object
- helper methods such as `.json()` and `.raise_for_status()`

## 8. API client wrapper example

```python
import requests

def fetch_health(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as error:
        return f"API call failed: {error}"
```

Syntax breakdown:

- `def fetch_health(url):` creates a reusable function.
- `url` is a parameter.
- `response.raise_for_status()` raises an exception for HTTP error statuses such as `404` or `500`.
- `except requests.RequestException as error:` catches common `requests` failures.
- `as error` stores the error object in a variable.
- The function returns a string instead of crashing.

Why this pattern matters:

Later, OpenAI/Gemini/Ollama clients use the same idea: wrap risky calls, set timeouts, catch known errors, return useful failure information.

## 9. Small example

File name: `error_handling.py`

Exact folder path: `02-python-beginner-to-advanced/practice/error_handling.py`

Full code:

```python
def read_required_key(data, key):
    try:
        return data[key]
    except KeyError:
        return f"Missing key: {key}"


api_response = {"status": "ok", "answer": "Use validation"}

print(read_required_key(api_response, "answer"))
print(read_required_key(api_response, "sources"))
```

What this file is for:

It shows how to safely read keys from API-style dictionary data.

Important lines:

- `data[key]` reads a dictionary value.
- If the key does not exist, Python raises `KeyError`.
- `except KeyError:` catches that specific problem.
- `return f"Missing key: {key}"` returns a useful message.

Run from the module folder:

```powershell
python .\practice\error_handling.py
```

Command explanation:

- `python` runs Python.
- `.\practice\error_handling.py` is the file path.
- The file runs locally and does not need internet.

Expected output:

```text
Use validation
Missing key: sources
```

How to verify:

The first line should show the existing value. The second line should show a controlled missing-key message instead of a traceback.

## 10. Similar concepts beginners confuse

### `if` vs `try/except`

Use `if` when you can check something before it fails.

Use `try/except` when an operation may fail while running.

### Module vs package

A module can be a single `.py` file.

A package is usually a folder of modules.

### `response.text` vs `response.json()`

`response.text` returns raw response text.

`response.json()` parses JSON text into Python dictionaries/lists.

Use `response.json()` only when the response is valid JSON.

## 11. Common mistakes

- Catching every error with bare `except:` and hiding real bugs.
- Not using timeouts for API calls.
- Assuming every response is valid JSON.
- Importing a package that is not installed in the active environment.
- Calling `.json()` without checking whether the server returned JSON.
- Ignoring status codes before using response content.

## 12. Quick practice

Task:

Write a function named `safe_int(text)`.

Rules:

- try to convert `text` to an integer
- catch `ValueError`
- return `"Invalid number"` when conversion fails
- test with `"42"` and `"abc"`

Expected output:

```text
42
Invalid number
```

## 13. Where used in AI Engineer work

- OpenAI and Gemini API calls
- Ollama local HTTP calls
- FastAPI error handling
- RAG file loading
- MCP tool failures
- LangGraph retry nodes
- POC demo resilience

Interview angle:

You should be able to explain why API code needs timeouts, status checks, and clear exception handling.
