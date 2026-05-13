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

## A2A: agent-to-agent communication awareness

A2A means agent-to-agent communication.

Beginner meaning:

```text
One agent asks another agent for help, receives the result, and continues the workflow.
```

Simple mental model:

```text
Agent A has a task -> Agent A asks Agent B for specialized help -> Agent B returns result -> Agent A continues
```

Example in QA work:

```text
Requirement Analyst Agent -> asks API Test Agent for endpoint test ideas -> API Test Agent returns cases -> Reviewer Agent checks quality
```

Why A2A exists:

Large AI tasks can be easier to control when different agents have different responsibilities. One agent may be good at analysis, another at test generation, another at review, and another at tool usage.

A2A vs MCP:

| Concept | Beginner meaning |
|---|---|
| A2A | communication between agents |
| MCP | protocol for connecting AI systems to tools, resources, and prompts |

MCP is usually about tool access. A2A is about agent collaboration.

A2A vs supervisor pattern:

| Concept | Beginner meaning |
|---|---|
| Supervisor pattern | one controller decides which agent acts next |
| A2A | agents may communicate or hand off work to each other |

In a beginner POC, you do not need to build full A2A infrastructure. You should understand the concept and be able to explain it safely.

Common mistake:

Thinking A2A means every agent talks freely to every other agent. In real enterprise workflows, agent communication should be controlled, logged, and limited by clear responsibilities.

## Where used in AI Engineer work

Agents appear in tool-using assistants, RAG workflows with review, LangGraph orchestration, MCP tool calling, and final POC architecture discussions.

A2A appears in interview and architecture discussions when the system uses multiple specialized agents. For the final POC, you can describe A2A as a future extension:

```text
The current POC uses a controlled workflow. In a larger version, a requirement analyst agent, test case generator agent, API automation helper agent, and reviewer agent could communicate through an A2A-style pattern.
```
