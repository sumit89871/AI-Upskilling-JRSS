# Python For GenAI And Agentic AI Overview

## 1. What it is

Python for GenAI means using Python to connect normal application logic with AI models.

That includes:

- preparing prompts
- calling model APIs
- reading API keys from environment variables
- parsing model responses
- validating structured output
- retrying failed calls
- logging important events
- exposing tools
- maintaining workflow state

Agentic AI means the system does more than answer once. It can plan steps, call tools, update state, and continue until it reaches a final answer or a stop condition.

## 2. The most important beginner idea

The model does not replace application code.

The model predicts text. The developer still controls:

- what input reaches the model
- what context is provided
- what tools exist
- what response shape is accepted
- what happens when the model gives invalid output
- what happens when an API call fails
- when an agent loop should stop

Frameworks can automate some plumbing, but the developer still writes the important business logic.

## 3. Why it matters

Most AI Engineer projects are integration projects.

You are not only "chatting with a model". You are building a system:

```text
User input -> Python app -> prompt/context/tools -> model/client -> parsed result -> API/UI/workflow
```

If your Python layer is weak, the GenAI app becomes fragile:

- invalid JSON breaks downstream code
- missing API key crashes the app
- agent loop runs forever
- model response cannot be displayed in UI
- tool function returns data in the wrong shape

## 4. Beginner mental model

GenAI app:

```text
input -> prompt -> model call -> response -> parser -> validated output
```

Agentic app:

```text
goal -> state -> decide -> tool/action -> update state -> repeat or finish
```

Mock-first app:

```text
app logic -> mock LLM client -> predictable response
```

Real-provider app:

```text
app logic -> OpenAI/Gemini/Ollama client -> external model response
```

Start mock-first so you can build and test the app without paid API keys.

## 5. What the developer writes vs what frameworks provide

The developer usually writes:

- prompt templates
- API client wrapper
- fallback mock client
- retry rules
- state keys
- tool functions
- response parsing logic
- validation models

Frameworks may provide:

- automatic endpoint calling in FastAPI
- validation from Pydantic
- workflow execution in LangGraph
- tool registration in FastMCP
- model client SDK methods

Do not treat framework magic as magic. It usually calls Python functions or classes you created manually.

## 6. Mock-first pattern

File name: `mock_llm_client.py`

Exact folder path: `03-python-for-genai-agentic-ai/implementation/mock_llm_client.py`

Full code:

```python
class MockLLMClient:
    def generate(self, prompt: str) -> str:
        return f"Mock response for: {prompt}"


if __name__ == "__main__":
    client = MockLLMClient()
    answer = client.generate("Explain RAG simply")
    print(answer)
```

Syntax breakdown:

- `class MockLLMClient:` creates a class.
- `MockLLMClient` is the class name.
- `def generate(self, prompt: str) -> str:` creates a method.
- `self` means the current object.
- `prompt: str` says the parameter should be text.
- `-> str` says the method should return text.
- `return f"Mock response for: {prompt}"` returns an f-string.
- `{prompt}` inserts the prompt value into the string.
- `if __name__ == "__main__":` runs the block only when this file is executed directly.

What you created manually:

- the class
- the `generate` method
- the test call inside the main block

What Python gives automatically:

- object creation when you call `MockLLMClient()`
- method calling through `client.generate(...)`

Run from the module folder:

```powershell
python .\implementation\mock_llm_client.py
```

Command explanation:

- `python` runs Python.
- `.\implementation\mock_llm_client.py` points to the file.
- `.` means current folder.

Expected output:

```text
Mock response for: Explain RAG simply
```

How to verify:

If you see the prompt text inside the mock response, the class and method call worked.

## 7. Similar concepts beginners confuse

### LLM vs app

The LLM generates text.

The app validates input, calls the model, handles errors, stores state, and returns results.

### Tool vs model

A tool is usually a normal function that performs an action or returns data.

A model decides what text to generate and may request a tool if the agent framework supports tool use.

### State vs memory

State is the current workflow data.

Memory usually means longer-term information saved across sessions or conversations.

### Mock client vs real client

Mock client returns predictable fake output.

Real client calls OpenAI, Gemini, Ollama, or another model provider.

## 8. Common mistakes

- Calling a model before validating input.
- Assuming every model response is valid JSON.
- Hardcoding API keys in Python files.
- Forgetting fallback behavior when no API key exists.
- Making an agent loop without a max step count.
- Treating tools as magic instead of normal functions.
- Logging secrets by accident.

## 9. Where used in AI Engineer work

- OpenAI/Gemini API wrappers
- RAG answer generation
- FastAPI AI endpoints
- LangGraph nodes and state
- MCP tools
- multi-agent orchestration
- POC demo mock mode
- interview explanation of system design

For Mettl-style screening, expect questions around dictionaries, JSON parsing, function calls, error handling, environment variables, and output prediction.
