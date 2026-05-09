# LangGraph Exercises

These exercises use normal Python first. The goal is to make state, nodes, edges, and graph flow obvious before using the real LangGraph package.

## Exercise 1: Explain the core terms

### Task

Explain these terms in your own words:

- graph
- node
- edge
- state
- checkpoint

### Expected answer

- Graph: the full workflow map.
- Node: one workflow step.
- Edge: the connection from one node to the next.
- State: shared data passed through the workflow.
- Checkpoint: saved workflow progress.

### Hint

Use this mental model:

```text
State = shared notebook
Node = worker
Edge = arrow to next worker
Graph = full workflow map
Checkpoint = saved copy of notebook
```

### Self-check

Can you explain why state is more than a normal local variable?

### Solution outline

State must be available across workflow steps. A local variable inside one function disappears when that function ends.

### Common mistake

Saying "node is only a function." A node may be implemented as a function, but conceptually it is a workflow step.

## Exercise 2: Run the mock graph

### Task

Run the existing mock graph project.

Starting file:

```text
13-langgraph-stateful-agents/implementation/qa-agent-graph/graph_mock.py
```

### Expected command

```powershell
python graph_mock.py
```

### Where to run

Run it from:

```text
13-langgraph-stateful-agents/implementation/qa-agent-graph/
```

### Command explanation

- `python` runs the Python interpreter.
- `graph_mock.py` is the file Python should execute.

### Expected output

```text
{'analysis': 'Analyzed: User can login', 'scenarios': ['valid case', 'invalid case', 'boundary case'], 'api_tests': ['check 200 response', 'check 400 validation']}
```

### Hint

If Python cannot find the file, your terminal is probably in the wrong folder.

### Self-check

- Which node adds `analysis`?
- Which node adds `scenarios`?
- Which node adds `api_tests`?
- Which node creates `final`?

### Solution outline

1. Open terminal in the `qa-agent-graph` folder.
2. Run `python graph_mock.py`.
3. Match each output key to the node that created it.

### Common mistake

Expecting the output to show the full state. The current script prints `result["final"]`, not the full state.

## Exercise 3: Create state for a RAG answer workflow

### Task

Create a state dictionary for this flow:

```text
User question -> retrieve documents -> generate answer -> review answer -> final answer
```

### Expected code

```python
state = {
    "question": "What is the refund rule?",
    "retrieved_context": [],
    "draft_answer": None,
    "review_status": None,
    "final_answer": None,
}
```

### Expected output

No output is required unless you print the state.

If you print it:

```python
print(state)
```

Expected output:

```text
{'question': 'What is the refund rule?', 'retrieved_context': [], 'draft_answer': None, 'review_status': None, 'final_answer': None}
```

### Hint

Use `None` when a value will be filled later. Use `[]` when the value should be a list.

### Self-check

- Which node should fill `retrieved_context`?
- Which node should fill `draft_answer`?
- Which node should fill `review_status`?

### Solution outline

Create one key for each important piece of data that a later node needs.

### Common mistake

Using different names for the same idea, such as `context`, `retrieved_docs`, and `retrieved_context` randomly.

## Exercise 4: Write a node function

### Task

Write a node named `analyze_question` that reads `state["question"]`, writes `state["analysis"]`, and returns state.

### Expected code

```python
def analyze_question(state: dict) -> dict:
    state["analysis"] = f"Question analyzed: {state['question']}"
    return state
```

### Syntax explanation

- `def` creates a function.
- `analyze_question` is the node function name.
- `state: dict` means input should be a dictionary.
- `-> dict` means output should be a dictionary.
- `state["question"]` reads the question.
- `state["analysis"] = ...` writes a new value into state.
- `return state` sends the updated state to the next step.

### Expected output

If you test it with:

```python
state = {"question": "What is the refund rule?"}
print(analyze_question(state))
```

Expected output:

```text
{'question': 'What is the refund rule?', 'analysis': 'Question analyzed: What is the refund rule?'}
```

### Hint

Make sure the initial state contains the `question` key.

### Self-check

What error happens if `state["question"]` does not exist?

Expected answer:

```text
KeyError
```

### Common mistake

Forgetting `return state`, which means the next workflow step does not receive the updated dictionary.

## Exercise 5: Design a conditional edge

### Task

Design routing logic for this rule:

```text
if review_status is approved, go to final
otherwise, go to revise
```

### Expected logic

```python
def route_after_review(state: dict) -> str:
    if state["review_status"] == "approved":
        return "final"
    return "revise"
```

### Expected output

If:

```python
print(route_after_review({"review_status": "approved"}))
```

Expected output:

```text
final
```

If:

```python
print(route_after_review({"review_status": "needs_changes"}))
```

Expected output:

```text
revise
```

### Hint

A conditional edge usually returns the name of the next route.

### Self-check

Why should this function read from state instead of using a random global variable?

### Solution outline

The route decision should depend on workflow data. Workflow data should live in state.

### Common mistake

Returning the final answer instead of returning the next route name.

## Exercise 6: Add a review node to a workflow

### Task

Write a review node that checks whether scenarios exist.

### Expected code

```python
def review_output(state: dict) -> dict:
    if state["scenarios"]:
        state["review_status"] = "approved"
    else:
        state["review_status"] = "needs_changes"
    return state
```

### Expected output

Test:

```python
state = {"scenarios": ["valid case"]}
print(review_output(state))
```

Expected output:

```text
{'scenarios': ['valid case'], 'review_status': 'approved'}
```

### Hint

An empty list behaves like false in an `if` condition. A non-empty list behaves like true.

### Self-check

What should happen if `state["scenarios"]` is an empty list?

Expected answer:

`review_status` should become `"needs_changes"`.

### Common mistake

Checking the wrong key name, such as `state["scenario"]` instead of `state["scenarios"]`.

## Exercise 7: Explain checkpoint placement

### Task

Choose where checkpointing helps in this flow:

```text
retrieve context -> generate answer -> review answer
```

### Expected answer

Checkpoint after retrieving context.

### Explanation

Retrieval may be expensive or slow. If generation fails after retrieval, a checkpoint lets the workflow resume from the saved context instead of retrieving again.

### Hint

Checkpoint after expensive or important steps.

### Self-check

Would checkpointing after the final answer help retry generation?

Expected answer:

No. By then generation has already happened.

### Common mistake

Saying "checkpoint at every line." Too many checkpoints may add complexity without benefit.

## Exercise 8: Decide if LangGraph is needed

### Task

For each case, decide whether LangGraph is useful.

Cases:

1. One prompt that summarizes a sentence.
2. RAG workflow with retrieval, answer generation, review, and retry.
3. A script that prints "hello".
4. Multi-agent workflow with planner, executor, and reviewer.

### Expected answer

1. Probably not needed.
2. Useful.
3. Not needed.
4. Useful.

### Hint

Use LangGraph when workflow control matters.

### Self-check

Can you explain the cost of using a graph when a simple function is enough?

### Common mistake

Using LangGraph only because it sounds advanced. Good engineering chooses the simplest tool that fits the workflow.
