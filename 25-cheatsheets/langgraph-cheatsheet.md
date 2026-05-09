# LangGraph Cheatsheet

## Mental Model

Syntax: `State -> node -> updated state -> edge -> next node`

Meaning: Controlled stateful workflow.

Use when: AI app needs multi-step orchestration.

Example: retrieve -> generate -> review -> final.

Be careful: Use simple functions when graph is unnecessary.

## State

Meaning: Shared data passed through nodes.

Use when: Later steps need earlier outputs.

Example: `{"query": "...", "context": [], "answer": None}`

Be careful: Keep key names consistent.

## Node

Meaning: One workflow step, often a function.

Use when: Step has one responsibility.

Example: `generate_answer(state)`.

Be careful: Return updated state.

## Conditional Edge

Meaning: Route based on state.

Use when: Review can pass or fail.

Example: approved -> final, failed -> revise.

Be careful: Avoid loops without stop condition.
