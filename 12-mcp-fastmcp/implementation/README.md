# MCP Implementation Examples

## 1. What this implementation folder is

This folder contains small Python examples that represent the kind of functions you may expose as MCP tools.

The files are intentionally beginner-friendly. They first show normal Python functions before adding real FastMCP server complexity.

Current files:

```text
12-mcp-fastmcp/implementation/
  calculator_server.py
  file_notes_server.py
  test_data_helper_server.py
```

Important:

These files are not a full production MCP server yet. They are MCP-style tool examples written as normal Python functions. The purpose is to understand the function logic first.

## 2. Why start with normal Python functions

FastMCP does not remove the need to understand Python.

Before a function can become a good MCP tool, the learner should understand:

- what the function receives
- what the function returns
- what type hints mean
- how to run the file
- what output to expect
- what errors may happen

After that, adding a FastMCP decorator becomes easier.

Beginner mental model:

```text
Normal Python function -> tested locally -> exposed as MCP tool -> used by an AI agent
```

## 3. Project goal

The goal of this folder is to prepare three simple MCP-style capabilities:

- calculator functions for trusted calculations
- file notes function for controlled local note reading
- test data helper functions for demo QA test data

In the final POC, similar functions can support an AI QA Knowledge Assistant and Test Case Generator.

## 4. Setup

No external package is required for the current examples.

You only need Python installed.

To check Python:

```powershell
python --version
```

Command explanation:

- `python` asks your computer to run Python.
- `--version` asks Python to print the installed version instead of running a script.
- Run this in PowerShell, Command Prompt, or VS Code terminal.

Expected output:

```text
Python 3.11.7
```

Your exact version may be different.

Common error:

```text
python is not recognized
```

Meaning:

Python is not installed correctly or not available in PATH.

How to verify:

If `python --version` prints a Python version, the examples can run.

## 5. File: calculator_server.py

Folder path:

```text
12-mcp-fastmcp/implementation/calculator_server.py
```

What this file is for:

This file contains simple calculation functions. In an MCP design, these functions could become tools that an AI agent calls when it needs trusted arithmetic.

Full code:

```python
def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    print(add(2, 3))
    print(multiply(4, 5))
```

### Line-by-line explanation

`def add(a: int, b: int) -> int:`

- `def` means define a function.
- `add` is the function name.
- `a` and `b` are input parameters.
- `: int` means each input should be an integer.
- `-> int` means the function is expected to return an integer.
- `:` starts the function body.

`return a + b`

- `return` sends a value back to whoever called the function.
- `a + b` adds the two input numbers.

`def multiply(a: int, b: int) -> int:`

- This creates another function named `multiply`.
- It also expects two integers.

`return a * b`

- `*` means multiplication in Python.

`if __name__ == "__main__":`

- This checks whether the file is being run directly.
- If the file is imported by another file, this block does not run automatically.
- This is useful because the same file can be tested directly and imported later.

`print(add(2, 3))`

- `add(2, 3)` calls the `add` function with `2` and `3`.
- `print(...)` displays the returned value in the terminal.

`print(multiply(4, 5))`

- Calls `multiply` with `4` and `5`.
- Displays the result.

### What the learner creates manually

The learner manually creates:

- the file
- both functions
- parameter names
- type hints
- return logic
- direct test code under `if __name__ == "__main__":`

### What FastMCP would provide automatically later

If this were converted to a real FastMCP server, FastMCP could provide:

- tool registration
- input schema creation from type hints
- communication between MCP client and server
- exposing the function to an AI client

FastMCP would not write the addition or multiplication logic for you.

### How to run

Run this command from:

```text
12-mcp-fastmcp/implementation/
```

Command:

```powershell
python calculator_server.py
```

Command explanation:

- `python` runs the Python interpreter.
- `calculator_server.py` is the file you want Python to execute.
- You run it from the implementation folder so Python can find the file easily.

Expected output:

```text
5
20
```

Output explanation:

- `5` comes from `add(2, 3)`.
- `20` comes from `multiply(4, 5)`.

How to verify it worked:

Check the math:

- `2 + 3 = 5`
- `4 * 5 = 20`

Common error:

```text
python: can't open file 'calculator_server.py'
```

Meaning:

You are probably running the command from the wrong folder.

Fix:

Move into the implementation folder first, or provide the full path to the file.

## 6. File: file_notes_server.py

Folder path:

```text
12-mcp-fastmcp/implementation/file_notes_server.py
```

What this file is for:

This file contains a function that reads a text note from a relative file path.

In MCP work, this is similar to a "file notes" tool or resource helper. It shows how an AI system could read approved local notes without giving it unlimited access to the whole computer.

Full code:

```python
from pathlib import Path


def read_note(file_path: str) -> str:
    safe_path = Path(file_path)
    if safe_path.is_absolute():
        return "Absolute paths are blocked in this beginner example."
    if not safe_path.exists():
        return "Note not found."
    return safe_path.read_text(encoding="utf-8")
```

### Line-by-line explanation

`from pathlib import Path`

- `from` means import something from a module.
- `pathlib` is a Python standard library module for working with file paths.
- `Path` is a class provided by `pathlib`.
- A `Path` object makes file path operations easier and safer than plain strings.

`def read_note(file_path: str) -> str:`

- Defines a function named `read_note`.
- `file_path` is the input.
- `: str` means the input should be text.
- `-> str` means the function should return text.

`safe_path = Path(file_path)`

- Converts the text path into a `Path` object.
- `safe_path` is a variable created by the developer.
- The name reminds us that we will check the path before reading.

`if safe_path.is_absolute():`

