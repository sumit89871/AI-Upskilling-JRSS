# MCP Tools, Resources, and Prompts

## 1. What these are

MCP mainly gives an AI application three useful things from a server:

- **Tool**: an action the AI system can ask the server to perform.
- **Resource**: information the AI system can read from the server.
- **Prompt**: a reusable prompt template the AI system can request from the server.

These three words are easy to confuse because all of them are "provided by the MCP server." The difference is what they are used for.

A tool does work.

A resource gives data.

A prompt gives a reusable instruction template.

## 2. The most important beginner idea

An MCP tool is usually just a normal function made available to an AI client.

Example:

```python
def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}
```

By itself, this is only a Python function. It does not become an MCP tool automatically.

In a real FastMCP server, the developer exposes it with a decorator:

```python
@mcp.tool()
def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}
```

The important change is `@mcp.tool()`.

That decorator tells FastMCP:

- this function should be advertised as a tool
- the tool has an input named `role`
- `role` should be a string
- the result should be returned to the MCP client

## 3. Why these concepts matter

AI models are good at generating text, but they cannot safely do every real task by themselves.

For example, an AI model cannot magically:

- read your local project files
- fetch approved test data
- calculate using a trusted business rule
- query a controlled internal system
- call an enterprise-approved API

MCP gives a standard way to connect the AI application to those external abilities.

In AI Engineer work, this matters because enterprise systems need controlled integration. You do not want the model inventing data. You want the model to call approved tools and use approved resources.

## 4. Beginner mental model

```text
Tool:
AI wants an action -> calls MCP tool -> Python function runs -> result comes back

Resource:
AI wants known information -> reads MCP resource -> server returns data

Prompt:
AI wants a reusable instruction -> asks MCP server for prompt -> client uses prompt text
```

Another way to remember:

```text
Tool = do something
Resource = read something
Prompt = say something in a prepared format
```

## 5. Tool

### What a tool is

A tool is a callable operation exposed by an MCP server.

It usually maps to a function in code.

Example tool ideas:

- add two numbers
- fetch a test user
- search a local notes folder
- generate test data
- validate an API payload
- check whether a requirement has enough acceptance criteria

### Why tools exist

Tools exist because LLMs need help from real systems.

If a user asks:

```text
Give me test credentials for an admin user.
```

The model should not invent credentials. A safer design is:

```text
User asks -> agent chooses get_test_user tool -> tool returns approved demo data
```

### Small example

File:

`12-mcp-fastmcp/implementation/test_data_helper_server.py`

Code:

```python
def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}


def get_test_card(card_type: str) -> dict:
    return {"card_type": card_type, "number": "4111111111111111"}
```

### Syntax breakdown

`def get_test_user(role: str) -> dict:`

- `def` means "define a function"
- `get_test_user` is the function name
- `role` is the input parameter
- `: str` means `role` should be a string
- `-> dict` means the function is expected to return a dictionary
- `:` starts the indented function body

`return {"username": f"{role}_user", "password": "demo123"}`

- `return` sends a value back to the caller
- `{...}` creates a Python dictionary
- `"username"` and `"password"` are dictionary keys
- `f"{role}_user"` is an f-string
- if `role` is `"admin"`, `f"{role}_user"` becomes `"admin_user"`

### What the learner created manually

The developer manually creates:

- the Python file
- the function name
- the input parameter
- the return dictionary
- the business logic

### What FastMCP would provide automatically

In a real FastMCP server, FastMCP can help provide:

- tool registration
- tool discovery
- schema creation from type hints
- communication between client and server
- returning the tool result to the MCP client

FastMCP does not invent your business logic. You still write the function.

## 6. Resource

### What a resource is

A resource is information exposed by an MCP server for reading.

A resource is not mainly for doing an action. It is mainly for giving context or data.

Example resources:

- project requirements document
- API contract
- test strategy note
- coding standard
- glossary
- latest approved prompt template

### Beginner analogy

A resource is like a file, document, or database record that the AI system can read through a controlled interface.

### Example resource idea

```text
notes://login-requirements
```

This looks like a custom URI.

Syntax breakdown:

- `notes` is the resource scheme
- `://` separates the scheme from the resource name
- `login-requirements` is the resource identifier

This does not mean it is a website URL. It is a name the MCP server and client understand.

### Tool vs resource

| Concept | Main purpose | Example |
|---|---|---|
| Tool | Perform an action | `get_test_user("admin")` |
| Resource | Read information | `notes://login-requirements` |

If the AI needs to calculate, search, validate, or generate something using code, use a tool.

If the AI needs to read stable data or context, use a resource.

## 7. Prompt

### What a prompt is in MCP

An MCP prompt is a reusable prompt template provided by the server.

It helps keep prompt wording consistent across tools, agents, or applications.

Example:

```text
You are a QA assistant. Generate test scenarios for:
{requirement}
```

`{requirement}` is a placeholder. The application fills it with real text later.

### Why prompt templates exist

