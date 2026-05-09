# LangGraph Overview

## 1. What LangGraph is

LangGraph is a framework for building controlled, stateful workflows for LLM and agent applications.

Simple meaning:

```text
LangGraph helps you build AI workflows as a graph of steps.
```

In LangGraph, the workflow is not just random code. You define:

- what data is carried through the workflow
- what steps exist
- what each step does
- which step comes next
- when the workflow should branch
- when progress should be saved
- what final result should be returned

This is useful when an AI application has more than one step.

## 2. The most important beginner idea

LangGraph is not the LLM.

LangGraph is not the prompt.

LangGraph is not "an agent" by itself.

LangGraph is the workflow structure around AI calls, tools, retrieval, review, and decisions.

Beginner memory:

```text
LLM generates text.
LangGraph controls the workflow around that generation.
```

## 3. Why LangGraph exists

A simple function chain works when the flow is always the same.

Example:

```python
step1()
step2()
step3()
```

This is easy when:

- every step always runs
- the order never changes
- no retry is needed
- no human approval is needed
- no saved progress is needed

Agentic AI workflows are usually not that simple.

Example AI QA workflow:

```text
understand requirement
retrieve context
generate test scenarios
review output
if review failed, revise
if review passed, return final answer
```

Now the workflow needs state, decisions, routing, and sometimes checkpointing.

LangGraph exists to make this structure clear.

## 4. What problem LangGraph solves

Without a workflow structure, AI projects often become confusing:

- one function creates a value but another function cannot find it
- key names are inconsistent
- retry logic is scattered
- the workflow path is hidden inside many nested `if` statements
- debugging is hard because you cannot see what happened at each step
- human approval pauses are difficult to represent

LangGraph solves this by giving names to the workflow pieces:

- graph
- node
- edge
- state
- conditional edge
- checkpoint

## 5. Beginner mental model

Use this mental model throughout the module:

```text
State carries data -> node reads state -> node updates state -> edge decides next node -> graph continues -> final answer is returned
```

Another simple analogy:

```text
State = shared notebook
Node = worker who reads and writes in the notebook
Edge = arrow showing which worker gets the notebook next
Graph = full workflow map
Checkpoint = saved copy of the notebook
```

## 6. Graph as workflow

A graph is the full workflow map.

Example:

```text
analyze_requirement -> generate_scenarios -> generate_api_tests -> review -> final
```

This says:

- first run `analyze_requirement`
- then run `generate_scenarios`
- then run `generate_api_tests`
- then run `review`
- then return the final result

In real LangGraph, the graph is created using the LangGraph library. In this beginner module, the mock project uses normal Python to show the same idea.

## 7. Node as a function step

A node is one step in the workflow.

Most beginner LangGraph nodes are Python functions.

Example:

```python
def analyze_requirement(state: dict) -> dict:
    state["analysis"] = f"Analyzed: {state['requirement']}"
    return state
```

This node:

- receives `state`
- reads `state["requirement"]`
- adds `state["analysis"]`
- returns the updated state

### Node vs function

A node is often implemented as a function, but the meaning is slightly different.

| Concept | Meaning |
|---|---|
| Function | Python code that can be called |
| Node | A workflow step inside a graph |

The same Python function becomes a node when you register it in a graph workflow.

## 8. Edge as next-step connection

An edge connects one node to the next node.

Simple edge:

```text
analyze_requirement -> generate_scenarios
```

Meaning:

After `analyze_requirement` finishes, run `generate_scenarios`.

### Edge vs if condition

An edge is a workflow connection.

An `if` condition is Python decision logic.

A conditional edge uses decision logic to choose the next workflow connection.

Example:

```text
if review_status == "approved" -> final
else -> revise
```

## 9. State as shared data bag

State is the data that moves through the workflow.

Example:

```python
state = {
    "requirement": "User can login",
    "analysis": None,
    "scenarios": [],
    "api_tests": [],
    "review": None,
    "final": None,
}
```

Syntax breakdown:

