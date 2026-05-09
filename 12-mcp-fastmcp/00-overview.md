# MCP Overview

## 1. What MCP is in plain English

MCP stands for Model Context Protocol.

Plain English:

```text
MCP is a standard way for AI clients to discover and use tools, resources, and prompts from external servers.
```

Do not treat this as a magic AI feature.

MCP is a connection pattern. It helps an AI application know:

- what tools are available
- what inputs each tool needs
- what output each tool returns
- what resources can be read
- what prompt templates can be reused

## 2. The most important beginner idea

MCP is not the model.

MCP is not the tool itself.

MCP is the protocol that connects AI clients to external capabilities.

Keep these separate:

```text
Model = reasons/generates text
Tool = function that does useful work
MCP server = exposes tools/resources/prompts
MCP client = discovers and calls what the server exposes
```

## 3. Why MCP exists

Without a standard, every AI app may connect to tools differently.

One app may call a Python function.

Another app may call an HTTP API.

Another app may use a plugin format.

Another app may use a custom agent framework.

MCP exists to create a common structure for tool/resource/prompt access.

Beginner analogy:

```text
MCP is like a common adapter plug between AI clients and useful external capabilities.
```

## 4. What problem MCP solves

LLMs can generate text, but they often need external help.

Examples:

- calculate exact values
- read approved local notes
- fetch test data
- query an internal system
- list available project resources
- reuse a standard prompt template

MCP helps expose those capabilities in a discoverable, structured, controlled way.

Problem without MCP-style structure:

```text
agent has no standard way to know what functions exist or how to call them
```

Better with MCP-style structure:

```text
server advertises tool name + description + schema
client discovers tool
agent calls tool with structured input
server returns structured output
```

## 5. Beginner mental model

Required mental model:

```text
Python function
  -> exposed as MCP tool
  -> MCP server advertises tool
  -> AI client discovers tool
  -> agent calls tool when needed
  -> tool returns result
```

Example:

```text
get_test_user(role)
  -> exposed as MCP tool
  -> server says "I have get_test_user"
  -> agent needs admin user
  -> client calls get_test_user({"role": "admin"})
  -> tool returns {"username": "admin_user", "password": "demo123"}
```

## 6. Model vs tool vs server vs client

### Model

The model generates or reasons over text.

Example:

```text
The LLM decides it needs test user data.
```

### Tool

A tool performs a specific operation.

Example:

```python
def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}
```

### MCP server

The MCP server exposes tools, resources, and prompts.

It is the provider side.

### MCP client

The MCP client connects to the server, discovers what is available, and calls tools/resources/prompts.

It is often part of the AI application or agent runtime.

## 7. MCP server

An MCP server is an application/process that offers capabilities to MCP clients.

It may expose:

- tools
- resources
- prompts

Beginner analogy:

```text
MCP server = service desk listing what help is available
```

Common mistake:

Thinking the server is the LLM. It is not. It exposes capabilities.

Where used in AI Engineer work:

Enterprise AI systems can run MCP servers for safe tool access.

## 8. MCP client

An MCP client connects to an MCP server.

It asks:

```text
What tools/resources/prompts do you expose?
```

Then it may call a selected tool.

Beginner analogy:

```text
MCP client = assistant that reads the service desk menu and requests an item
```

Common mistake:

Thinking the client is the same thing as the server. The client calls. The server exposes.

## 9. Tool

A tool is a callable operation.

It usually starts as a normal Python function.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Why it exists:

The model may need exact work done outside text generation.

Common mistake:

Exposing tools that are too powerful or unsafe.

Where used in AI Engineer work:

Test data lookup, calculators, approved file lookup, API helper functions.

## 10. Resource

A resource is readable context/data.

Example:

```text
notes://requirements/login
```

Simple meaning:

```text
read the login requirement note
```

Why it exists:

Sometimes the AI client needs context, not an action.

Common mistake:

Making read-only information into a tool that can perform unnecessary actions.

## 11. Prompt

A prompt is a reusable instruction template.

Example:

```text
Generate positive, negative, and edge test cases for:
{requirement}
```

Why it exists:

Prompts can be standardized and reused.

Common mistake:

Hardcoding many different prompt versions in random places.

## 12. FastMCP

