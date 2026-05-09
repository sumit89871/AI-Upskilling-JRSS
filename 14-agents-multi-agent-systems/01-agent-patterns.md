# Agent Patterns

## Tool-using agent

What it is:

An agent that can call external tools when text generation alone is not enough.

Example:

```text
User asks for demo admin data -> agent calls get_test_user("admin") -> tool returns approved test data
```

Common mistake:

Letting the model invent data instead of calling a controlled tool.

## Planner agent

What it is:

An agent that breaks a task into steps.

Example:

```text
Plan: analyze requirement, retrieve context, generate tests, review output
```

Common mistake:

Using a planner for tiny tasks that do not need planning.

## Executor agent

What it is:

An agent or worker that performs a planned step.

Example:

Generate API test cases after the planner identifies API coverage as needed.

Common mistake:

Mixing planning and execution so the workflow is hard to debug.

## Reviewer agent

What it is:

An agent that checks output quality against rules.

Example:

Check whether generated test cases include title, type, priority, steps, and expected result.

Common mistake:

Asking "is this good?" without objective criteria.

## Supervisor pattern

What it is:

A controller decides which specialist agent should act next.

Mental model:

```text
Supervisor -> requirement analyst -> test generator -> reviewer
```

Use when:

Different workers have different responsibilities.

Do not use when:

A fixed linear workflow is enough.

## Agent memory

What it is:

Information stored for future steps or future sessions.

Compare:

```text
state = data during current workflow
memory = stored information reused later
```

Common mistake:

Assuming the model remembers everything automatically.

## Framework awareness

AutoGen, CrewAI, PydanticAI, and LlamaIndex agents are frameworks or libraries that help build agent workflows.

Beginner rule:

Learn the agent pattern first. Framework syntax comes later.
