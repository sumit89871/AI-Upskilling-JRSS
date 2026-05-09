# MCP and FastMCP Cheatsheet

This cheatsheet is for revision after reading the MCP notes. It is concise, but each entry still explains what the syntax means and when to use it.

## 1. MCP

Syntax / term:

```text
MCP
```

Meaning:

Model Context Protocol. A standard way for AI clients to discover and use tools, resources, and prompts from servers.

When to use:

Use MCP when an AI application needs controlled access to external capabilities.

Example:

```text
AI QA agent calls a test data helper tool through MCP.
```

Be careful:

MCP is not the LLM. MCP is the connection layer around tools, resources, and prompts.

## 2. MCP server

Syntax / term:

```text
MCP server
```

Meaning:

A program that exposes tools, resources, and prompts.

When to use:

Use an MCP server when you want to provide capabilities to an AI client in a standard way.

Example:

```text
qa-helper-server exposes get_test_user and read_note.
```

Be careful:

The server does not automatically know your business logic. You write the functions.

## 3. MCP client

Syntax / term:

```text
MCP client
```

Meaning:

The application that connects to an MCP server and calls its tools or reads its resources.

When to use:

Use an MCP client inside an AI application, agent workflow, or developer tool that needs MCP capabilities.

Example:

```text
LangGraph agent connects to an MCP server to call get_test_user.
```

Be careful:

The client calls tools. The server provides tools.

## 4. Tool

Syntax / term:

```text
tool
```

Meaning:

An action exposed by an MCP server.

When to use:

Use a tool when the AI system needs to do something, such as calculate, validate, search, or fetch test data.

Example:

```python
def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}
```

Be careful:

A normal Python function is not automatically an MCP tool. It must be exposed by the MCP server.

## 5. Resource

Syntax / term:

```text
resource
```

Meaning:

Readable information exposed by an MCP server.

When to use:

Use a resource for stable context or data, such as notes, requirements, or API documentation.

Example:

```text
notes://login-requirements
```

Be careful:

If logic must run, it is probably a tool, not a resource.

## 6. Prompt

Syntax / term:

```text
prompt
```

Meaning:

A reusable prompt template provided by the MCP server.

When to use:

Use prompts when multiple agents or apps should use consistent instructions.

Example:

```text
Generate test scenarios for: {requirement}
```

Be careful:

A prompt template is not the final answer. It is a reusable instruction pattern.

## 7. FastMCP server object

Syntax:

```python
mcp = FastMCP("qa-helper-tools")
```

Meaning:

Creates a FastMCP server object named `mcp`.

When to use:

Use this when creating a Python MCP server with FastMCP.

Example:

```python
from fastmcp import FastMCP

mcp = FastMCP("qa-helper-tools")
```

Be careful:

`mcp` is just a variable name. You could name it differently, but `mcp` is common and readable.

## 8. Tool decorator

Syntax:

```python
@mcp.tool()
```

Meaning:

Registers the function below it as an MCP tool.

When to use:

Place it directly above a function that you want the MCP client to discover and call.

Example:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b
```

Be careful:

The decorator exposes the function. The function body still contains the actual logic.

## 9. Function signature

Syntax:

```python
def add(a: int, b: int) -> int:
```

Meaning:

Defines a function named `add` that accepts two integers and returns an integer.

When to use:

Use clear function signatures for MCP tools so the schema is easy to understand.

Example:

```python
def get_test_user(role: str) -> dict:
```

Be careful:

Avoid unclear names like `def run(x):`. Tool names and parameters should explain their purpose.

## 10. Type hint

Syntax:

```python
role: str
```

Meaning:

The parameter `role` is expected to be a string.

When to use:

Use type hints so tool inputs are clearer and schemas can be generated more easily.

Example:

```python
def read_note(file_path: str) -> str:
```

Be careful:

Type hints describe expected types. They do not automatically make unsafe logic safe.

## 11. Return type hint

Syntax:

```python
-> dict
```

Meaning:

The function is expected to return a dictionary.

When to use:

Use return type hints to make tool output easier to understand.

Example:

```python
def get_test_card(card_type: str) -> dict:
```

Be careful:

The function should actually return the type you claim. Do not write `-> dict` and return plain text.

## 12. Tool input

Syntax / term:

```text
tool input
```

Meaning:

The data sent to the tool.

When to use:

Use inputs when the tool needs details to perform its work.

Example:

```json
{
  "role": "admin"
}
```

Be careful:

Input names should match the function parameter names.

## 13. Tool output

Syntax / term:

```text
tool output
```

Meaning:

The value returned by the tool.

When to use:

Use output as controlled data that the agent can include in its answer.

Example:

```json
{
  "username": "admin_user",
  "password": "demo123"
}
```

Be careful:

Do not return real secrets or private customer data from demo tools.

## 14. Schema

Syntax / term:

```text
schema
```

Meaning:

A description of the expected data shape.

When to use:

Use schema to explain valid tool inputs and outputs.

Example:

```text
role must be a string
return value must be a dictionary
```

Be careful:

Schema is not the same as JSON data. Schema describes valid data.

## 15. Run a Python file

Command:

```powershell
python calculator_server.py
```

Meaning:

Run the Python file named `calculator_server.py`.

When to use:

Use this when a file has direct test code under `if __name__ == "__main__":`.

Expected output:

```text
5
20
```

Be careful:

Run it from the folder where the file exists, or Python may not find it.

## 16. Run one imported function

Command:

```powershell
python -c "from test_data_helper_server import get_test_user; print(get_test_user('admin'))"
```

Meaning:

Run a short Python command from the terminal without creating a new file.

When to use:

Use it to test a function quickly.

Expected output:

```text
{'username': 'admin_user', 'password': 'demo123'}
```

Be careful:

Inside an import, write `test_data_helper_server`, not `test_data_helper_server.py`.

## 17. Agent tool-calling flow

Syntax / flow:

```text
User request -> agent selects tool -> MCP client calls server -> Python function runs -> result returns -> agent answers
```

Meaning:

The model does not do everything itself. It can use a controlled external function.

When to use:

Use this explanation in POC demos and interviews.

Example:

```text
User asks for admin test data -> agent calls get_test_user("admin") -> tool returns demo credentials
```

Be careful:

Do not say "MCP thinks." The model reasons. MCP connects the system to tools.
