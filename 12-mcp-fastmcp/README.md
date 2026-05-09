# 12 MCP And FastMCP

## 1. What this module is

This module teaches Model Context Protocol, usually shortened to MCP, and the beginner idea behind FastMCP-style Python tool servers.

Plain English:

```text
MCP is a standard way for AI applications to discover and use external tools, resources, and prompt templates.
```

FastMCP is a Python-friendly way to build MCP servers.

This module starts with normal Python functions first. Then it explains how those functions can be exposed as MCP tools.

## 2. Why it matters

An LLM can generate text, but it cannot safely do every useful action by itself.

An AI assistant may need to:

- calculate something
- look up fake test users
- read approved notes
- fetch safe project context
- call an internal helper
- use a reusable prompt template

MCP gives a consistent pattern for exposing those capabilities to AI clients.

## 3. What the learner should finish knowing

After this module, the learner should understand:

- what MCP is
- why MCP exists
- model vs tool vs server vs client
- MCP server
- MCP client
- tool
- resource
- prompt
- FastMCP
- decorator
- schema
- tool input
- tool output
- how a normal Python function becomes an MCP tool
- how an AI agent discovers and calls tools
- safety concerns
- how this fits into enterprise AI and the final POC

## 4. Study order

1. `00-overview.md`
2. `01-tools-resources-prompts.md`
3. `implementation/README.md`
4. `exercises.md`
5. `cheatsheet.md`
6. `interview-questions.md`

## 5. File list

- `README.md`: module guide.
- `00-overview.md`: MCP mental model, server/client/tool flow, FastMCP decorator basics.
- `01-tools-resources-prompts.md`: tool vs resource vs prompt, input/output, schema, and safety.
- `implementation/README.md`: explains the conceptual Python examples.
- `implementation/calculator_server.py`: calculator-style tool functions.
- `implementation/file_notes_server.py`: local note reader with safety checks.
- `implementation/test_data_helper_server.py`: QA test data helper functions.
- `exercises.md`: hands-on MCP design and safety exercises.
- `cheatsheet.md`: practical MCP/FastMCP revision.
- `interview-questions.md`: beginner, scenario, and tricky MCP Q&A.

## 6. Practical scope

This module uses beginner-safe Python examples first.

The implementation files are conceptual MCP-style examples. They show function shapes and safety thinking before adding a real MCP runtime.

In other words:

```text
normal Python function first -> MCP/FastMCP exposure later
```

## 7. What not to over-focus on

Do not start by memorizing protocol internals.

First understand:

- a tool is usually a normal function
- a resource is readable context
- a prompt is a reusable instruction template
- a server exposes capabilities
- a client discovers and calls them
- schema describes inputs and outputs
- safety matters because tools can do real work

## 8. How this helps in AI Engineer JRSS / Mettl / POC / interview

- JRSS labs: MCP is relevant to tool-using AI systems.
- Mettl: conceptual questions may test server/client/tool/resource differences.
- POC: final project can use MCP-style test data lookup.
- Interview: you can explain how an agent gets controlled access to external functions.
