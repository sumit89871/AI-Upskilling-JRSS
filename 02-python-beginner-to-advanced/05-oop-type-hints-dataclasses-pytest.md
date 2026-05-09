# OOP, Type Hints, Dataclasses, And `pytest`

## 1. What it is

Object-oriented programming organizes data and behavior into classes and objects.

Type hints describe the expected type of a value.

Dataclasses reduce boilerplate when you need simple data containers.

`pytest` is a testing framework used to check whether code behaves correctly.

## 2. The most important beginner idea

A class is a blueprint. An object is a real thing created from that blueprint.

Example:

```text
Class: TestCase
Object: one specific login test case
```

Do not confuse the blueprint with the created object.

## 3. Why it matters

AI Engineer projects use these ideas in practical ways:

- API clients are often classes.
- Pydantic models use class syntax and type hints.
- LangGraph state can be typed.
- Dataclasses are useful for internal structured data.
- `pytest` validates helper functions before they are used in a POC.

If you understand classes and type hints, Pydantic, FastAPI, LangGraph, and agent code become much easier to read.

## 4. Beginner mental model

```text
class -> blueprint
object -> created instance
self -> current object
method -> function attached to an object
type hint -> expected shape, not automatic validation
pytest -> check expected behavior
```

## 5. Class and object

```python
class LLMRequest:
    def __init__(self, prompt):
        self.prompt = prompt


request = LLMRequest("Summarize this")
print(request.prompt)
```

Syntax breakdown:

- `class` creates a class.
- `LLMRequest` is the class name.
- The colon `:` starts the class block.
- `def __init__(self, prompt):` defines a special initialization method.
- `__init__` runs automatically when an object is created.
- `self` means the current object being created.
- `self.prompt = prompt` stores the prompt value inside the object.
- `request = LLMRequest("Summarize this")` creates an object.
- `request.prompt` reads the prompt stored in that object.

Expected output:

```text
Summarize this
```

What the developer writes manually:

- class name
- attributes such as `prompt`
- methods and their logic

What Python gives automatically:

- object creation behavior
- method binding through `self`

## 6. Method vs function

A function can stand alone:

```python
def generate(prompt):
    return f"Mock response for: {prompt}"
```

A method belongs to a class or object:

```python
class MockLLMClient:
    def generate(self, prompt):
        return f"Mock response for: {prompt}"
```

Call the method:

```python
client = MockLLMClient()
print(client.generate("Hello"))
```

The dot `.` means "access something that belongs to this object".

## 7. Type hints

```python
def generate(self, prompt: str) -> str:
    return f"Mock response for: {prompt}"
```

Syntax breakdown:

- `prompt: str` means the `prompt` parameter is expected to be a string.
- `-> str` means the method is expected to return a string.
- Type hints help humans, editors, and tools understand the code.
- Normal Python type hints do not automatically validate runtime data.

Important comparison:

Type hints describe expected types.

Pydantic validates actual input data at runtime.

## 8. Dataclass

```python
from dataclasses import dataclass

@dataclass
class TestCase:
    title: str
    expected_result: str
    priority: str = "P3"
```

Syntax breakdown:

- `from dataclasses import dataclass` imports the `dataclass` decorator.
- `@dataclass` is a decorator.
- A decorator modifies the class below it.
- `title: str` declares a field named `title`.
- `priority: str = "P3"` declares a field with a default value.

What `@dataclass` gives automatically:

- an `__init__` method
- readable object representation
- basic comparison behavior

What the developer still writes manually:

- class name
- field names
- field types
- default values

## 9. Small example

File name: `oop_typing.py`

Exact folder path: `02-python-beginner-to-advanced/practice/oop_typing.py`

Full code:

```python
from dataclasses import dataclass


@dataclass
class TestCase:
    title: str
    expected_result: str
    priority: str = "P3"


class TestCaseFormatter:
    def format(self, test_case: TestCase) -> str:
        return f"{test_case.priority}: {test_case.title} -> {test_case.expected_result}"


test_case = TestCase(
    title="Login succeeds with valid user",
    expected_result="Dashboard is displayed",
    priority="P1",
)

formatter = TestCaseFormatter()
print(formatter.format(test_case))
```

What this file is for:

It shows how to represent a test case as structured Python data and format it using a class method.

Important lines:

- `@dataclass` creates an initializer automatically.
- `priority: str = "P3"` gives a default priority.
- `formatter = TestCaseFormatter()` creates an object.
- `formatter.format(test_case)` calls a method.
- `test_case.priority` accesses a field on the `TestCase` object.

Run from the module folder:

```powershell
python .\practice\oop_typing.py
```

Command explanation:

- `python` runs Python.
- `.\practice\oop_typing.py` points to the file.
- This script runs locally and needs no external package.

Expected output:

```text
P1: Login succeeds with valid user -> Dashboard is displayed
```

## 10. `pytest` basics

Testing means checking expected behavior automatically.

File name: `test_priority.py`

Exact folder path: `02-python-beginner-to-advanced/practice/test_priority.py`

Full code:

```python
def classify_priority(severity):
    if severity == "critical":
        return "P1"
    return "P3"


def test_critical_severity_returns_p1():
    assert classify_priority("critical") == "P1"
```

Syntax breakdown:

- Test functions normally start with `test_`.
- `assert` checks whether a condition is true.
- If the assertion is false, the test fails.
- `pytest` automatically finds functions whose names start with `test_`.

Run:

```powershell
pytest .\practice\test_priority.py
```

Command explanation:

- `pytest` runs Python tests.
- `.\practice\test_priority.py` is the specific test file.
- Run this from the module folder after installing `pytest`.

Expected output:

```text
1 passed
```

The exact output includes timing and file information, but `1 passed` is the important part.

Common setup command:

```powershell
pip install pytest
```

Command explanation:

- `pip` installs Python packages.
- `install` tells pip to install a package.
- `pytest` is the testing package.
- Install it inside the active virtual environment.

## 11. Similar concepts beginners confuse

### Class vs object

Class is the blueprint.

Object is the created instance.

### Instance variable vs local variable

`self.prompt` lives on the object.

`prompt` alone is usually a local variable or parameter.

### Type hints vs validation

Type hints guide developers and tools.

Validation checks actual data and rejects invalid input.

Pydantic performs validation. Normal type hints alone do not.

### `assert` vs `print`

`print` only displays information.

`assert` checks correctness and fails the test if the condition is false.

## 12. Common mistakes

- Forgetting `self` in class methods.
- Thinking type hints enforce validation automatically.
- Creating a class when a simple function would be enough.
- Writing tests that only print instead of asserting.
- Forgetting to install `pytest`.
- Running `pytest` from the wrong folder.

## 13. Quick practice

Task:

- create a dataclass named `Requirement`
- fields: `id`, `text`, `priority`
- create one object
- print the priority
- write one pytest test that checks the priority

Expected terminal result:

```text
1 passed
```

Self-check:

Can you explain which parts you wrote manually and which parts `@dataclass` generated automatically?

## 14. Where used in AI Engineer work

- Pydantic models use class syntax and type hints.
- FastAPI reads Pydantic models to validate request bodies.
- API clients are commonly written as classes.
- LangGraph workflows often use typed state.
- Mock LLM clients are useful in beginner POCs.
- `pytest` proves your helper logic works before demo day.
