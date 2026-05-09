# MCP Cheatsheet

## MCP

Meaning: Protocol for connecting AI clients to tools, resources, and prompts.

Use when: Agents need controlled external capabilities.

Example: test data lookup tool.

Be careful: MCP is not the model.

## MCP Tool

Syntax: `@mcp.tool()`

Meaning: Expose a function as a callable tool.

Use when: AI client needs to perform an action.

Example: `get_test_user(role: str)`.

Be careful: Tool logic is still written by developer.

## Resource

Meaning: Readable context exposed by server.

Use when: Client needs documents or notes.

Example: `notes://login-requirements`.

Be careful: Resource reads data; tool performs action.

## Server vs Client

Meaning: Server exposes capabilities; client discovers and calls them.

Use when: Explaining MCP architecture.

Be careful: Do not reverse responsibilities.
