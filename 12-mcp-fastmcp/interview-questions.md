# MCP and FastMCP Interview Questions

Use these answers for AI Engineer JRSS screening, POC explanation, and interview discussion. Practice giving the short answer first, then expand with a project example.

## 1. What is MCP?

Short answer:

MCP, or Model Context Protocol, is a standard way for AI clients to discover and use tools, resources, and prompts from external servers.

Expanded answer:

An LLM alone can generate text, but it cannot safely access every real system by itself. MCP provides a structured connection layer. An MCP server exposes capabilities such as tools, resources, and prompts. An MCP client connects to that server and can use those capabilities inside an AI application or agent workflow.

Project example:

In an AI QA assistant POC, an MCP server can expose a `get_test_user` tool. The agent can call that tool when it needs approved demo login data.

Common wrong answer:

"MCP is an AI model."

Why this is wrong:

MCP is not the model. It is a protocol for connecting AI clients to external capabilities.

## 2. Why does MCP exist?

Short answer:

MCP exists to give AI systems a standard, controlled way to use external tools and context.

Expanded answer:

Without MCP, every tool integration may be custom. One app may call tools one way, another app may call them differently, and the same capability becomes hard to reuse. MCP standardizes how tools, resources, and prompts are exposed and discovered.

Project example:

Instead of hardcoding test data logic directly inside every agent, an MCP server can expose `get_test_user`, `get_test_card`, and `read_note` as reusable capabilities.

Common wrong answer:

"MCP is only needed for chatbots."

Why this is wrong:

MCP is useful in any AI application that needs tools or context, including agents, IDE assistants, QA helpers, and enterprise copilots.

## 3. What is an MCP server?

Short answer:

An MCP server is a program that exposes tools, resources, and prompts to MCP clients.

Expanded answer:

The server owns the capabilities. It may expose a Python function as a tool, a document as a resource, or a reusable prompt template. The client connects to the server and asks what is available.

Project example:

A `qa-helper-tools` MCP server can expose tools like `get_test_user(role)` and `validate_api_response(payload)`.

Common wrong answer:

"The MCP server is the frontend."

Why this is wrong:

The frontend may call your backend, but an MCP server specifically exposes AI-usable capabilities over MCP.

## 4. What is an MCP client?

Short answer:

An MCP client is the application that connects to an MCP server and uses its tools, resources, or prompts.

Expanded answer:

The client does not own the tools. It discovers them from the server. In an agent system, the client may sit inside the AI application and call tools when the model decides they are needed.

Project example:

A LangGraph QA agent can act as the AI workflow, while an MCP client layer calls the external test data server.

Common wrong answer:

"The MCP client is the tool."

Why this is wrong:

The client calls the tool. The tool is exposed by the server.

## 5. What is an MCP tool?

Short answer:

An MCP tool is an action exposed by an MCP server that an AI client or agent can call.

Expanded answer:

A tool usually maps to a function. It accepts input, runs logic, and returns output. The function may calculate, search, validate, fetch test data, or call another service.

Project example:

```python
def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}
```

This function could become an MCP tool that returns demo login data.

Common wrong answer:

"A tool is just any file in the project."

Why this is wrong:

A tool is a callable capability, not just a file. A file may contain tool functions, but the function must be exposed by the MCP server.

## 6. What is the difference between a tool and a resource?

Short answer:

A tool performs an action. A resource provides readable information.

Expanded answer:

Use a tool when logic must run, such as fetching test data, calculating a value, or validating a payload. Use a resource when the AI client needs to read stable data, such as a requirement document or project note.

Project example:

`get_test_user("admin")` is a tool because it performs a lookup. `notes://login-requirements` is a resource because it represents readable requirement content.

Common wrong answer:

"Tool and resource are the same because both come from the MCP server."

Why this is wrong:

They may both come from the server, but their purpose is different.

## 7. What is an MCP prompt?

Short answer:

An MCP prompt is a reusable prompt template exposed by an MCP server.

Expanded answer:

Prompt templates help standardize instructions. Instead of every developer writing a different prompt for test case generation, the server can expose a reviewed prompt template.

Project example:

```text
Generate positive, negative, and edge test scenarios for:
{requirement}
```

The application fills `{requirement}` with real requirement text.

Common wrong answer:

"A prompt is the final model response."

Why this is wrong:

A prompt is input or instruction for the model. The final response is generated after the model processes the prompt.

## 8. What is FastMCP?

Short answer:

FastMCP is a Python-friendly way to build MCP servers more easily.

Expanded answer:

MCP is the protocol concept. FastMCP is a framework or library that helps Python developers create MCP servers and expose functions as tools with less boilerplate.

Project example:

```python
from fastmcp import FastMCP

mcp = FastMCP("qa-helper-tools")


@mcp.tool()
def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}
```

Common wrong answer:

"FastMCP and MCP are exactly the same."

Why this is wrong:

MCP is the standard. FastMCP is a Python tool for implementing MCP servers.

## 9. What does `@mcp.tool()` do?

Short answer:

`@mcp.tool()` registers the function below it as an MCP tool.

