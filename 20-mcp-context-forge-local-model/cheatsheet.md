# MCP Context Forge Cheatsheet

## Tool Registry

Meaning: Catalog of available tools and their schemas.

Use when: AI clients need discoverable approved tools.

Example: `get_test_user(role: str) -> dict`

Be careful: Registry does not replace tool safety checks.

## Context System

Meaning: Managed source of approved context.

Use when: AI answers must use controlled information.

Example: approved requirement notes.

Be careful: Bad context still causes bad answers.

## Local Model + MCP

Meaning: Local model workflow can call MCP tools through a client layer.

Use when: Building privacy-aware or offline-style labs.

Example: Ollama-like local model plus test data MCP server.

Be careful: Tool calling is orchestrated by the app/client, not magic.
