# Local Lab Architecture

## Goal

Design a beginner-friendly local architecture that combines a local model idea with MCP-style tools.

## Architecture

```text
User prompt
  -> AI client application
  -> local model or mock model
  -> MCP client layer
  -> MCP server tools
  -> tool result
  -> final response
```

## Components

AI client application:

Coordinates prompt, model call, and tool calls.

Local model:

Runs on your machine or local server. Example runtime could be Ollama.

MCP client:

Discovers and calls tools exposed by the MCP server.

MCP server:

Exposes Python functions as tools, resources, or prompts.

Tool registry/context catalog:

Keeps track of available tools and context.

## Example use case

User asks:

```text
Give me demo admin test data.
```

Flow:

```text
client receives request -> decides test data tool is needed -> calls get_test_user("admin") -> returns demo credentials -> model formats final answer
```

## Troubleshooting

If tool is not found:

Check server is running and tool name is registered.

If local model is slow:

Use a smaller model or mock mode.

If output invents facts:

Use stronger grounding and tool results.
