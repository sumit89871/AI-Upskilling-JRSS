# Control Flow, Functions, Parameters, Return Values, And Scope

## 1. What it is

Control flow decides which lines of code run.

Functions group reusable logic under a name.

You use control flow when code must make decisions:

```python
if status_code == 200:
    print("success")
else:
    print("failed")
```

You use functions when code should be reusable:

```python
def build_prompt(requirement):
    return "Generate test cases for: " + requirement
```

## 2. The most important beginner idea

Indentation is not decoration in Python. Indentation decides which code belongs to an `if`, `for`, `while`, or `def` block.

Example:

```python
if True:
    print("inside if")
print("outside if")
```

The first `print` belongs to the `if` block because it is indented. The second `print` does not.

## 3. Why it matters

AI Engineer projects use functions everywhere:

- FastAPI endpoint functions receive API requests.
- MCP tool functions expose Python logic to AI clients.
- LangGraph node functions process state.
- Prompt builder functions create model instructions.
- Retry helper functions call APIs safely.
- Validation helper functions check structured output.

If you do not understand functions, every later framework will feel confusing.

## 4. Beginner mental model

```text
input value -> function -> returned output
```

Example:

```text
"login requirement" -> build_prompt() -> "Generate test cases for login requirement"
```

A function is like a small named machine. You give it input through parameters. It gives back output using `return`.

## 5. Conditions

Conditions allow code to choose a path.

```python
score = 85

if score >= 80:
    print("pass")
else:
    print("retry")
```

Syntax breakdown:

- `if` starts a condition.
- `score >= 80` is the condition being checked.
- `>=` means greater than or equal to.
- `:` starts the indented block.
- The indented `print("pass")` runs only if the condition is true.
- `else` runs when the `if` condition is false.

Expected output:

```text
pass
```

## 6. Loops

Loops repeat code.

```python
requirements = ["login should work", "payment should be secure"]

for requirement in requirements:
    print(requirement)
```

Syntax breakdown:

- `for` starts a loop.
- `requirement` is a temporary variable created by the loop.
- `in requirements` means take one item at a time from the list.
- `:` starts the loop block.
- The indented line runs once per item.

Expected output:

```text
login should work
payment should be secure
```

What Python does internally at beginner level:

- first loop: `requirement` becomes `"login should work"`
- second loop: `requirement` becomes `"payment should be secure"`
- loop ends because there are no more items

## 7. Functions

A function is reusable code.

```python
def build_test_case_prompt(requirement):
    prompt = f"Generate positive and negative test cases for: {requirement}"
    return prompt
```

Syntax breakdown:

- `def` means define a function.
- `build_test_case_prompt` is the function name.
- `requirement` is a parameter.
- Parentheses `()` hold parameters.
- The colon `:` starts the function body.
- Indented lines belong to the function.
- `f"..."` creates an f-string.
- `{requirement}` inserts the variable value into the string.
- `return prompt` sends the final value back to the caller.

Calling the function:

```python
result = build_test_case_prompt("User can reset password")
print(result)
```

Expected output:

```text
Generate positive and negative test cases for: User can reset password
```

## 8. Parameter vs argument

Beginners often mix these words.

A parameter is the variable name in the function definition:

```python
def build_prompt(requirement):
```

Here `requirement` is a parameter.

An argument is the actual value passed during the function call:

```python
build_prompt("User can login")
```

Here `"User can login"` is an argument.

## 9. Return vs print

`print` displays a value in the terminal.

`return` sends a value back to the code that called the function.

Example:

```python
def create_message():
    return "ready"

message = create_message()
print(message)
```

If a function only prints and does not return, other code cannot easily reuse the result.

This matters in FastAPI, MCP, LangGraph, and RAG pipelines because one function's output often becomes another function's input.

## 10. Scope

Scope means where a variable can be used.

```python
def create_prompt():
    local_prompt = "Generate tests"
    return local_prompt

print(local_prompt)
```

This fails because `local_prompt` was created inside the function.

Common error:

```text
NameError: name 'local_prompt' is not defined
```

Plain English meaning:

Python cannot find a variable with that name in the place where you are using it.

Fix:

```python
prompt = create_prompt()
print(prompt)
```

## 11. Small example

File name: `functions_flow.py`

Exact folder path: `02-python-beginner-to-advanced/practice/functions_flow.py`

Full code:

```python
def classify_priority(severity):
    if severity == "critical":
        return "P1"
    if severity == "high":
        return "P2"
    return "P3"


def build_prompt(requirement, priority):
    return f"Create test cases for {requirement}. Priority: {priority}"


requirements = ["login should work", "payment should be secure"]

for requirement in requirements:
    priority = classify_priority("high")
    prompt = build_prompt(requirement, priority)
    print(prompt)
```

What this file is for:

It shows how a test case generator can classify priority and build prompts using functions.

What you created manually:

- the two functions
- the list of requirements
- the loop that calls the functions

What Python gives automatically:

- function calling behavior
- loop iteration behavior
- f-string replacement

Run from the module folder:

```powershell
python .\practice\functions_flow.py
```

Command explanation:

- `python` runs Python.
- `.\practice\functions_flow.py` points to the file to run.
- `.` means current folder.

Expected output:

```text
Create test cases for login should work. Priority: P2
Create test cases for payment should be secure. Priority: P2
```

How to verify:

- You should see two lines because the list has two requirements.
- Both lines should show `P2` because the code passes `"high"` to `classify_priority`.

## 12. Common mistakes

- Forgetting the colon after `if`, `for`, or `def`.
- Returning too early inside a loop.
- Printing a value but not returning it.
- Using a variable outside the function where it was created.
- Passing arguments in the wrong order.
- Writing a function but never calling it.

## 13. Similar concepts beginners confuse

### Function vs method

A function is standalone.

A method is a function that belongs to an object or class.

Example:

```python
text = "hello"
print(text.upper())
```

`upper()` is a method because it belongs to the string object `text`.

### `if` vs `try/except`

Use `if` when you can check a condition normally.

Use `try/except` when code may fail with an exception, such as file reading or API calls.

### `return` vs `print`

Use `return` when another part of the program needs the value.

Use `print` when you only want to display something for the human reading the terminal.

## 14. Quick practice

Task:

Write a function named `is_success_status_code(code)`.

Rules:

- return `True` if `code` is between `200` and `299`
- return `False` otherwise
- call the function with `200`, `404`, and `500`
- print each result

Expected output:

```text
True
False
False
```

Self-check question:

If your function prints `True` but returns nothing, can FastAPI or another function reuse the result easily?

Answer:

No. Use `return` when the result must be reused.

## 15. Where used in AI Engineer work

- FastAPI endpoint functions handle HTTP requests.
- MCP tool functions expose local logic to AI clients.
- LangGraph node functions transform state.
- Prompt builder functions prepare model instructions.
- Retry functions protect API calls from temporary failure.
- Test helper functions keep programming assessments readable.

Mettl-style Python questions often test indentation, return values, loop output, scope, and function calls.