- `if` starts a condition.
- `.is_absolute()` checks whether the path is an absolute path.
- An absolute path starts from a drive or system root, such as `C:\Users\...`.

`return "Absolute paths are blocked in this beginner example."`

- If the path is absolute, the function stops and returns this message.
- This is a simple safety rule.

`if not safe_path.exists():`

- `.exists()` checks whether the file exists.
- `not` reverses the result.
- If the file does not exist, this condition is true.

`return "Note not found."`

- Returns a friendly message instead of crashing.

`return safe_path.read_text(encoding="utf-8")`

- Reads the file content as text.
- `encoding="utf-8"` tells Python how to decode the file characters.

### What the learner creates manually

The learner manually creates:

- the `read_note` function
- the safety check for absolute paths
- the missing-file handling
- the text reading behavior

### What FastMCP would provide automatically later

FastMCP could expose this function as a tool or resource, but the developer must still decide:

- which paths are allowed
- what safety checks are needed
- what output should be returned

### How to test without editing the file

Run this command from:

```text
12-mcp-fastmcp/implementation/
```

Command:

```powershell
python -c "from file_notes_server import read_note; print(read_note('missing.txt'))"
```

Command explanation:

- `python` runs Python.
- `-c` means "run the code written inside the quotes."
- `from file_notes_server import read_note` imports the `read_note` function from `file_notes_server.py`.
- `print(...)` displays the returned result.
- `read_note('missing.txt')` calls the function with a file name that probably does not exist.

Expected output:

```text
Note not found.
```

How to verify it worked:

The output should be a clean message, not a Python crash.

Common error:

```text
ModuleNotFoundError: No module named 'file_notes_server'
```

Meaning:

Python cannot find `file_notes_server.py`.

Fix:

Run the command from the same folder where `file_notes_server.py` exists.

## 7. File: test_data_helper_server.py

Folder path:

```text
12-mcp-fastmcp/implementation/test_data_helper_server.py
```

What this file is for:

This file contains helper functions that return demo test data.

In an AI QA POC, an agent could call this kind of tool when it needs approved sample usernames, passwords, or card numbers for test case examples.

Full code:

```python
def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}


def get_test_card(card_type: str) -> dict:
    return {"card_type": card_type, "number": "4111111111111111"}
```

### Line-by-line explanation

`def get_test_user(role: str) -> dict:`

- Defines a function named `get_test_user`.
- `role` is the input, such as `"admin"` or `"guest"`.
- `: str` means the role should be text.
- `-> dict` means the function returns a dictionary.

`return {"username": f"{role}_user", "password": "demo123"}`

- Returns a dictionary with two keys.
- `username` is created using the role.
- `password` is a fixed demo password.
- This should never be a real production password.

`def get_test_card(card_type: str) -> dict:`

- Defines another helper function.
- `card_type` may be `"visa"` or `"demo"`.

`return {"card_type": card_type, "number": "4111111111111111"}`

- Returns a dictionary containing card type and a demo card number.
- In real enterprise work, use only approved test data.

### How to test

Run this command from:

```text
12-mcp-fastmcp/implementation/
```

Command:

```powershell
python -c "from test_data_helper_server import get_test_user; print(get_test_user('admin'))"
```

Command explanation:

- `python` runs Python.
- `-c` runs the short code inside quotes.
- `from test_data_helper_server import get_test_user` imports the function.
- `get_test_user('admin')` calls the function with `"admin"` as the role.
- `print(...)` displays the returned dictionary.

Expected output:

```text
{'username': 'admin_user', 'password': 'demo123'}
```

Output explanation:

- `admin_user` was created from the input role.
- `demo123` is the fixed demo password.
- The curly braces show this is a Python dictionary.

Common error:

```text
NameError: name 'get_test_user' is not defined
```

Meaning:

The function was not imported or the name was typed incorrectly.

Fix:

Check the import statement and function spelling.

## 8. How these examples would become FastMCP tools

Conceptual FastMCP version:

```python
from fastmcp import FastMCP

mcp = FastMCP("qa-helper-tools")


@mcp.tool()
def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}
```

Syntax explanation:

- `from fastmcp import FastMCP` imports the FastMCP class from the installed package.
- `mcp = FastMCP("qa-helper-tools")` creates an MCP server object.
- `"qa-helper-tools"` is the server name.
- `@mcp.tool()` registers the next function as a tool.
- `def get_test_user(...)` is still normal Python function syntax.

What the developer writes manually:

- server name
- function name
- parameter names and types
- function body
- safety rules

What FastMCP gives:

- tool registration
- schema generation from type hints
- MCP protocol handling
- client discovery support

## 9. Common implementation mistakes

### Mistake 1: Thinking the current files are already running MCP servers

They are not full MCP servers yet. They are beginner Python functions that could become MCP tools.

### Mistake 2: Running commands from the wrong folder

If Python cannot find the file or module, check your current folder.

### Mistake 3: Exposing unsafe file access

File tools should restrict what can be read. Do not expose arbitrary file paths in real projects.

### Mistake 4: Using real secrets in demo test data

Never return real usernames, passwords, tokens, or customer data from demo tools.

### Mistake 5: Forgetting type hints

Type hints help build clear tool schemas.

## 10. How this connects to the final POC

In the final AI QA Knowledge Assistant POC, similar tools can be used for:

- test data lookup
- requirement note reading
- controlled helper calculations
- API payload examples
- agent workflow support

The final architecture may look like:

```text
Streamlit UI -> FastAPI backend -> LangGraph agent -> MCP tool call -> Python helper result
```

MCP is useful because it makes the tool boundary explicit. This is important for demos, interviews, and enterprise AI discussions.
