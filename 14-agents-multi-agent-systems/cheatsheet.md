# Agents Cheatsheet

## Agent

Meaning: Model-powered workflow with state, tools, or decisions.

Use when: Task needs multiple steps or external actions.

Example: QA assistant retrieves context, calls tool, reviews output.

Be careful: Not every chatbot is an agent.

## Tool-Using Agent

Meaning: Agent calls controlled functions/tools.

Use when: Model needs real data or action.

Example: MCP test data lookup.

Be careful: Do not let model invent tool results.

## Supervisor

Meaning: Routes work to specialist agents.

Use when: Multiple workers have different responsibilities.

Example: analyst -> generator -> reviewer.

Be careful: Avoid supervisor for simple one-step tasks.

## Memory vs State

Meaning: State is current workflow data; memory persists beyond a step or session.

Use when: Explaining agent architecture.

Be careful: Model does not automatically remember private project facts.
