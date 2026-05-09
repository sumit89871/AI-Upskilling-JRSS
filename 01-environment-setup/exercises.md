# Environment Setup Exercises

## Exercise 1: Terminal Location

Run:

```powershell
Get-Location
Get-ChildItem
```

Explain in your own words:

- What folder are you in?
- What files or folders can you see?

## Exercise 2: Create A Practice Folder

Run:

```powershell
mkdir setup-practice
cd setup-practice
```

Command breakdown:

- `mkdir setup-practice` creates a folder.
- `cd setup-practice` moves into it.

Task:

- create a file named `hello.py`
- add `print("hello setup")`
- run it with `python hello.py`

## Exercise 3: Virtual Environment

Run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Task:

- confirm the terminal prompt shows `(.venv)`
- run `python --version`
- run `pip --version`

Command breakdown:

- `python --version` prints the Python version.
- `pip --version` prints the pip version and location.

## Exercise 4: Install And Import Package

Run:

```powershell
pip install requests
```

Command explanation:

- `pip` installs Python packages.
- `install` means add a package to the active environment.
- `requests` is a Python library for calling HTTP APIs.

Expected output:

```text
Successfully installed requests ...
```

How to verify:

Run `python check_requests.py` after creating the file below.

Create `check_requests.py`:

```python
import requests

print("requests works")
```

Run:

```powershell
python check_requests.py
```

Command explanation:

- `python` runs the Python interpreter.
- `check_requests.py` is the file to execute.

Expected output:

```text
requests works
```

## Exercise 5: Dependency File

Run:

```powershell
pip freeze > requirements.txt
```

Command explanation:

- `pip freeze` prints installed packages and exact versions.
- `>` writes the output into a file.
- `requirements.txt` is the file being created or overwritten.

Expected output:

Usually no terminal output.

How to verify:

Open `requirements.txt` and confirm it contains package names such as `requests`.

Open `requirements.txt`.

Write down:

- package name
- version number
- what `==` means

## Exercise 6: Safe API Key Practice

Create `.env`:

```text
OPENAI_API_KEY=placeholder_only
```

Install:

```powershell
pip install python-dotenv
```

Create `read_key.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
print("Key loaded:", bool(key))
```

Run:

```powershell
python read_key.py
```

Expected output:

```text
Key loaded: True
```

## Exercise 7: Troubleshooting

Write the likely cause for each issue:

- `python is not recognized`
- `ModuleNotFoundError: No module named 'requests'`
- `.venv activation script cannot be loaded`
- API key is `None`
- local app says port already in use
