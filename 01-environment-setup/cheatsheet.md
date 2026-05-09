# Environment Setup Cheatsheet

## Check Location And Files

Command:

```powershell
Get-Location
Get-ChildItem
```

Meaning:

- `Get-Location` prints the current folder.
- `Get-ChildItem` lists files and folders.

Use when:

Before running project commands, confirm you are in the correct folder.

Expected output:

```text
Path
----
C:\Users\Sumit\Desktop\project
```

and a file/folder listing.

Be careful:

Most beginner setup errors happen because commands are run from the wrong folder.

## Move Between Folders

Command:

```powershell
cd folder-name
cd ..
```

Meaning:

- `cd folder-name` enters a folder.
- `cd ..` moves one level up.

Use when:

Navigating to a project or module folder.

Expected output:

Usually no output; the terminal location changes.

Verify with:

```powershell
Get-Location
```

## Create Virtual Environment

Command:

```powershell
python -m venv .venv
```

Meaning:

- `python` runs Python.
- `-m` runs a module as a command.
- `venv` is Python's virtual environment module.
- `.venv` is the folder where the environment is created.

Use when:

At the start of a new Python project.

Expected output:

Usually no output if successful.

Verify with:

```powershell
Get-ChildItem -Force
```

You should see a `.venv` folder.

## Activate Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Meaning:

Activate the `.venv` environment for the current terminal session.

Expected output:

Your prompt usually starts with:

```text
(.venv)
```

Common error:

PowerShell execution policy may block scripts. Use the setup note for the `Set-ExecutionPolicy` fix.

macOS/Linux:

```bash
source .venv/bin/activate
```

Meaning:

Run the activation script in the current shell session.

## Install Packages

Command:

```powershell
pip install package-name
```

Example:

```powershell
pip install fastapi uvicorn
```

Meaning:

- `pip` installs Python packages.
- `install` tells pip to add packages.
- package names are listed after `install`.

Expected output:

```text
Successfully installed fastapi uvicorn ...
```

Verify with:

```powershell
pip show fastapi
```

## Save Dependencies

Command:

```powershell
pip freeze > requirements.txt
```

Meaning:

- `pip freeze` prints installed packages and versions.
- `>` writes that output to a file.
- `requirements.txt` stores dependencies.

Expected output:

Usually no terminal output. A `requirements.txt` file is created or updated.

Verify with:

```powershell
Get-Content requirements.txt
```

## Install Dependencies From File

Command:

```powershell
pip install -r requirements.txt
```

Meaning:

- `-r` means read package names from a file.
- `requirements.txt` is the dependency list.

Expected output:

Package installation progress and `Successfully installed ...`.

Common error:

`Could not open requirements file` means the file path is wrong or the file does not exist.

## Run Python File

Command:

```powershell
python app.py
```

Meaning:

Run the Python file named `app.py`.

Use when:

Testing a script or local helper.

Expected output:

Whatever the script prints. If the file contains `print("hello")`, output is:

```text
hello
```

## Run FastAPI Later

Command:

```powershell
uvicorn main:app --reload
```

Meaning:

- `uvicorn` runs the web server.
- `main` means `main.py`.
- `app` means the FastAPI object inside that file.
- `--reload` restarts when code changes.

Expected output:

```text
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

Verify with:

```text
http://127.0.0.1:8000/docs
```

## Safe Secret Pattern

Use `.env` for local secrets:

```text
OPENAI_API_KEY=replace_with_your_key
```

Use `.env.example` for sharing:

```text
OPENAI_API_KEY=your_placeholder_here
```

Never commit real secrets.
