# qa-agent-graph

## 1. Project goal

This project is a beginner mock of a LangGraph-style QA workflow.

It does not require the real LangGraph package yet. It uses normal Python functions so you can understand state, nodes, and edges before learning the framework API.

Workflow:

```text
User requirement -> Analyze requirement -> Generate scenarios -> Generate API test ideas -> Review -> Final output
```

Beginner mental model:

```text
state starts with requirement -> each node adds something -> final node returns structured output
```

## 2. Project structure

```text
13-langgraph-stateful-agents/implementation/qa-agent-graph/
  README.md
  graph_mock.py
  requirements.txt
```

File meaning:

- `README.md`: explains how the mock workflow works.
- `graph_mock.py`: contains the runnable Python workflow.
- `requirements.txt`: dependency file. It is empty because the mock version uses only built-in Python.

## 3. Why this project is not using real LangGraph yet

Real LangGraph introduces extra concepts such as graph builders, compile, invoke, state schemas, and checkpoint stores.

Those are useful, but beginners should first understand:

- what state is
- what a node does
- how state moves from node to node
- how final output is created

This mock project teaches the same workflow idea with fewer moving parts.

## 4. File: graph_mock.py

Folder path:

```text
13-langgraph-stateful-agents/implementation/qa-agent-graph/graph_mock.py
```

What this file is for:

This file simulates a simple graph using normal Python. Each function acts like a node. The `run_graph` function acts like the graph runner.

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

## 5. Line-by-line explanation

### `analyze_requirement`

```python
def analyze_requirement(state: dict) -> dict:
    state["analysis"] = f"Analyzed: {state['requirement']}"
    return state
```

Meaning:

- `def` creates a function.
- `analyze_requirement` is the function name.
- `state: dict` means the function expects a dictionary.
- `-> dict` means the function returns a dictionary.
- `state["requirement"]` reads the requirement from state.
- `state["analysis"] = ...` adds an analysis field to state.
- `return state` sends the updated state to the next step.

This function acts like a graph node.

### `generate_scenarios`

```python
def generate_scenarios(state: dict) -> dict:
    state["scenarios"] = ["valid case", "invalid case", "boundary case"]
    return state
```

Meaning:

- This node creates a list of test scenario types.
- `[]` creates a list.
- The list is stored under the `scenarios` key.

### `generate_api_tests`

```python
def generate_api_tests(state: dict) -> dict:
    state["api_tests"] = ["check 200 response", "check 400 validation"]
    return state
```

Meaning:

- This node creates API test ideas.
- `check 200 response` means verify success status.
- `check 400 validation` means verify validation failure behavior.

### `review`

```python
def review(state: dict) -> dict:
    state["review"] = "Mock review passed"
    state["final"] = {
        "analysis": state["analysis"],
        "scenarios": state["scenarios"],
        "api_tests": state["api_tests"],
    }
    return state
```

Meaning:

- This node adds a review result.
- It creates a final dictionary.
- The final dictionary contains selected values from state.
- The final output is stored under `state["final"]`.

### `run_graph`

```python
def run_graph(requirement: str) -> dict:
    state = {"requirement": requirement}
    for node in [analyze_requirement, generate_scenarios, generate_api_tests, review]:
        state = node(state)
    return state
```

Meaning:

- `requirement: str` means the input should be text.
- `state = {"requirement": requirement}` creates the starting state.
- `for node in [...]` loops through the node functions.
- `state = node(state)` runs the current node and stores the updated state.
- `return state` returns the final full state.

This is a mock replacement for a real graph runner.

### Direct run block

```python
if __name__ == "__main__":
    result = run_graph("User can login")
    print(result["final"])
```

Meaning:

- `if __name__ == "__main__":` runs only when this file is executed directly.
- `run_graph("User can login")` starts the workflow.
- `result` stores the returned state.
- `print(result["final"])` displays only the final output section.

## 6. What the learner creates manually

The learner manually creates:

- the state keys
- the node functions
- the order of nodes
- the final output shape
- the review logic

## 7. What LangGraph would provide in a real project

Real LangGraph would provide:

- graph builder object
- node registration
- edge registration
- conditional routing
- compile step
- invoke step
- checkpoint support
- cleaner graph execution model

This mock project uses a Python loop instead of real LangGraph edges.

## 8. How state moves through each node

Initial state:

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

After `review`, the state also contains:

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

## 9. How to run locally

Command:

```powershell
python graph_mock.py
```

Where to run:

Run this from:

```text
13-langgraph-stateful-agents/implementation/qa-agent-graph/
```

When to run:

Run it after opening this folder in your terminal and confirming `graph_mock.py` is present.

What each part means:

- `python` runs the Python interpreter.
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

Common beginner mistake:

Running `python graph_mock.py` from the parent module folder instead of this folder. If you do that, Python may not find the file.

## 10. Alternative run command from the module folder

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

- `python` runs Python.
- `.\` means start from the current folder.
- `implementation\qa-agent-graph\graph_mock.py` is the relative path to the file.

Expected output:

```text
{'analysis': 'Analyzed: User can login', 'scenarios': ['valid case', 'invalid case', 'boundary case'], 'api_tests': ['check 200 response', 'check 400 validation']}
```

## 11. Common errors

### Error: Python cannot open the file

Possible output:

```text
python: can't open file 'graph_mock.py'
```

Meaning:

The terminal is not in the folder where `graph_mock.py` exists.

Fix:

Either move into the implementation folder or use the full relative path.

### Error: KeyError

Possible output:

```text
KeyError: 'requirement'
```

Meaning:

Some node tried to read a state key that does not exist.

Fix:

Check the initial state and make sure the key names match across nodes.

### Error: No output

Meaning:

The direct run block may be missing or commented out.

Check for:

```python
if __name__ == "__main__":
```

## 12. How this connects to real LangGraph

In real LangGraph, the same concept becomes more formal:

```text
define state schema
create graph builder
add nodes
add edges
compile graph
invoke graph with input state
```

Conceptual real LangGraph flow:

```python
app = graph.compile()
result = app.invoke({"requirement": "User can login"})
```

The mock project teaches what happens inside that flow:

```text
state is created -> nodes run -> state is updated -> final output returns
```

## 13. How this connects to the final POC

The final AI QA Knowledge Assistant POC can use a graph workflow like:

```text
understand query -> retrieve context -> generate test cases -> review -> final response
```

This project is the small version of that idea.

In the POC:

- `requirement` may come from a user or uploaded file
- retrieval may come from local documents or vector DB
- generation may use mock LLM or real LLM
- review may check structure and missing context
- final output may be returned through FastAPI to Streamlit
