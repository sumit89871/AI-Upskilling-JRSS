# Agents and Multi-Agent Systems Overview

## What an AI agent is

An AI agent is a workflow that uses an LLM plus additional control logic to complete a task.

Simple meaning:

```text
LLM call = prompt in, answer out
Agent = model + state + tools + decisions + workflow
```

## Most important beginner idea

Every chatbot is not an agent.

A simple chatbot may only do:

```text
user prompt -> model response
```

An agent may do:

```text
user task -> decide plan -> call tool -> inspect result -> continue -> final answer
```

## Why agents exist

Agents exist because some tasks need more than text generation.

Example:

```text
Generate API test cases from requirement notes and approved test data.
```

This may require:

- reading context
- generating test ideas
- calling a test data tool
- reviewing output
- returning structured JSON

## Agent mental model

```text
Goal -> state -> model decision -> tool/workflow step -> updated state -> final answer
```

## LLM vs agent

| Concept | Meaning |
|---|---|
| LLM | Generates text from prompt |
| Agent | Uses model decisions inside a workflow |

Project example:

The final POC can use an LLM to generate tests. It becomes more agentic when it retrieves context, calls MCP-style tools, reviews output, and routes through LangGraph-style state.

## When not to use agents

Do not use an agent when:

- one deterministic function is enough
- one prompt call is enough
- the task has no decisions or tools
- reliability matters more than flexibility

Common mistake:

Using agents because they sound advanced.

## Where used in AI Engineer work

Agents appear in tool-using assistants, RAG workflows with review, LangGraph orchestration, MCP tool calling, and final POC architecture discussions.
