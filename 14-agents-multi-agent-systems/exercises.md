# Agents Exercises

## Exercise 1: LLM or agent?

Task:

Classify each case as simple LLM call or agent workflow.

Cases:

1. Summarize one paragraph.
2. Retrieve context, call test data tool, generate tests, review output.
3. Translate one sentence.

Expected answer:

1. Simple LLM call.
2. Agent workflow.
3. Simple LLM call.

Hint:

Look for tools, decisions, state, and multiple steps.

Self-check:

Can you explain why case 2 is agentic?

Common mistake:

Calling every LLM use an agent.

## Exercise 2: Design QA agent roles

Task:

Design roles for a multi-agent QA workflow.

Expected answer:

- Requirement Analyst: finds ambiguity and missing rules.
- Test Generator: creates test scenarios.
- API Test Helper: creates API checks.
- Reviewer: validates completeness and schema.

Solution outline:

Give each agent one responsibility.

Common mistake:

Making every agent do everything.

## Exercise 3: When not to use agents

Task:

Explain why a health check endpoint should not use an agent.

Expected answer:

A health check should return a deterministic response such as `{"status": "ok"}`. An agent would add unnecessary cost, latency, and failure risk.

Common mistake:

Using AI where simple code is better.
