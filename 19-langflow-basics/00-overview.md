# Langflow Overview

## What Langflow is

Langflow is a visual tool for building AI workflows by connecting nodes.

Beginner meaning:

```text
Node = one component
Edge = connection between components
Flow = full AI pipeline
```

## Most important beginner idea

Langflow helps visualize workflows, but it does not remove the need to understand what each node does.

Example:

```text
Text input -> prompt node -> LLM node -> output
```

## Why visual flow builders exist

They make it easier to prototype and explain AI pipelines without writing every connection in code first.

They are useful for:

- quick demos
- stakeholder explanation
- prompt testing
- RAG flow visualization
- learning pipelines

## Limits

Langflow is useful for prototyping, but production systems often still need code for testing, security, deployment, logging, and custom business logic.
