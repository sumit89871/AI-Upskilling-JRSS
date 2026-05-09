# Mini Project: Mock Agentic Test Case Planner

## Project Goal

Build a small mock agent workflow that takes a requirement and produces a structured test case planning response.

The project should not use a real LLM yet. Use mock responses so the workflow is predictable.

## Project Structure

```text
mini-project/
  README.md
  agent_state.py
  tools.py
  mock_llm.py
  planner.py
  main.py
  test_planner.py
  requirements.txt
  .env.example
```

## File Explanation

- `agent_state.py`: creates the initial state dictionary.
- `tools.py`: stores normal Python functions that act like tools.
- `mock_llm.py`: returns mock LLM-style text or dictionaries.
- `planner.py`: controls the workflow steps.
- `main.py`: runs the project locally.
- `test_planner.py`: verifies the workflow.
- `requirements.txt`: package list.
- `.env.example`: safe placeholder configuration.

## Setup Steps

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pytest python-dotenv
pip freeze > requirements.txt
```

Command breakdown:

- `python -m venv .venv` creates the local environment.
- `.\.venv\Scripts\Activate.ps1` activates it on Windows PowerShell.
- `pip install pytest python-dotenv` installs testing and `.env` helpers.
- `pip freeze > requirements.txt` saves dependency versions.

## Workflow

```text
Requirement received
State initialized
Test user tool called
Mock LLM generates draft
Reviewer step checks structure
Final structured output returned
```

## Expected Output Shape

```python
{
    "requirement": "User can reset password",
    "test_cases": [
        {
            "title": "Valid reset password request",
            "priority": "P1",
            "expected_result": "Password reset link is sent"
        }
    ],
    "steps": ["initialized", "tool_called", "draft_generated", "reviewed"]
}
```

## Common Errors

- Missing stop condition in loop.
- Tool returns a string but planner expects a dictionary.
- State key spelling mismatch.
- Test asserts a field that is never created.

## How This Connects To AI Engineer Work

This mini project prepares you for LangGraph, MCP, and final POC work. The same concepts appear later with real frameworks:

- state
- tools
- planner workflow
- validation
- final response shape

