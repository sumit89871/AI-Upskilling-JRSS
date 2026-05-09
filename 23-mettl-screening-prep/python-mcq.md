# Python MCQs

## MCQ 1: Variable assignment

Question:

```python
x = 10
x = x + 5
print(x)
```

What is printed?

Options:

A. `10`  
B. `15`  
C. `x + 5`  
D. Error

Correct answer:

B. `15`

Explanation:

`x = 10` stores `10` in `x`. `x = x + 5` reads the old value `10`, adds `5`, and stores the new value `15` back into `x`.

Why other options are wrong:

A is the old value before reassignment. C is not printed because Python evaluates the expression. D is wrong because the code is valid.

Common trap:

Thinking `x = x + 5` is an algebra equation. In Python, `=` means assignment, not equality.

## MCQ 2: List mutation

Question:

```python
items = ["api", "rag"]
items.append("mcp")
print(items)
```

Options:

A. `["api", "rag"]`  
B. `["mcp"]`  
C. `["api", "rag", "mcp"]`  
D. Error

Correct answer:

C. `["api", "rag", "mcp"]`

Explanation:

`append()` modifies the existing list by adding one item at the end.

Why other options are wrong:

A ignores the append. B would be true only if a new list with only `mcp` was created. D is wrong because `append()` is valid for lists.

Common trap:

Forgetting that lists are mutable, which means they can be changed after creation.

## MCQ 3: Dictionary access

Question:

```python
user = {"name": "Asha", "role": "qa"}
print(user["role"])
```

Options:

A. `Asha`  
B. `qa`  
C. `role`  
D. Error

Correct answer:

B. `qa`

Explanation:

`user["role"]` reads the value stored under the key `"role"`.

Why other options are wrong:

A is the value for `"name"`. C is the key, not the value. D is wrong because `"role"` exists.

Common trap:

Confusing dictionary keys and values.

## MCQ 4: Missing dictionary key

Question:

```python
data = {"status": "ok"}
print(data["message"])
```

Options:

A. `None`  
B. Empty string  
C. `KeyError`  
D. `message`

Correct answer:

C. `KeyError`

Explanation:

Bracket access requires the key to exist. Since `"message"` is not present, Python raises a `KeyError`.

Why other options are wrong:

Python does not automatically return `None` or empty string for missing keys with bracket access.

Common trap:

Confusing `data["message"]` with `data.get("message")`. `get()` can return `None`; bracket access raises an error.

## MCQ 5: Function return

Question:

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

Options:

A. `2`  
B. `3`  
C. `5`  
D. `None`

Correct answer:

C. `5`

Explanation:

`return a + b` sends `5` back to the caller. `result` stores that returned value.

Common trap:

Confusing `return` with `print`. `return` gives a value back to code. `print` displays a value in the terminal.

## MCQ 6: Function without return

Question:

```python
def greet():
    print("hello")

value = greet()
print(value)
```

Options:

A. Only `hello`  
B. `hello` then `None`  
C. Only `None`  
D. Error

Correct answer:

B. `hello` then `None`

Explanation:

`greet()` prints `hello`. Since the function has no `return`, it returns `None` automatically. Then `print(value)` prints `None`.

Common trap:

Thinking anything printed by a function is also returned by the function.

## MCQ 7: Boolean condition

Question:

```python
score = 80
if score >= 75:
    print("pass")
else:
    print("fail")
```

Options:

A. `pass`  
B. `fail`  
C. `True`  
D. Error

Correct answer:

A. `pass`

Explanation:

`80 >= 75` is true, so Python runs the indented block under `if`.

Common trap:

Thinking Python prints the boolean condition itself. It only prints what the code tells it to print.

## MCQ 8: `is` vs `==`

Question:

Which operator should usually be used to compare two values for equality?

Options:

A. `is`  
B. `==`  
C. `=`  
D. `!=`

Correct answer:

B. `==`

Explanation:

`==` checks whether values are equal. `is` checks whether two names refer to the same object in memory.

Why other options are wrong:

`=` assigns a value. `!=` checks not equal. `is` is not the normal value equality operator.

Common trap:

Using `is` for string or number equality in beginner code.

## MCQ 9: Exception handling

Question:

What does `except ZeroDivisionError:` catch?

Options:

A. Any error  
B. Only division by zero errors  
C. Syntax errors only  
D. No errors

Correct answer:

B. Only division by zero errors

Explanation:

`ZeroDivisionError` is raised when code attempts division by zero, such as `10 / 0`.

Common trap:

Thinking every `except` catches every error. Specific exception types catch specific errors.

## MCQ 10: Type hints

Question:

What does this mean?

```python
def ask(question: str) -> str:
    return "answer"
```

Options:

A. `question` should be a string and the function should return a string  
B. Python will always reject non-string input automatically  
C. The function returns an integer  
D. `question` is optional

Correct answer:

A. `question` should be a string and the function should return a string

Explanation:

Type hints describe expected types. Normal Python does not always enforce them at runtime.

Common trap:

Thinking type hints are the same as runtime validation. Pydantic can validate runtime data; type hints alone usually do not.
