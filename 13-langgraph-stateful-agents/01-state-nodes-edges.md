# State, Nodes, Edges, and Checkpointing

## 1. What these concepts are

LangGraph workflows are built from a few core ideas:

- **State**: the shared data that travels through the workflow.
- **Node**: one workflow step that reads and updates state.
- **Edge**: a connection that decides which node runs next.
- **Conditional edge**: an edge that chooses the next node based on state.
- **Reducer**: a rule for combining updates into state.
- **Checkpoint**: saved workflow progress.

These are not academic terms. They are practical building blocks for agent workflows.

## 2. The most important beginner idea

State is the center of the workflow.

Nodes should not guess what happened earlier. They should read from state.

Nodes should not hide important results in local variables. They should write important results back to state.

Beginner rule:

```text
If a later step needs it, store it in state.
```

## 3. Why state matters

Agent workflows fail when data movement is unclear.

Bad example:

```python
def retrieve_context(state: dict) -> dict:
    state["retrieved_context"] = "Login rules..."
    return state


def generate_answer(state: dict) -> dict:
    context = state["context"]
    state["answer"] = f"Answer using {context}"
    return state
```

Problem:

- `retrieve_context` writes `retrieved_context`
- `generate_answer` reads `context`
- the key names do not match

This causes a `KeyError`.

Better:

```python
def retrieve_context(state: dict) -> dict:
    state["context"] = "Login rules..."
    return state


def generate_answer(state: dict) -> dict:
    context = state["context"]
    state["answer"] = f"Answer using {context}"
    return state
```

## 4. Beginner mental model

```text
Initial state -> node reads state -> node writes update -> edge sends state to next node -> final state
```

Analogy:

```text
State = form being filled
Node = person filling one section
Edge = instruction for who gets the form next
Checkpoint = saved copy of the form
```

## 5. Designing state

State should describe what the workflow needs to remember.

Example state for a QA test generation workflow:

```python
state = {
    "requirement": "User can login",
    "analysis": None,
    "scenarios": [],
    "api_tests": [],
    "review_status": None,
    "final_answer": None,
}
```

Syntax breakdown:

- `state` is a variable name.
- `=` assigns a value to the variable.
- `{}` creates a dictionary.
- `"requirement"` is a key.
- `"User can login"` is a string value.
- `None` means no value has been added yet.
- `[]` means an empty list.
- commas separate dictionary entries.

What the developer creates manually:

- key names
- initial values
- expected state shape
- meaning of each field

What LangGraph provides:

- a way to pass and update state through the graph
- routing between nodes
- reducer and checkpoint support

## 6. State vs variable

A variable is a named value in code.

State is the shared workflow data passed between nodes.

Example:

```python
def analyze_requirement(state: dict) -> dict:
    temporary_note = "checking requirement"
    state["analysis"] = f"Analyzed: {state['requirement']}"
    return state
```

`temporary_note` is a local variable. It exists only inside this function.

`state["analysis"]` becomes part of the shared workflow state and can be used by later nodes.

Common beginner mistake:

Storing important workflow data in a local variable and expecting another node to see it.

## 7. Node

### What a node is

A node is one processing step in the graph.

In beginner LangGraph projects, a node is usually a Python function.

Example:

```python
def generate_scenarios(state: dict) -> dict:
    state["scenarios"] = ["valid login", "invalid password"]
    return state
```

### Syntax breakdown

`def generate_scenarios(state: dict) -> dict:`

- `def` means define a function.
- `generate_scenarios` is the function name.
- `state` is the input parameter.
- `: dict` means `state` should be a dictionary.
- `-> dict` means the function should return a dictionary.
- `:` starts the function body.

`state["scenarios"] = ["valid login", "invalid password"]`

- `state["scenarios"]` accesses the `scenarios` key in the dictionary.
- `=` assigns a new value.
- `[...]` creates a list.
- each string inside the list is one scenario.

`return state`

- sends the updated state back to the workflow.

### Node vs function

| Concept | Simple meaning |
|---|---|
| Function | A reusable block of Python code |
| Node | A workflow step in a graph |

A function becomes a node when the graph uses it as a workflow step.

## 8. Edge

### What an edge is

An edge connects one node to another.

Simple workflow:

```text
analyze_requirement -> generate_scenarios -> review
```

Meaning:

- after `analyze_requirement`, run `generate_scenarios`
- after `generate_scenarios`, run `review`

### Edge vs if condition

An edge is the route between steps.

An `if` condition is a decision in code.

A conditional edge uses a decision to choose the route.

## 9. Conditional edge

A conditional edge chooses the next node based on state.

Example:

```text
if state["review_status"] == "approved":
    go to final
else:
    go to revise
```

Practical flow:

```text
generate answer -> review answer -> approved? -> final
                                      -> not approved? -> revise
```

Why this matters:

AI output may need review. If the output is weak, the workflow should not return it immediately.

Common mistake:

Putting all routing logic inside one large node. That makes the graph hard to understand.

## 10. Reducer basics

A reducer controls how updates are combined into state.

This matters when multiple steps add to the same field.

Example:

```python
state = {"messages": ["Requirement analyzed"]}
new_update = {"messages": ["Test cases generated"]}
```

Should the new message replace the old list?

```python
["Test cases generated"]
```

Or should it append?

```python
["Requirement analyzed", "Test cases generated"]
```

A reducer defines that merge behavior.

Beginner mental model:

```text
old value + new update -> reducer -> final state value
```

In LangGraph, reducers are commonly useful for message lists and accumulated outputs.

