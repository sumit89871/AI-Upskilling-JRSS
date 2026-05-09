# Environment Setup Interview Questions

## 1. What is a virtual environment?

A virtual environment is an isolated Python environment for one project. It keeps project packages separate from other projects.

## 2. Why do we use `.venv`?

We use `.venv` so package versions do not conflict between projects. A FastAPI project and a RAG project may need different versions of the same library.

## 3. What does this command do?

```powershell
python -m venv .venv
```

It runs Python's `venv` module and creates a virtual environment folder named `.venv`.

Command breakdown:

- `python` starts Python.
- `-m` runs a module as a command.
- `venv` is the built-in module for virtual environments.
- `.venv` is the target folder name.

Expected output:

Usually no output when successful.

How to verify:

Check that a `.venv` folder exists in the project.

## 4. What is `pip`?

`pip` is Python's package installer. It downloads and installs libraries such as `fastapi`, `requests`, and `python-dotenv`.

## 5. What is `requirements.txt`?

It is a dependency list for a Python project. Another developer can run `pip install -r requirements.txt` to install the same packages.

## 6. Why should API keys not be hardcoded?

Hardcoded keys can be leaked through Git, screenshots, logs, or shared files. They should be stored in environment variables or secret managers.

## 7. What is the difference between `.env` and `.env.example`?

`.env` contains real local values and should not be committed. `.env.example` contains placeholder names and can be committed to show what variables are needed.

## 8. What does `127.0.0.1` mean?

It means localhost, which is your own computer.

## 9. What is a port?

A port is a number used to access a specific running service on a machine. FastAPI often uses port `8000`.

## 10. What should you check if `ModuleNotFoundError` appears?

Check whether the package is installed, whether the virtual environment is active, and whether VS Code is using the correct Python interpreter.
