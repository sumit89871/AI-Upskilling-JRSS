# Core Syntax And Data Types

## 1. What it is

Python code is made from values, names, and instructions.

A value is actual data:

```python
"Generate test cases"
500
True
```

A variable is a name that points to a value:

```python
max_tokens = 500
```

Data types describe what kind of value a variable currently points to.

Common Python data types:

- `str` means text.
- `int` means whole number.
- `float` means decimal number.
- `bool` means `True` or `False`.
- `list` means ordered collection.
- `tuple` means ordered collection that should not normally change.
- `set` means unique unordered values.
- `dict` means key-value data.

## 2. The most important beginner idea

Python variables do not permanently own a type. The value has the type.

Example:

```python
max_tokens = 500
max_tokens = "five hundred"
```

This is allowed in Python, but it can break real projects because an API may expect `500` as a number, not `"five hundred"` as text.

In AI Engineer work, types matter because prompts, API payloads, RAG chunks, model responses, and agent state are passed between many functions and libraries.

## 3. Why it matters

If you misunderstand the data type, your code may fail even though the value "looks similar" to you.

Example:

```python
max_tokens = "500"
```

This is text because it has quotes.

```python
max_tokens = 500
```

This is a number because it has no quotes.

An LLM API configuration may accept the second value but reject the first.

## 4. Beginner mental model

```text
variable name -> value -> type
```

Example:

```python
model_name = "mock-llm"
```

Mental model:

```text
model_name -> "mock-llm" -> str
```

The variable name helps you reuse the value later. The value determines what operations are allowed.

## 5. How it works

Python reads the right side first, then stores it under the name on the left side.

```python
temperature = 0.2
```

What happens:

- Python sees `0.2`.
- Python understands it as a decimal number.
- Python creates the name `temperature`.
- Python points `temperature` to that number.

You can check a type with:

```python
print(type(temperature))
```

Expected output:

```text
<class 'float'>
```

This means Python sees `temperature` as a floating-point decimal value.

## 6. Syntax breakdown

### Assignment

```python
model_name = "mock-llm"
```

- `model_name` is the variable name.
- `=` means assign the value on the right to the name on the left.
- `"mock-llm"` is a string because it is inside quotes.

`=` in Python does not mean "mathematically equal". It means "store this value in this name".

### String

```python
prompt = "Generate test cases"
```

- Quotes create text.
- Single quotes and double quotes both work in Python.
- The text inside quotes is called a string.

### Integer

```python
retry_count = 3
```

- No quotes means this is a number.
- `3` is an integer because it has no decimal point.

### Float

```python
temperature = 0.1
```

- `0.1` is a float because it has a decimal point.
- LLM settings often use float values for temperature.

### Boolean

```python
use_mock = True
```

- `True` and `False` are booleans.
- They must start with capital letters in Python.
- `true` and `false` are invalid in Python.

### List

```python
tools = ["search", "calculator", "database"]
```

- Square brackets `[]` create a list.
- Commas separate items.
- List order is preserved.
- The first item is at index `0`, not index `1`.

Access a list item:

```python
print(tools[0])
```

Expected output:

```text
search
```

### Tuple

```python
api_version = ("v1", "stable")
```

- Parentheses `()` create a tuple.
- Tuples are used when values should be treated as fixed.
- Beginners can think of a tuple as a list you do not plan to modify.

### Set

```python
unique_tags = {"api", "rag", "api"}
```

- Curly braces can create a set when you only provide values.
- Duplicate values are stored once.
- Sets do not preserve a reliable order.

### Dictionary

```python
request_config = {
    "model": "mock-llm",
    "temperature": 0.2,
    "max_tokens": 500,
    "stream": False,
}
```

- Curly braces `{}` create a dictionary when you provide key-value pairs.
- `"model"` is a key.
- `"mock-llm"` is a value.
- The colon `:` separates key and value.
- Commas separate key-value pairs.

Access a dictionary value:

```python
print(request_config["model"])
```

Expected output:

```text
mock-llm
```

## 7. Small example

File name: `data_types.py`

Exact folder path: `02-python-beginner-to-advanced/practice/data_types.py`

Full code:

```python
model_name = "mock-llm"
max_tokens = 300
temperature = 0.1
is_enabled = True
skills = ["python", "fastapi", "rag"]
settings = {"model": model_name, "max_tokens": max_tokens}

print(type(model_name))
print(type(max_tokens))
print(type(temperature))
print(type(is_enabled))
print(skills[0])
print(settings["model"])
```

What this file is for:

This file helps you see how Python stores common values used in AI projects.

What you created manually:

- the file `data_types.py`
- all variable names
- all `print(...)` lines

What Python gives automatically:

- the `type(...)` function
- list indexing behavior
- dictionary lookup behavior

Important lines:

- `skills[0]` reads the first list item.
- `settings["model"]` reads a dictionary value by key.
- `type(model_name)` asks Python what type the current value has.

Run from the module folder:

```powershell
python .\practice\data_types.py
```

Command explanation:

- `python` starts the Python interpreter.
- `.\practice\data_types.py` is the relative path to the file.
- `.` means current folder.
- `practice` is the folder containing the file.

Expected output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
python
mock-llm
```

How to verify:

- If you see `<class 'str'>`, the string example worked.
- If you see `python`, the list indexing example worked.
- If you see `mock-llm`, the dictionary lookup example worked.

Common error:

```text
python: can't open file
```

This usually means you are running the command from the wrong folder or the file path is typed incorrectly.

## 8. Similar concepts beginners confuse

### List vs tuple

A list is normally used when items may change.

A tuple is normally used when the group of values should be treated as fixed.

### Dictionary vs JSON

A Python dictionary is an in-memory Python object.

JSON is a text format used to send data through APIs.

They look similar, but they are not the same thing.

### String number vs real number

`"500"` is text.

`500` is a number.

Use numbers for token limits, retry counts, and status codes.

Use strings for prompts, URLs, model names, and IDs.

## 9. Quick practice

Create a file named `api_payload_practice.py` inside `02-python-beginner-to-advanced/practice/`.

Task:

- create a dictionary named `api_request`
- include `endpoint`, `method`, `headers`, and `body`
- print the method
- print the body

Expected idea:

```python
api_request = {
    "endpoint": "/generate-test-cases",
    "method": "POST",
    "headers": {"Authorization": "Bearer placeholder"},
    "body": {"requirement": "User can reset password"},
}

print(api_request["method"])
print(api_request["body"])
```

Expected output:

```text
POST
{'requirement': 'User can reset password'}
```

## 10. Common mistakes

- Using list index `1` when you want the first item.
- Forgetting exact dictionary key spelling.
- Writing `true` instead of `True`.
- Storing numbers as strings.
- Confusing `{}` for a dictionary and `{value1, value2}` for a set.
- Using `=` when you meant to compare values with `==`.

## 11. Where used in AI Engineer work

- Strings are used for prompts, URLs, model names, and API keys.
- Numbers are used for token limits, retry counts, and status codes.
- Booleans are used for flags such as `use_mock_llm`.
- Lists are used for chat messages, documents, chunks, and tool lists.
- Dictionaries are used for JSON payloads, model responses, LangGraph state, and API responses.

Mettl-style questions often check whether you understand output, indexing, dictionary access, and type differences.