Expanded answer:

In Python, `@...` syntax is a decorator. A decorator can add behavior to a function. In FastMCP, `@mcp.tool()` tells the MCP server to expose the next function as a tool that clients can discover and call.

Project example:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b
```

Here, the function still performs the addition. The decorator exposes it as a tool.

Common wrong answer:

"The decorator contains the business logic."

Why this is wrong:

The business logic is inside the function body. The decorator registers the function.

## 10. How does a normal Python function become an MCP tool?

Short answer:

The developer writes the function and exposes it through the MCP server, usually with a FastMCP decorator.

Expanded answer:

First, you write a normal function with clear inputs, type hints, and return value. Then you register it with the MCP server. FastMCP can use the function signature to understand the tool name, input fields, and expected output type.

Project example:

Normal function:

```python
def add(a: int, b: int) -> int:
    return a + b
```

FastMCP tool:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b
```

Common wrong answer:

"Any Python function automatically becomes an MCP tool."

Why this is wrong:

A function must be exposed by the MCP server before clients can discover and call it.

## 11. What is a schema in MCP tool calling?

Short answer:

A schema describes the expected shape of tool input and output.

Expanded answer:

If a tool accepts `role: str`, the schema tells the client that the tool needs a field named `role` and the value should be a string. This helps the AI client call the tool correctly.

Project example:

For:

```python
def get_test_user(role: str) -> dict:
```

The input schema concept is:

```text
role must be a string
```

Common wrong answer:

"Schema is the same as JSON."

Why this is wrong:

JSON is actual data. Schema describes what valid data should look like.

## 12. What is the difference between tool input and tool output?

Short answer:

Tool input is what the client sends to the tool. Tool output is what the tool returns.

Expanded answer:

For `get_test_user(role: str)`, the input might be `role="admin"`. The output might be a dictionary containing a username and password. The agent uses the output to answer the user.

Project example:

Input:

```json
{
  "role": "admin"
}
```

Output:

```json
{
  "username": "admin_user",
  "password": "demo123"
}
```

Common wrong answer:

"The function name is the input."

Why this is wrong:

The function name identifies the tool. The input is the data passed into the function parameters.

## 13. How does an AI agent use an MCP tool?

Short answer:

The agent decides a tool is needed, sends input through the MCP client, receives the tool result, and uses that result in the final answer.

Expanded answer:

The model may reason that it needs external data. The client layer calls the MCP server. The server runs the tool function. The result comes back. The agent then uses the result instead of inventing the answer.

Project example:

User asks:

```text
Give me test data for a guest user.
```

Agent calls:

```text
get_test_user(role="guest")
```

Tool returns:

```json
{
  "username": "guest_user",
  "password": "demo123"
}
```

Common wrong answer:

"The model directly accesses the Python function by itself."

Why this is wrong:

The model does not directly run local Python functions. The application and MCP client/server integration handle tool calls.

## 14. What is the difference between an MCP tool and a REST API endpoint?

Short answer:

A REST API endpoint is usually called over HTTP by apps or services. An MCP tool is exposed for AI clients through MCP.

Expanded answer:

Both can run backend logic, but they are designed for different integration styles. REST APIs are general web interfaces. MCP tools are designed for AI tool discovery and invocation.

Project example:

FastAPI endpoint:

```text
POST /generate-test-cases
```

MCP tool:

```text
generate_test_cases(requirement)
```

In a POC, the Streamlit frontend may call FastAPI, while the agent inside FastAPI may call MCP tools.

Common wrong answer:

"MCP replaces all APIs."

Why this is wrong:

MCP and REST APIs can work together. MCP does not remove the need for normal application APIs.

## 15. What are common MCP security concerns?

Short answer:

Do not expose unsafe tools, secrets, private files, or destructive actions without strong controls.

Expanded answer:

An MCP tool is powerful because an AI workflow can call it. That means tool design must be careful. A tool that reads files should restrict paths. A tool that calls APIs should protect tokens. A tool that changes data should require approval or validation.

Project example:

The beginner `read_note` function blocks absolute paths to reduce accidental unsafe file access.

Common wrong answer:

"Security is not important because it is only a demo."

Why this is wrong:

POC demos are often evaluated for production thinking. You should show that secrets, file access, and tool permissions are controlled.

## 16. How would you explain MCP in your final POC?

Short answer:

In my POC, MCP is used to expose controlled helper functions as tools that the AI workflow can call when needed.

Expanded answer:

The final POC has a QA assistant that can answer questions and generate test cases. Some capabilities should be controlled, such as test data lookup or reading approved notes. Instead of letting the model invent those details, I expose helper functions through MCP-style tools. The agent can call those tools and include the returned result in its response.

Project example:

```text
User asks for login test data
LangGraph workflow decides a tool is needed
MCP tool get_test_user runs
Tool returns approved demo data
Final answer includes that data
```

Common wrong answer:

"I used MCP because it is a trending framework."

Why this is wrong:

Interviewers expect a practical reason. The better reason is controlled tool integration for AI applications.
