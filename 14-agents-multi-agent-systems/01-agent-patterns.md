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

## Agent handoff

What it is:

Agent handoff means one agent passes work to another agent because the second agent is better suited for the next step.

Beginner example:

```text
Requirement Analyst Agent finds API behavior -> hands off to API Test Agent -> API Test Agent creates test cases
```

What is passed during handoff:

- current task
- relevant context
- constraints
- expected output format
- previous agent result

Common mistake:

Passing only a vague instruction such as "continue this." A useful handoff should include enough context for the next agent to act safely.

## A2A pattern

What it is:

A2A means agent-to-agent communication. It is a broader idea where agents exchange information or requests.

Beginner mental model:

```text
Agent A asks Agent B -> Agent B returns a structured result -> Agent A decides next step
```

Small QA example:

```text
Analyst Agent:
"I found three acceptance criteria. API Agent, generate endpoint coverage ideas."

API Agent:
"Here are positive, negative, and validation test ideas."

Reviewer Agent:
"Two cases lack expected results. Please fix them."
```

A2A vs supervisor:

In a supervisor pattern, one controller routes work. In A2A, agents may directly coordinate or exchange messages. For beginners, the safer first implementation is usually supervisor-controlled because it is easier to trace and debug.

A2A vs MCP:

MCP connects an AI system to tools and resources. A2A connects agents to other agents. A QA agent may use MCP to fetch test data and A2A to ask a reviewer agent for feedback.

Where it appears:

A2A may appear in reskilling material, architecture discussion, and enterprise agentic AI interviews. You do not need to overclaim a specific A2A implementation unless you built one.

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