- `{}` creates a Python dictionary
- `"requirement"` is a key
- `"User can login"` is the value for that key
- `None` means no value yet
- `[]` means an empty list
- commas separate dictionary items

### State vs variable

A normal variable may exist only inside one function.

State is shared across workflow steps.

Example:

```python
def analyze_requirement(state: dict) -> dict:
    local_note = "temporary"
    state["analysis"] = "done"
    return state
```

`local_note` disappears after the function ends.

`state["analysis"]` continues to the next node because it is stored in state.

## 10. Reducer basics

A reducer is a rule for combining state updates.

Beginner example:

If multiple nodes add messages, should the new messages replace the old messages or be appended?

Reducer mental model:

```text
old state value + new update -> combined state value
```

Example:

```text
old messages: ["analyzed"]
new messages: ["generated"]
combined messages: ["analyzed", "generated"]
```

You do not need advanced reducer logic on day one. Just understand that reducers control how updates are merged.

## 11. Conditional edge as decision

A conditional edge chooses the next node based on state.

Example:

```text
if state["review"] == "passed":
    go to final
else:
    go to revise
```

This matters because agent workflows often need review and retry.

Example:

```text
generate answer -> review answer
if answer is good -> final
if answer is weak -> generate again
```

## 12. Checkpoint as saved progress

A checkpoint is a saved copy of workflow progress.

Simple meaning:

```text
checkpoint = save the state so the workflow can resume or be inspected later
```

Why checkpointing matters:

- LLM calls may fail
- retrieval can be expensive
- human approval may pause the workflow
- long workflows need debugging
- you may want to inspect what each node produced

### Checkpoint vs normal memory

Normal memory may mean information stored for a conversation or user profile.

Checkpointing means saving the workflow state at a point in execution.

Example:

```text
checkpoint after retrieve_context
```

If generation fails later, the workflow may resume from the saved state instead of repeating retrieval.

## 13. Compile

In LangGraph, compile means preparing the graph definition so it can run.

Beginner meaning:

```text
compile = check and prepare the workflow map before execution
```

You define nodes and edges first. Then you compile the graph.

Conceptual example:

```python
app = graph.compile()
```

Syntax breakdown:

- `graph` is the graph builder object
- `.compile()` calls the compile method on that object
- `app` stores the runnable compiled graph

The mock project in this module does not use real `compile()` because it is a normal Python teaching example.

## 14. Invoke

Invoke means run the compiled graph with input.

Conceptual example:

```python
result = app.invoke({"requirement": "User can login"})
```

Syntax breakdown:

- `app` is the compiled graph
- `.invoke(...)` runs the graph
- `{...}` is the initial state
- `"requirement"` is a state key
- `"User can login"` is the starting value
- `result` stores the final state or output

Beginner meaning:

```text
invoke = start the workflow
```

## 15. Agent workflow vs normal script

A normal script usually runs top to bottom.

Example:

```text
line 1 -> line 2 -> line 3 -> finish
```

An agent workflow may need:

- tool calls
- retrieval
- branching
- retries
- review
- human approval
- saved state

LangGraph helps represent this as a workflow instead of scattered code.

## 16. Supervisor pattern basics

A supervisor pattern means one controller decides which worker or agent should handle the next task.

Example:

```text
Supervisor -> Requirement Analyst
Supervisor -> Test Scenario Generator
Supervisor -> Reviewer
```

Use supervisor patterns when different specialized agents or workers are needed.

Do not use a supervisor pattern for a tiny one-step task. It adds unnecessary complexity.

## 17. Full beginner code example

File:

```text
13-langgraph-stateful-agents/implementation/qa-agent-graph/graph_mock.py
```

Full code:

