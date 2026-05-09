# MCP Context Forge Exercises

## Exercise 1: Draw the architecture

Task:

Write the local model plus MCP flow.

Expected answer:

```text
User -> AI client -> local/mock model -> MCP client -> MCP server -> tool result -> final response
```

Hint:

Separate model from tool server.

Self-check:

Which component exposes the tool?

Common mistake:

Saying the model itself stores all tools.

## Exercise 2: Tool registry thinking

Task:

Describe a registry entry for `get_test_user`.

Expected answer:

- name: `get_test_user`
- input: `role: str`
- output: username and password demo data
- purpose: approved demo test user lookup

Common mistake:

Not describing input/output shape.

## Exercise 3: Identify limitations

Task:

List three local model lab limitations.

Expected answer:

- slower on laptop
- tool calling needs orchestration
- unsafe tools need controls

Common mistake:

Assuming local automatically means production-ready.
