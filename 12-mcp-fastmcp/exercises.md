# MCP and FastMCP Exercises

These exercises focus on understanding MCP concepts through small Python functions first. Do not worry about production MCP hosting yet. The goal is to understand what becomes a tool, what input/output means, and how an AI agent would use it.

## Exercise 1: Run the calculator helper

### Task

Run the existing calculator helper and explain the output.

Starting file:

```text
12-mcp-fastmcp/implementation/calculator_server.py
```

Expected command:

```powershell
python calculator_server.py
```

Where to run it:

Run it from:

```text
12-mcp-fastmcp/implementation/
```

Command explanation:

- `python` runs the Python interpreter.
- `calculator_server.py` is the file Python should execute.
- The file contains an `if __name__ == "__main__":` block, so it prints test results when run directly.

Expected output:

```text
5
20
```

Expected result explanation:

- `5` is the result of `add(2, 3)`.
- `20` is the result of `multiply(4, 5)`.

Hint:

If the command cannot find the file, check whether your terminal is inside the implementation folder.

Self-check:

- Can you point to the exact line that prints `5`?
- Can you explain why `multiply(4, 5)` returns `20`?
- Can you say which functions could become MCP tools later?

Solution outline:

1. Open terminal.
2. Change into `12-mcp-fastmcp/implementation/`.
3. Run `python calculator_server.py`.
4. Match each output line to the function call.

Common mistake:

Running the command from `12-mcp-fastmcp/` instead of `12-mcp-fastmcp/implementation/` may cause Python to fail to find the file.

## Exercise 2: Identify tool input and output

### Task

Look at this function:

```python
def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}
```

Answer:

- What is the tool input?
- What is the tool output?
- What type is the input?
- What type is the output?
- What would an AI agent ask this tool for?

Expected answer:

- Tool input: `role`
- Input type: `str`
- Tool output: dictionary with `username` and `password`
- Output type: `dict`
- Agent use: get approved demo test user data for a role

Hint:

Read the function signature first:

```python
def get_test_user(role: str) -> dict:
```

The part inside parentheses tells you the input. The arrow tells you the expected output type.

Self-check:

Can you explain what happens if the input is `"admin"`?

Expected output for `"admin"`:

```python
{"username": "admin_user", "password": "demo123"}
```

Common mistake:

Saying the input is `"username"`. That is incorrect. `"username"` is a key inside the returned dictionary. The input is `role`.

## Exercise 3: Test the test data helper from the terminal

### Task

Call `get_test_user("admin")` without modifying the file.

Expected command:

```powershell
python -c "from test_data_helper_server import get_test_user; print(get_test_user('admin'))"
```

Where to run it:

```text
12-mcp-fastmcp/implementation/
```

Command explanation:

- `python` runs Python.
- `-c` means run the code inside quotes.
- `from test_data_helper_server import get_test_user` imports the function.
- `get_test_user('admin')` calls the function with role `admin`.
- `print(...)` displays the return value.

Expected output:

```text
{'username': 'admin_user', 'password': 'demo123'}
```

Hint:

The file name is `test_data_helper_server.py`, but when importing it, you write `test_data_helper_server` without `.py`.

Self-check:

- Why do we not include `.py` in the import?
- What does the returned dictionary contain?
- Would this be safe with real production passwords?

Solution outline:

1. Open terminal in the implementation folder.
2. Run the command.
3. Confirm the output has `admin_user`.
4. Explain that this would be a demo-only tool in real projects.

Common mistake:

Writing:

```python
from test_data_helper_server.py import get_test_user
```

This is wrong because Python imports modules by module name, not file name with extension.

## Exercise 4: Create a new environment URL helper

### Task

Create a function that returns a demo URL for an environment.

Create or add this code in a practice file inside the implementation folder:

```text
12-mcp-fastmcp/implementation/practice_environment_helper.py
```

Expected code:

```python
def get_environment_url(env: str) -> dict:
    return {"env": env, "url": f"https://{env}.demo.example.com"}


if __name__ == "__main__":
    print(get_environment_url("qa"))
```

What this file is for:

This file practices creating a function that could become an MCP tool later.

Line explanation:

- `def get_environment_url(env: str) -> dict:` defines a function.
- `env` is the input, such as `"qa"` or `"dev"`.
- `-> dict` means the output should be a dictionary.
- `f"https://{env}.demo.example.com"` creates a string using the `env` value.
- `print(...)` displays the result when the file is run directly.

Expected command:

```powershell
python practice_environment_helper.py
```

Expected output:

```text
{'env': 'qa', 'url': 'https://qa.demo.example.com'}
```

Hint:

Use the calculator file as a pattern. A file can contain functions and a small direct test block.

Self-check:

- What is the tool input?
- What is the tool output?
- What would the schema say about `env`?
- Why should this function return a dictionary instead of only a URL string?

Solution outline:

1. Create `practice_environment_helper.py`.
2. Add the function and direct test block.
3. Run the file with Python.
4. Confirm the output URL contains `qa`.

Common mistake:

Forgetting the `f` before the string:

```python
"https://{env}.demo.example.com"
```

This would output the literal text `{env}` instead of replacing it with `qa`.

## Exercise 5: Convert a normal function into a conceptual MCP tool

### Task

Take this normal function:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Write what it would look like conceptually as a FastMCP tool.

Expected code:

```python
from fastmcp import FastMCP

mcp = FastMCP("calculator-tools")


@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b
```

Expected explanation:

- `FastMCP` is the class used to create the MCP server object.
- `mcp` is the server object.
- `@mcp.tool()` exposes the next function as a tool.
- `add` is still a normal Python function.
- `a` and `b` become tool inputs.
- The return value becomes the tool output.

Hint:

The decorator goes directly above the function it exposes.

Self-check:

- What does the learner create manually?
- What does FastMCP provide?
- Is `@mcp.tool()` the calculation logic?

Solution outline:

1. Import `FastMCP`.
2. Create a server object.
3. Place `@mcp.tool()` above the function.
4. Keep the function body unchanged.

Common mistake:

Thinking the decorator performs the addition. It does not. The function body still performs the addition.

## Exercise 6: Decide tool, resource, or prompt

### Task

For each item, decide whether it should be a tool, resource, or prompt.

Items:

1. A function that returns demo login credentials.
2. A project requirement document.
3. A reusable instruction for generating test scenarios.
4. A function that validates whether an API response has required fields.
5. A glossary of project terms.

Expected answer:

1. Tool
2. Resource
3. Prompt
4. Tool
5. Resource

Hint:

Use this rule:

```text
Does work = tool
Gives data = resource
Reusable instruction = prompt
```

Self-check:

Can you explain why item 4 is a tool and not a resource?

Solution outline:

Item 4 is a tool because it performs validation logic. It does not only return a static document.

Common mistake:

Calling everything a tool because it is available from the server. Availability does not decide the category. Purpose decides the category.

## Exercise 7: Explain the agent tool-calling flow

### Task

Write the flow for this user request:

```text
Give me test data for a guest user.
```

Expected flow:

```text
User asks for guest user test data
Agent checks available tools
Agent selects get_test_user
Agent sends role="guest"
MCP server runs get_test_user
Tool returns {"username": "guest_user", "password": "demo123"}
Agent writes final answer using the tool result
```

Hint:

Do not say the model "knows" the password. In a safe design, the model gets it from the tool.

Self-check:

- Where is the tool input?
- Where is the tool output?
- Which part is Python?
- Which part is agent decision-making?

Common mistake:

Writing that the LLM directly creates the test data from memory. That misses the purpose of MCP tool calling.
