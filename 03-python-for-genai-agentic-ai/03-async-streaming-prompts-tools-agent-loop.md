# Async, Streaming, Prompt Templates, Tools, And Agent Loops

## 1. What it is

`async` and `await` are Python features for waiting on slow operations without blocking everything.

Streaming means receiving output piece by piece instead of waiting for the full answer.

A prompt template is reusable prompt text with placeholders.

A tool is a normal function exposed to an AI system.

An agent loop repeats decision, action, and state update steps until the goal is reached or the loop stops.

## 2. The most important beginner idea

Tools are not magic. They usually start as normal Python functions.

Agent frameworks add structure around them:

```text
normal Python function -> tool schema -> model/agent can request tool -> framework calls function
```

The developer still writes the function and decides what it returns.

## 3. Why it matters

GenAI apps often wait for slow operations:

- model responses
- API calls
- database search
- file loading
- streaming token output

Agents also need:

- tool functions
- state
- stop conditions
- max step limits
- structured final output

Without these controls, an agent can become unreliable or run too long.

## 4. Beginner mental model

Prompt template:

```text
template + values -> final prompt
```

Tool:

```text
function name + inputs -> output
```

Agent loop:

```text
read state -> decide next action -> call tool or model -> update state -> stop or continue
```

Async:

```text
start slow operation -> wait without freezing everything -> continue when result is ready
```

## 5. Prompt template

```python
template = "Generate test cases for this requirement: {requirement}"
prompt = template.format(requirement="User can reset password")
print(prompt)
```

Syntax breakdown:

- `template` stores reusable text.
- `{requirement}` is a placeholder.
- `.format(...)` replaces placeholders with real values.
- `requirement="User can reset password"` passes the value by name.

Expected output:

```text
Generate test cases for this requirement: User can reset password
```

Prompt templates matter because production prompts should be consistent, not manually typed in many places.

## 6. Tool function

```python
def get_test_user(role):
    return {"username": f"{role}_user", "password": "demo123"}
```

Syntax breakdown:

- `def` creates a function.
- `get_test_user` is the function name.
- `role` is a parameter.
- The function returns a dictionary.
- `f"{role}_user"` inserts the role value into the username.

In MCP/FastMCP later, a decorator can expose this normal function as a tool.

Important safety note:

Examples may show simple test data. Real tools must not return real passwords or private data.

## 7. Async syntax

```python
async def generate_answer():
    return "answer"
```

Syntax breakdown:

- `async def` creates an asynchronous function.
- It returns a coroutine when called.
- It is normally awaited from another async function.

```python
answer = await generate_answer()
```

- `await` pauses until the async result is ready.
- `await` can only be used inside an async function.

Common beginner confusion:

`async` does not make CPU-heavy work magically faster. It helps with waiting on I/O operations such as network calls.

## 8. Small tool and state example

File name: `prompt_tool_loop.py`

Exact folder path: `03-python-for-genai-agentic-ai/practice/prompt_tool_loop.py`

Full code:

```python
def get_test_user(role):
    return {"username": f"{role}_user", "password": "demo123"}


def build_prompt(requirement, user):
    return (
        f"Generate test cases for: {requirement}. "
        f"Use test username {user['username']}."
    )


state = {
    "requirement": "Admin can approve requests",
    "tool_result": None,
    "final_prompt": None,
}

state["tool_result"] = get_test_user("admin")
state["final_prompt"] = build_prompt(state["requirement"], state["tool_result"])

print(state["final_prompt"])
```

What this file is for:

It shows how a tool result can be stored in state and then used to build a prompt.

Important lines:

- `get_test_user` is a normal Python function.
- `state` stores values across steps.
- `state["tool_result"] = ...` saves the tool output.
- `user['username']` reads a dictionary value inside an f-string.
- `build_prompt(...)` creates the final prompt from requirement and tool result.

Run from the module folder:

```powershell
python .\practice\prompt_tool_loop.py
```

Command explanation:

- `python` runs Python.
- `.\practice\prompt_tool_loop.py` points to the script.
- This script uses mock local data and does not need an API key.

Expected output:

```text
Generate test cases for: Admin can approve requests. Use test username admin_user.
```

How to verify:

Change `"admin"` to `"qa"` and rerun. The username should become `qa_user`.

## 9. Agent loop concept

A beginner-safe agent loop should always have a stop condition:

```python
max_steps = 3
step = 0

while step < max_steps:
    step = step + 1
    print(f"Running step {step}")
```

Syntax breakdown:

- `while step < max_steps:` keeps looping while the condition is true.
- `step = step + 1` increases the counter.
- `max_steps` prevents an infinite loop.

Expected output:

```text
Running step 1
Running step 2
Running step 3
```

Why this matters:

Real agents may call models and tools repeatedly. Always limit steps during learning and demos.

## 10. Similar concepts beginners confuse

### Tool vs API endpoint

A tool is a function exposed to an AI system.

An API endpoint is a URL exposed to HTTP clients.

They can call similar business logic, but they are exposed through different protocols.

### Prompt template vs final prompt

Template contains placeholders.

Final prompt has actual values filled in.

### Streaming vs normal response

Normal response returns all text at once.

Streaming returns chunks gradually.

### Agent loop vs function chain

A function chain follows a fixed sequence.

An agent loop may decide the next action based on state and model/tool output.

## 11. Common mistakes

- Thinking tools are special before frameworks register them.
- Forgetting frameworks need schemas to know tool inputs.
- Creating an agent loop with no max step count.
- Using unsafe code like `eval` in real tools.
- Using async without knowing what is being awaited.
- Streaming output but not handling partial chunks correctly.
- Putting secrets inside prompt templates.

## 12. Quick practice

Task:

- add a second tool named `get_test_account_status`
- store both tool results in state
- build one final prompt from both results

Self-check:

Can you explain which part is the tool, which part is state, and which part is the final prompt?

## 13. Where used in AI Engineer work

- streaming chat UI
- FastAPI async endpoints
- OpenAI/Gemini streaming APIs
- LangGraph nodes and conditional loops
- MCP tools
- agent planner/executor loops
- POC demo workflows
