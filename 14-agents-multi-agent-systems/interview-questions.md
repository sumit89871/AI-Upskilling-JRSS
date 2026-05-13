# Agents Interview Questions

## What is an AI agent?

Short answer:

An AI agent is a workflow that uses a model with state, tools, and decisions to complete a task.

Expanded explanation:

Unlike a simple LLM call, an agent may retrieve context, decide whether to call a tool, update state, review output, and continue.

Real project example:

A QA assistant agent can retrieve requirement context, call a test data tool, generate test cases, and review the result.

Common wrong answer:

"Every chatbot is an agent."

When to say this in interview:

Use when asked about agentic AI basics.

## When should you not use agents?

Short answer:

Do not use agents when a simple function or one prompt call is enough.

Expanded explanation:

Agents add cost, latency, complexity, and debugging challenges. Use them only when decisions, tools, state, or multi-step workflows are needed.

Real project example:

A `/health` endpoint should not use an agent.

Common wrong answer:

"Agents should be used for every AI task."

When to say this in interview:

Use when discussing engineering tradeoffs.

## What is the supervisor pattern?

Short answer:

A supervisor routes work to specialist agents or workers.

Expanded explanation:

It is useful when different agents have different responsibilities such as planning, execution, and review.

Real project example:

A supervisor routes a requirement to analyst, test generator, and reviewer workers.

Common wrong answer:

"Supervisor does all work itself."

When to say this in interview:

Use when asked about multi-agent systems.

## Question: What is A2A in agentic AI?

Short answer:

A2A means agent-to-agent communication, where one agent can ask another agent for help or hand off part of a task.

Expanded answer:

In a multi-agent system, different agents may have different responsibilities. For example, one agent analyzes a requirement, another generates test cases, and another reviews quality. A2A describes the communication or handoff between those agents. The important beginner idea is that A2A should be controlled and traceable, not random uncontrolled chatting between agents.

Project example:

In the final QA assistant POC, a future version could let a Requirement Analyst Agent hand off API-related work to an API Test Agent, then send the result to a Reviewer Agent.

Common wrong answer:

"A2A is the same as MCP."

Why wrong:

MCP connects AI systems to tools, resources, and prompts. A2A is about communication between agents.

When to say this in interview:

Use this when asked about multi-agent systems, agent handoff, enterprise agent collaboration, or terms from the reskilling PPT.

## Question: What is the difference between supervisor pattern and A2A?

Short answer:

Supervisor pattern uses one controller to route work. A2A focuses on agents communicating or handing work to each other.

Expanded answer:

A supervisor pattern is easier to debug because one component decides which agent acts next. A2A can be more flexible, but it needs stronger control, logging, and responsibility boundaries. For beginner POCs, supervisor-style orchestration is usually simpler and safer to explain.

Project example:

The POC can use a LangGraph-style supervisor flow: understand query, retrieve context, generate answer, review response. A later enterprise version could add A2A between specialist agents.

Common wrong answer:

"Supervisor and A2A are identical because both use multiple agents."

When to say this in interview:

Use this when explaining why your POC uses a controlled workflow instead of fully autonomous multi-agent communication.