FastMCP is a Python-friendly way to create MCP servers.

MCP is the concept/protocol.

FastMCP is a library/style that helps implement it in Python.

Comparison:

```text
MCP = protocol concept
FastMCP = Python tool for building MCP servers
```

Common mistake:

Saying FastMCP and MCP are the same thing. They are related but not identical.

## 13. How a normal Python function becomes an MCP tool

Normal function:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Conceptual FastMCP tool:

```python
from fastmcp import FastMCP

mcp = FastMCP("calculator")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b
```

Read it in this order:

```text
FastMCP -> mcp object -> @mcp.tool() -> function -> schema -> callable tool
```

Meaning:

- `from fastmcp import FastMCP` imports the FastMCP class.
- `mcp = FastMCP("calculator")` creates an MCP server object.
- `@mcp.tool()` is a decorator.
- The decorator registers the function below it as a tool.
- `def add(...)` is still a normal Python function.
- Type hints help describe the input and output schema.

## 14. Decorator vs normal function

Normal function:

```python
def add(a: int, b: int) -> int:
    return a + b
```

This can be called by Python code directly.

Decorated function:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b
```

The function still works like Python, but FastMCP also registers it as a tool.

Beginner memory:

```text
function = does the work
decorator = tells the framework to expose/register it
```

## 15. Tool input and output

Tool input:

```json
{"a": 2, "b": 3}
```

Tool output:

```json
5
```

Input means what the client sends.

Output means what the tool returns.

Common mistake:

Returning inconsistent shapes. Example: sometimes string, sometimes dictionary, sometimes list without clear reason.

## 16. How input/output schema is formed

Schema means the expected shape of data.

Python function:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Possible schema idea:

```text
Tool name: add
Inputs:
- a: integer
- b: integer
Output:
- integer
```

Where does this come from?

- function name gives tool name
- parameter names give input names
- type hints give input types
- return type hint gives output type

Schema vs JSON:

- schema describes the expected shape
- JSON is actual data sent or returned

Example schema says:

```text
a must be an integer
b must be an integer
```

Example JSON input is:

```json
{"a": 2, "b": 3}
```

## 17. How an AI agent discovers and calls tools

Beginner flow:

```text
agent has a goal
client asks MCP server for available tools
server lists tool names/descriptions/schemas
agent decides a tool is needed
client calls tool with structured input
server runs Python function
server returns result
agent uses result in final answer
```

Example:

```text
Goal: create test case with admin user
Tool discovered: get_test_user(role: str)
Tool call: {"role": "admin"}
Tool result: {"username": "admin_user", "password": "demo123"}
Agent response: use admin_user as demo test user
```

Important:

The model may suggest a tool call, but the client/server should still validate inputs and enforce safety.

## 18. Required comparisons

### MCP server vs MCP client

Server exposes capabilities.

Client discovers and calls capabilities.

### Tool vs resource

Tool performs work.

Resource provides readable context.

### Tool vs API endpoint

Tool is designed for AI-client tool use through MCP.

API endpoint is an HTTP route called through REST/HTTP.

They can call similar business logic, but they are exposed differently.

### FastMCP vs MCP concept

MCP is the protocol/concept.

FastMCP is a Python way to build MCP servers.

### Decorator vs normal function

Normal function performs work.

Decorator tells the framework to register/expose that function.

### Tool input vs tool output

Input is what client sends.

Output is what tool returns.

### Schema vs JSON

Schema describes expected shape.

JSON is actual structured data.

## 19. Where MCP fits in enterprise AI and final POC

Enterprise AI:

- controlled tool access
- governed resources
- reusable prompts
- auditability
- safer integration boundaries

Final POC:

```text
QA assistant needs test data
  -> agent/workflow calls MCP-style test data tool
  -> tool returns fake safe user/card data
  -> workflow uses result in generated test scenarios
```

This shows that the AI system can use controlled external capabilities instead of inventing everything.

## 20. Common mistakes

- Thinking MCP is the LLM.
- Thinking a tool is automatically safe because an AI calls it.
- Forgetting type hints.
- Returning inconsistent output shapes.
- Exposing file or shell access without restrictions.
- Confusing MCP server with FastAPI server.
- Confusing tool schema with actual JSON input.
- Using real passwords or real customer data in demo tools.
