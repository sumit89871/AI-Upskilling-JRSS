# Collections, JSON, And File Handling

## 1. What it is

Collections store multiple values in one variable.

JSON is a text format used to exchange structured data between systems.

File handling means reading data from files and writing data into files.

These three ideas work together in AI projects:

```text
file content -> Python data -> JSON payload -> API/model response -> saved result
```

## 2. The most important beginner idea

Python dictionaries and lists are not JSON, but they can be converted to and from JSON.

Python dictionary:

```python
data = {"name": "Login API", "steps": ["send request", "check response"]}
```

JSON text:

```json
{
  "name": "Login API",
  "steps": ["send request", "check response"]
}
```

They look similar, but the Python dictionary exists inside Python memory. JSON is text that can be saved to a file or sent through an API.

## 3. Why it matters

AI apps constantly move structured data:

- LLM request payloads are usually dictionaries before being sent as JSON.
- LLM responses often contain nested dictionaries and lists.
- RAG documents are loaded from files.
- Retrieved chunks are stored in lists.
- LangGraph state is commonly a dictionary.
- Test cases can be saved as JSON files.

If you cannot read nested data, you will struggle with API responses, RAG metadata, MCP tool outputs, and agent state.

## 4. Beginner mental model

```text
list -> ordered items
dict -> named values
JSON -> text version of structured data
file -> place where data is stored on disk
```

Example AI response mental model:

```text
response
  -> data
     -> answer
     -> sources
```

Python access:

```python
answer = response["data"]["answer"]
```

## 5. How nested access works

Example:

```python
response = {
    "status": "success",
    "data": {
        "answer": "Use POST for creating a resource.",
        "sources": ["api_notes.md", "rest_basics.md"],
    },
}

answer = response["data"]["answer"]
first_source = response["data"]["sources"][0]
```

Syntax breakdown:

- `response["data"]` reads the value stored under the key `"data"`.
- That value is another dictionary.
- `["answer"]` then reads the `"answer"` key from the nested dictionary.
- `["sources"]` reads a list.
- `[0]` reads the first item from that list.

Expected values:

```text
answer -> Use POST for creating a resource.
first_source -> api_notes.md
```

## 6. Modifying collections

### Add item to a list

```python
chunks = ["chunk one"]
chunks.append("chunk two")
```

Syntax breakdown:

- `chunks` is a list.
- The dot `.` means access something that belongs to the object.
- `append(...)` is a list method.
- `"chunk two"` is the new item.

Expected value:

```python
["chunk one", "chunk two"]
```

### Update dictionary value

```python
state = {"step": "start"}
state["step"] = "retrieved_context"
```

Syntax breakdown:

- `state` is a dictionary.
- `"step"` is the key.
- `=` replaces the old value with the new value.

Expected value:

```python
{"step": "retrieved_context"}
```

## 7. File handling syntax

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Syntax breakdown:

- `with` safely opens and closes the file.
- `open(...)` asks Python to open a file.
- `"notes.txt"` is the file path.
- `"r"` means read mode.
- `encoding="utf-8"` tells Python how to decode text.
- `as file` gives the opened file object a temporary name.
- The colon `:` starts the indented block.
- `file.read()` reads the full content.

What Python gives automatically:

The file is closed when the `with` block finishes.

What the developer creates manually:

The file path, the mode, and the logic for what to do with the content.

## 8. Small example

File name: `json_files.py`

Exact folder path: `02-python-beginner-to-advanced/practice/json_files.py`

Full code:

```python
import json

test_case = {
    "title": "Verify login with valid credentials",
    "steps": ["open login page", "enter username", "enter password", "click login"],
    "expected_result": "User lands on dashboard",
}

with open("test_case.json", "w", encoding="utf-8") as file:
    json.dump(test_case, file, indent=2)

with open("test_case.json", "r", encoding="utf-8") as file:
    loaded_test_case = json.load(file)

print(loaded_test_case["title"])
print(loaded_test_case["steps"][0])
```

What this file is for:

It saves a Python dictionary as JSON and reads it back.

Important lines:

- `import json` loads Python's built-in JSON module.
- `json.dump(test_case, file, indent=2)` writes a Python dictionary into a file as JSON text.
- `indent=2` makes the saved JSON readable.
- `json.load(file)` reads JSON text from a file and converts it back into Python data.
- `loaded_test_case["steps"][0]` reads the first step from a nested list.

Run from the module folder:

```powershell
python .\practice\json_files.py
```

Command explanation:

- `python` runs Python.
- `.\practice\json_files.py` points to the file.
- The file creates `test_case.json` in the current terminal folder, not necessarily inside the `practice` folder.

Expected output:

```text
Verify login with valid credentials
open login page
```

How to verify:

```powershell
Get-ChildItem
```

Expected result:

You should see `test_case.json` in the folder where you ran the Python command.

## 9. Similar concepts beginners confuse

### `json.load` vs `json.loads`

`json.load(file)` reads JSON from a file object.

`json.loads(text)` reads JSON from a string.

### `json.dump` vs `json.dumps`

`json.dump(data, file)` writes JSON into a file.

`json.dumps(data)` returns JSON as a string.

### File path vs file name

`"test_case.json"` is a relative file path. It means "look in the current working folder".

`"practice/test_case.json"` points inside the `practice` folder.

## 10. Common mistakes

- Confusing Python dict syntax with JSON syntax.
- Forgetting JSON keys must use double quotes in real JSON.
- Reading a file from the wrong folder.
- Using `json.loads` when the data is already a dictionary.
- Assuming every API response has every key.
- Accessing `response["answer"]` when the answer is actually inside `response["data"]["answer"]`.

## 11. Quick practice

Task:

- create a dictionary for an LLM response
- include `answer`, `confidence`, and `sources`
- save it to `answer.json`
- read it back
- print `answer`

Expected output:

```text
Your answer text here
```

Self-check:

If `answer.json` appears in a different folder than expected, what should you check?

Answer:

Check the terminal's current folder before running the Python command.

## 12. Where used in AI Engineer work

- OpenAI and Gemini request payloads
- FastAPI request and response bodies
- Pydantic `model_dump()` output
- RAG document metadata
- LangGraph state dictionaries
- MCP tool inputs and outputs
- POC result export files
