# 07 Pydantic

## 1. What This Module Is

This module teaches Pydantic from beginner level.

Pydantic is a Python library that validates data using classes and type hints.

Simple meaning:

```text
Pydantic = a data shape checker for Python applications
```

It helps your app answer questions like:

- Did the input contain the required fields?
- Is `age` really an integer?
- Is `prompt` empty?
- Is `test_cases` a list of structured test case objects?
- Can this data safely go into FastAPI, an LLM call, a RAG response, or an agent workflow?

## 2. Why It Matters

AI and API applications pass a lot of structured data:

- FastAPI request bodies
- FastAPI response bodies
- LLM messages
- structured GenAI output
- RAG answers with sources
- MCP tool input and output
- LangGraph agent state
- final POC response contracts

If this data shape is wrong, the app may fail later in a confusing place.

Pydantic helps the app fail early with a clear validation error.

## 3. What The Learner Should Finish Knowing

After this module, you should understand:

- `BaseModel`
- model classes
- class fields
- type hints
- required fields
- optional fields
- default values
- nested models
- list of objects
- validation errors
- `model_validate`
- `model_dump`
- Pydantic model vs Python dictionary
- Pydantic with FastAPI
- Pydantic with GenAI structured output
- Pydantic with agent state

## 4. Study Order

1. Read `00-overview.md`.
2. Read `01-models-fields-validation.md`.
3. Read `02-nested-models-genai-state.md`.
4. Inspect and run the files in `practice/`.
5. Complete `exercises.md`.
6. Revise with `cheatsheet.md`.
7. Practice `interview-questions.md`.

## 5. File List

- `README.md`: this module guide.
- `00-overview.md`: beginner mental model for Pydantic, validation, `BaseModel`, fields, `model_validate`, and `model_dump`.
- `01-models-fields-validation.md`: deeper explanation of fields, type hints, defaults, optional fields, `Field`, and validation errors.
- `02-nested-models-genai-state.md`: nested models, list of objects, structured GenAI output, RAG answers, and agent state.
- `practice/user_model.py`: basic model validation example.
- `practice/prompt_request.py`: field rules, defaults, and validation error example.
- `practice/test_case_response.py`: nested model and list of objects example.
- `exercises.md`: hands-on validation practice with expected commands and outputs.
- `cheatsheet.md`: concise Pydantic syntax revision with caution notes.
- `interview-questions.md`: beginner, practical, scenario, and tricky Pydantic Q&A.

## 6. Practical Scope

This module focuses on Pydantic v2 style:

- `model_validate`
- `model_dump`
- `Field`
- Python `str | None` optional syntax
- Python `list[ModelName]` list-of-model syntax

The examples are intentionally local and small so the validation behavior is easy to see.

## 7. What Not To Over-Focus On

Do not start with advanced custom validators, serializers, generics, or complex configuration.

First become strong with:

- required fields
- optional fields
- default values
- nested models
- reading validation errors
- converting between dictionary and model object

## 8. How This Helps In AI Engineer JRSS / Mettl / POC / Interview

For JRSS labs, Pydantic appears in FastAPI request and response models.

For Mettl-style screening, you may see questions about type hints, required fields, defaults, and validation errors.

For the final POC, Pydantic keeps `/ask`, `/generate-test-cases`, RAG answers, MCP tool payloads, and LangGraph state predictable.

For interviews, Pydantic helps you explain how you prevent bad input from reaching an LLM, tool, retriever, or agent workflow.