```python
def analyze_requirement(state: dict) -> dict:
    state["analysis"] = f"Analyzed: {state['requirement']}"
    return state


def generate_scenarios(state: dict) -> dict:
    state["scenarios"] = ["valid case", "invalid case", "boundary case"]
    return state


def generate_api_tests(state: dict) -> dict:
    state["api_tests"] = ["check 200 response", "check 400 validation"]
    return state


def review(state: dict) -> dict:
    state["review"] = "Mock review passed"
    state["final"] = {
        "analysis": state["analysis"],
        "scenarios": state["scenarios"],
        "api_tests": state["api_tests"],
    }
    return state


def run_graph(requirement: str) -> dict:
    state = {"requirement": requirement}
    for node in [analyze_requirement, generate_scenarios, generate_api_tests, review]:
        state = node(state)
    return state


if __name__ == "__main__":
    result = run_graph("User can login")
    print(result["final"])
```

## 18. How state moves through this code

Starting state:

```python
{"requirement": "User can login"}
```

After `analyze_requirement`:

```python
{
    "requirement": "User can login",
    "analysis": "Analyzed: User can login"
}
```

After `generate_scenarios`:

```python
{
    "requirement": "User can login",
    "analysis": "Analyzed: User can login",
    "scenarios": ["valid case", "invalid case", "boundary case"]
}
```

After `generate_api_tests`:

```python
{
    "requirement": "User can login",
    "analysis": "Analyzed: User can login",
    "scenarios": ["valid case", "invalid case", "boundary case"],
    "api_tests": ["check 200 response", "check 400 validation"]
}
```

After `review`:

```python
{
    "review": "Mock review passed",
    "final": {
        "analysis": "Analyzed: User can login",
        "scenarios": ["valid case", "invalid case", "boundary case"],
        "api_tests": ["check 200 response", "check 400 validation"]
    }
}
```

## 19. How to run the mock example

Command:

```powershell
python .\implementation\qa-agent-graph\graph_mock.py
```

Where to run:

Run this from:

```text
13-langgraph-stateful-agents/
```

What each part means:

- `python` runs the Python interpreter.
- `.\implementation\qa-agent-graph\graph_mock.py` is the path to the mock graph file.
- `.\` means "start from the current folder" in PowerShell.
- `implementation\qa-agent-graph` is the folder containing the example.
- `graph_mock.py` is the Python file to execute.

Expected output:

```text
{'analysis': 'Analyzed: User can login', 'scenarios': ['valid case', 'invalid case', 'boundary case'], 'api_tests': ['check 200 response', 'check 400 validation']}
```

How to verify it worked:

The output should include:

- `analysis`
- `scenarios`
- `api_tests`

Common error:

```text
python: can't open file
```

Meaning:

You are likely running the command from the wrong folder or the path is typed incorrectly.

## 20. What learner creates vs what LangGraph provides

Learner creates:

- state shape
- node functions
- edge order
- conditional routing rules
- final response format
- error handling decisions

LangGraph provides:

- graph builder
- node registration
- edge routing
- conditional edge support
- compiled runnable workflow
- invoke pattern
- checkpointing support

LangGraph does not decide your business workflow for you. You design the workflow.

## 21. Common mistakes

### Mistake 1: Treating state like a random dictionary

State should have clear key names. If one node writes `retrieved_context` and another reads `context`, the workflow breaks.

### Mistake 2: Forgetting to return state

If a node updates state but does not return it, the next step may not receive the update.

### Mistake 3: Using LangGraph for everything

If your task is one simple model call, a graph may be unnecessary.

### Mistake 4: Confusing checkpoint with final output

A checkpoint is saved progress. Final output is what the user receives.

### Mistake 5: Building loops without stop conditions

Retry loops need limits. Otherwise the workflow may run forever.

## 22. Where LangGraph fits in the final POC

The final POC can use LangGraph for:

```text
understand query -> retrieve local context -> generate answer/test cases -> review response -> return final structured output
```

Example:

- state stores the user query
- retrieve node stores relevant chunks
- generate node creates draft answer
- review node checks whether the answer uses context
- final node returns structured output to FastAPI

This gives a clear story for demos and interviews:

```text
The POC does not call an LLM randomly. It uses a controlled graph workflow with state, routing, and review.
```
