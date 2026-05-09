# LangGraph Cheatsheet

Use this after studying the notes. It is short for revision, but each entry still explains meaning, usage, example, and caution.

## 1. LangGraph

Syntax / term:

```text
LangGraph
```

Meaning:

A framework for building controlled, stateful LLM and agent workflows.

When to use:

Use it when the workflow needs multiple steps, state, branching, retries, review, checkpointing, or human approval.

Example:

```text
understand query -> retrieve context -> generate answer -> review -> final
```

Be careful:

Do not use LangGraph for a one-line prompt call unless workflow control is actually needed.

## 2. Graph

Syntax / term:

```text
graph
```

Meaning:

The full workflow map.

When to use:

Use a graph to represent the whole flow from input to final output.

Example:

```text
analyze -> generate -> review -> final
```

Be careful:

The graph is the workflow structure. It is not the model itself.

## 3. Node

Syntax:

```python
def analyze(state: dict) -> dict:
    state["analysis"] = "done"
    return state
```

Meaning:

A node is one workflow step. It is often implemented as a Python function.

When to use:

Use a node for one clear responsibility, such as analyze, retrieve, generate, review, or finalize.

Be careful:

Always return updated state unless the node intentionally ends the workflow.

## 4. Edge

Syntax / flow:

```text
analyze -> generate
```

Meaning:

An edge connects one node to the next node.

When to use:

Use an edge to define workflow order.

Example:

```text
retrieve_context -> generate_answer
```

Be careful:

An edge is not the work itself. The node performs work. The edge decides where state goes next.

## 5. Conditional edge

Syntax / flow:

```text
if review_status == "approved" -> final
else -> revise
```

Meaning:

A conditional edge chooses the next node based on state.

When to use:

Use it when the workflow may branch.

Example:

```python
def route_after_review(state: dict) -> str:
    if state["review_status"] == "approved":
        return "final"
    return "revise"
```

Be careful:

The route should be based on clear state keys.

## 6. State

Syntax:

```python
state = {"query": "Generate tests", "steps": [], "final": None}
```

Meaning:

State is the shared data passed through the workflow.

When to use:

Use state for any data that later nodes need.

Example:

```python
state["retrieved_context"] = ["Login rule text"]
```

Be careful:

Use consistent key names. `context` and `retrieved_context` are different keys.

## 7. State update

Syntax:

```python
state["analysis"] = "Requirement analyzed"
```

Meaning:

Adds or replaces the `analysis` field in the state dictionary.

When to use:

Use this inside a node when the node produces information needed later.

Example:

```python
state["scenarios"] = ["valid login", "invalid password"]
```

Be careful:

Do not hide important workflow results only in local variables.

## 8. Reducer

Syntax / concept:

```text
old value + new update -> reducer -> merged value
```

Meaning:

A reducer decides how state updates are combined.

When to use:

Use reducers when multiple updates should be merged, such as appending messages instead of replacing them.

Example:

```text
["analyzed"] + ["generated"] -> ["analyzed", "generated"]
```

Be careful:

Beginners do not need advanced reducers immediately. First understand normal state updates.

## 9. Checkpoint

Syntax / term:

```text
checkpoint
```

Meaning:

Saved workflow state at a point in execution.

When to use:

Use checkpoints for long, expensive, retryable, or human-in-loop workflows.

Example:

```text
save state after retrieve_context
```

Be careful:

Checkpoint is not the same as final answer. It is saved progress.

## 10. Compile

Syntax:

```python
app = graph.compile()
```

Meaning:

Prepare the graph definition so it can run.

When to use:

Use after defining graph state, nodes, and edges in a real LangGraph project.

Example:

```text
define graph -> add nodes -> add edges -> compile
```

Be careful:

The mock project in this module does not use real `compile()` because it is normal Python.

## 11. Invoke

Syntax:

```python
result = app.invoke({"requirement": "User can login"})
```

Meaning:

Run the compiled graph with initial input state.

When to use:

Use it to start a real LangGraph workflow.

Example:

```python
result = app.invoke({"question": "What are login rules?"})
```

Be careful:

The input must match the state keys your nodes expect.

## 12. Retry node

Syntax / flow:

```text
generate failed -> retry_generate -> generate again
```

Meaning:

A retry path handles temporary failures.

When to use:

Use for timeouts, rate limits, or temporary API issues.

Example:

```text
retry LLM generation up to 2 times
```

Be careful:

Do not retry permanent errors forever.

## 13. Human approval node

Syntax / flow:

```text
generated answer -> human approval -> final
```

Meaning:

A workflow step where a human reviews before the graph continues.

When to use:

Use for sensitive or stakeholder-facing output.

Example:

```text
Review generated test cases before exporting them
```

Be careful:

Human approval adds safety but also slows the workflow.

## 14. Supervisor pattern

Syntax / flow:

```text
Supervisor -> analyst
Supervisor -> generator
Supervisor -> reviewer
```

Meaning:

A controller routes tasks to specialized workers or agents.

When to use:

Use when multiple specialized agents are needed.

Example:

```text
Supervisor chooses whether the requirement analyst or API test generator should run next
```

Be careful:

Do not add a supervisor for simple fixed-order workflows.

## 15. Run mock graph

Command:

```powershell
python graph_mock.py
```

Meaning:

Run the mock graph Python file.

When to use:

Use it from the `implementation/qa-agent-graph/` folder.

Expected output:

```text
{'analysis': 'Analyzed: User can login', 'scenarios': ['valid case', 'invalid case', 'boundary case'], 'api_tests': ['check 200 response', 'check 400 validation']}
```

Be careful:

If Python cannot open the file, check your current folder.