## 11. Checkpointing

### What checkpointing is

Checkpointing saves workflow state during execution.

Simple meaning:

```text
checkpoint = saved progress
```

### Why it exists

AI workflows may be:

- long
- expensive
- interactive
- prone to API failures
- paused for human review

If the workflow fails after an expensive retrieval step, you may not want to start from zero.

### Example

Workflow:

```text
retrieve context -> generate answer -> review answer
```

Useful checkpoint:

```text
save state after retrieve context
```

If generation fails, the workflow can resume from the saved retrieved context.

### Checkpoint vs normal memory

| Concept | Meaning |
|---|---|
| Checkpoint | Saved workflow state at a point in execution |
| Memory | Often means user/session knowledge across conversations |

Do not confuse them. A checkpoint is about workflow progress.

## 12. Retry node

A retry node or retry route handles temporary failure.

Example:

```text
generate_answer failed due to timeout -> retry_generate -> generate_answer again
```

Use retries for:

- temporary API failure
- timeout
- rate limit after waiting
- flaky network issue

Do not use retries for:

- missing required input
- invalid API key
- broken code
- bad state key names

Common mistake:

Retrying forever without a limit.

Better:

```text
retry at most 2 or 3 times, then return a clear error
```

## 13. Human approval node

A human approval node pauses the workflow so a person can review.

Example:

```text
Generate test cases -> Human approval -> Final response
```

Use this when:

- output affects important decisions
- generated test cases will be shared with stakeholders
- production data or compliance is involved
- the AI recommendation needs human confirmation

In a beginner POC, you can explain this concept even if the demo uses a mock approval step.

## 14. Supervisor pattern

A supervisor pattern has one controller decide which specialized worker should act next.

Example:

```text
Supervisor
  -> Requirement Analyst
  -> RAG Retriever
  -> Test Case Generator
  -> Reviewer
```

Beginner explanation:

The supervisor does not do all work. It routes work to the right specialist.

When to use:

- multiple specialized agents exist
- the next step depends on task type
- workflow may branch to different workers

When not to use:

- simple one-step tasks
- small scripts
- flows where fixed order is enough

## 15. Graph workflow vs simple function chain

Simple function chain:

```python
state = analyze(state)
state = generate(state)
state = review(state)
```

Good for:

- fixed order
- no branching
- no checkpointing
- small workflows

Graph workflow:

```text
analyze -> generate -> review
                    -> if failed, revise
                    -> if passed, final
```

Good for:

- branching
- retries
- human approval
- long-running workflows
- state inspection
- agent orchestration

## 16. Agent workflow vs normal script

A normal script runs a planned sequence of code.

An agent workflow may decide actions based on state, tools, retrieval results, and review outcomes.

Example:

```text
normal script = always do A, B, C
agent workflow = do A, then decide whether B or C is needed
```

LangGraph makes that decision structure visible and testable.

## 17. Full mock example

File:

```text
13-langgraph-stateful-agents/implementation/qa-agent-graph/graph_mock.py
```

Code:

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

## 18. How the mock graph works

`run_graph("User can login")` creates the first state:

```python
{"requirement": "User can login"}
```

This line runs each node in order:

```python
for node in [analyze_requirement, generate_scenarios, generate_api_tests, review]:
    state = node(state)
```

Syntax breakdown:

- `for` starts a loop.
- `node` is a temporary variable that stores one function at a time.
- `[analyze_requirement, generate_scenarios, generate_api_tests, review]` is a list of functions.
- `state = node(state)` calls the current node function and stores the returned state.

This mock loop represents a simple graph with fixed edges.

## 19. How to run

Command:

```powershell
python .\implementation\qa-agent-graph\graph_mock.py
```

Where to run:

Run it from:

```text
13-langgraph-stateful-agents/
```

What each part means:

- `python` runs Python.
- `.\implementation\qa-agent-graph\graph_mock.py` points to the mock graph file.
- `.\` means the path starts from the current folder.

Expected output:

```text
{'analysis': 'Analyzed: User can login', 'scenarios': ['valid case', 'invalid case', 'boundary case'], 'api_tests': ['check 200 response', 'check 400 validation']}
```

How to verify:

Confirm the output contains:

- the analyzed requirement
- three scenario ideas
- two API test ideas

## 20. Common mistakes

### Mistake 1: Changing state key names randomly

If one node writes `api_tests` and another reads `api_test_cases`, the workflow can fail.

### Mistake 2: Not returning updated state

Every node should return state unless it is intentionally ending the workflow.

### Mistake 3: Creating loops without stop conditions

Retry logic must have limits.

### Mistake 4: Using graph when a function is enough

If the task has one step, do not add a graph just to sound advanced.

### Mistake 5: Confusing checkpoint with final answer

A checkpoint is saved progress. It is not necessarily what the user sees.

## 21. Quick practice

Design state for this flow:

```text
Question -> retrieve documents -> answer -> review
```

Expected state:

```python
state = {
    "question": "What are login password rules?",
    "retrieved_context": [],
    "draft_answer": None,
    "review_status": None,
    "final_answer": None,
}
```

Self-check:

- Which node writes `retrieved_context`?
- Which node writes `draft_answer`?
- Which node writes `review_status`?
- Which key should the final response read?

## 22. Where used in AI Engineer work

These concepts appear in:

- RAG workflows with answer review
- AI test case generation workflows
- tool-using agents
- human-in-loop approval flows
- retryable LLM calls
- final POC orchestration
- enterprise AI design discussions
- interview system design explanations