Prompt templates exist because real projects should not scatter important prompt text randomly across many files.

If every developer writes their own prompt, output quality becomes inconsistent.

With reusable prompts:

- the team can standardize wording
- prompts can be reviewed
- prompts can be versioned
- AI behavior becomes easier to explain in interviews and demos

## 8. Schema

### What schema means

A schema describes the shape of data.

For an MCP tool, the schema tells the client:

- what inputs the tool accepts
- input names
- input types
- which inputs are required
- what output shape may come back

For this function:

```python
def add(a: int, b: int) -> int:
    return a + b
```

The input schema is conceptually:

```json
{
  "a": "integer",
  "b": "integer"
}
```

The output is expected to be an integer.

### Schema vs JSON

Schema and JSON are not the same thing.

| Concept | Meaning |
|---|---|
| JSON | Actual data being sent |
| Schema | Description of what valid data should look like |

Example JSON data:

```json
{
  "a": 2,
  "b": 3
}
```

Example schema idea:

```text
a must be an integer
b must be an integer
```

Beginner mistake:

Thinking schema is the data itself. It is not. Schema is the rulebook for the data.

## 9. Tool input and tool output

Tool input is what the client sends to the tool.

Tool output is what the tool returns.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Input:

```json
{
  "a": 2,
  "b": 3
}
```

Output:

```json
5
```

In real AI agent work:

```text
Agent decides: I need calculation
Agent calls: add(a=2, b=3)
Tool returns: 5
Agent uses: "The answer is 5"
```

## 10. Decorator vs normal function

### Normal function

```python
def add(a: int, b: int) -> int:
    return a + b
```

This function can be called by Python code.

### Decorated function

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b
```

This function is still a Python function, but the decorator also registers it as an MCP tool.

Syntax breakdown:

- `@` means decorator syntax in Python
- `mcp` is the FastMCP server object
- `.tool()` means call the `tool` method on the `mcp` object
- the next function below the decorator is the function being registered

Common beginner confusion:

The decorator does not replace the function body. The function body still contains the actual logic.

## 11. Tool vs API endpoint

MCP tools and REST API endpoints can both perform actions, but they are used differently.

| Concept | Usually called by | Example |
|---|---|---|
| REST API endpoint | Web client, backend service, browser, curl | `POST /generate-test-cases` |
| MCP tool | AI client or agent through MCP protocol | `generate_test_cases(requirement)` |

REST APIs are usually designed for general application communication.

MCP tools are designed so AI clients can discover and call capabilities in a standard way.

In a final POC, you may use both:

- FastAPI exposes REST endpoints for the frontend
- MCP exposes tools for the agent workflow

## 12. How an agent uses a tool

At beginner level, the flow is:

```text
User asks a question
Agent checks available tools
Agent decides whether a tool is needed
Agent sends tool input
MCP server runs Python function
Tool result returns
Agent writes final response using result
```

Example:

User:

```text
Give me login test data for an admin user.
```

Agent may call:

```text
get_test_user(role="admin")
```

Tool returns:

```json
{
  "username": "admin_user",
  "password": "demo123"
}
```

Agent responds:

```text
Use admin_user / demo123 as demo admin login test data.
```

Important:

The model did not create the password from imagination. It used a controlled tool.

## 13. Common mistakes

### Mistake 1: Thinking MCP is the model

MCP is not the LLM. MCP is the connection layer that lets clients discover tools, resources, and prompts.

### Mistake 2: Thinking every function is automatically a tool

A normal Python function is not an MCP tool until the server exposes it.

### Mistake 3: Exposing unsafe tools

Do not expose tools that can delete files, leak secrets, or run arbitrary commands unless the design has strong controls.

### Mistake 4: Confusing resource and tool

If it reads data, it may be a resource. If it performs an operation, it is usually a tool.

### Mistake 5: Forgetting input types

Good type hints help tools become easier to understand and safer to call.

Bad:

```python
def get_user(x):
    return {}
```

Better:

```python
def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}
```

## 14. Quick practice

1. Write a normal Python function named `get_environment_url(env: str) -> dict`.
2. Return `{"env": env, "url": "https://demo.example.com"}`.
3. Identify the tool input.
4. Identify the tool output.
5. Write the conceptual schema in plain English.
6. Explain whether this should be a tool, resource, or prompt.

Expected answer:

- It is a tool if the agent calls it to look up an environment URL.
- Input is `env`.
- Output is a dictionary with `env` and `url`.
- Schema says `env` must be a string.

## 15. Where used in AI Engineer work

MCP tools, resources, and prompts appear in:

- final POC test data lookup
- AI QA assistant tool calling
- enterprise agent integrations
- local file notes assistant
- controlled access to approved business data
- agent workflows that need calculators, search helpers, validators, or API wrappers
- interview explanations about how an AI system safely uses external tools

For the AI Engineer JRSS course, MCP is important because it shows that you can build more than a chatbot. You can connect an AI workflow to real project capabilities in a controlled, explainable way.
