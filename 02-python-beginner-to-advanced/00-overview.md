# Python Overview For AI Engineers

## 1. What It Is

Python is a programming language used heavily in AI engineering because it is readable, has strong libraries, and works well for APIs, automation, data processing, and ML/GenAI tools.

## 2. Why It Matters

AI Engineer tasks often look like this:

```text
Read input
Clean input
Create prompt or request body
Call API/model/tool
Parse response
Validate result
Return result through API/UI
Log errors
```

Each step uses Python basics.

## 3. How It Works

Python runs files from top to bottom.

Example:

```python
name = "QA Assistant"
print(name)
```

Python first stores text in `name`, then prints it.

## 4. How I Use It

In AI projects, Python files usually have different responsibilities:

- `main.py`: starts the app
- `config.py`: reads settings
- `client.py`: calls external APIs
- `models.py`: defines data shapes
- `utils.py`: stores helper functions
- `tests/`: stores test files

The developer creates these files manually unless a framework scaffolds them.

## 5. Syntax Breakdown

### Assignment

```python
topic = "RAG"
```

- `topic` is a variable name.
- `=` assigns a value.
- `"RAG"` is a string value.

### Function Call

```python
print(topic)
```

- `print` is a function.
- parentheses pass input to the function.
- `topic` is the value being printed.

### Indentation

Python uses indentation to show blocks:

```python
if topic == "RAG":
    print("Retrieval augmented generation")
```

The indented line belongs to the `if` block.

## 6. Small Examples

File name: `practice/first_python.py`

Where to create it: inside `02-python-beginner-to-advanced/practice/`

```python
course_name = "AI Engineer JRSS"
module_number = 2
is_beginner_friendly = True

print(course_name)
print(module_number)
print(is_beginner_friendly)
```

Important lines:

- `course_name` stores text.
- `module_number` stores an integer.
- `is_beginner_friendly` stores a boolean.

Run:

```powershell
python .\practice\first_python.py
```

Command breakdown:

- `python` runs the interpreter.
- `.\practice\first_python.py` points to the file to execute.

## 7. Expected Output

```text
AI Engineer JRSS
2
True
```

## 8. Quick Practice

- Create three variables: `model_name`, `token_limit`, `uses_rag`.
- Print them.
- Change one value and run again.

## 9. Common Mistakes

- Using `=` when you meant comparison with `==`.
- Forgetting quotes around text.
- Mixing tabs and spaces.
- Assuming Python ignores indentation like Java or JavaScript.

## 10. Where Used In AI Engineer Work

Python appears in:

- LLM client wrappers
- FastAPI endpoints
- RAG loaders and retrievers
- LangGraph nodes
- MCP tool functions
- Dockerized app entrypoints
- test automation utilities

## 11. Beginner Deep Dive

Python is the main glue language for this course.

Beginner mental model:

```text
data -> Python logic -> API/model/tool/file -> structured result
```

Do not study Python as isolated syntax only. Connect every concept to AI Engineer work:

- variables store prompts, URLs, and config
- dictionaries represent JSON bodies and agent state
- functions become FastAPI endpoints, MCP tools, and LangGraph nodes
- classes become API clients and Pydantic models
- exceptions protect API calls and file loading
- pytest checks helper logic before demo

What beginners often miss:

- `print` is not the same as `return`
- dictionary and JSON look similar but are not identical
- type hints do not validate data by themselves
- code indentation changes program behavior
- imports fail if packages are installed in the wrong environment

Study method:

```text
read concept -> type small file -> run it -> inspect output -> break it intentionally -> fix it
```

This is the fastest way to prepare for Mettl output questions and interview explanations.
