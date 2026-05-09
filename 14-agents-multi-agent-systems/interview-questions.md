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
