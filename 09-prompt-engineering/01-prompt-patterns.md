# Prompt Patterns

## 1. What prompt patterns are

Prompt patterns are reusable ways to instruct a model.

Simple meaning:

```text
prompt pattern = a repeatable prompt structure for a common task
```

Patterns help you avoid rewriting prompts from zero every time.

They also make prompts easier to test, compare, and improve.

## 2. Zero-shot prompting

Zero-shot prompting means giving the model a task without examples.

Use when:

- the task is simple
- the output format is easy
- examples are not necessary

Bad prompt:

```text
Classify this.
Login fails with 500.
```

Improved prompt:

```text
Classify the ticket below as one of: bug, feature, question.
Return only the category.

Ticket:
Login fails with 500 error.
```

Why improved prompt is better:

- defines allowed labels
- asks for only one category
- includes the ticket text clearly

Expected output shape:

```text
bug
```

Common mistake:

Using zero-shot for complex formats where examples would help.

Where used:

Simple classification, summarization, short extraction, Mettl-style concept prompts.

## 3. One-shot prompting

One-shot prompting means giving one example before the real task.

Use when:

- the model needs to copy a specific style
- one example is enough to clarify the format

Bad prompt:

```text
Write a test case title for login.
```

Improved prompt:

```text
Write a concise test case title.

Example:
Requirement: User can reset password.
Title: Verify password reset using registered email

Now write a title:
Requirement: User can log in with valid email and password.
Title:
```

Why improved prompt is better:

The example shows the expected title style.

Expected output shape:

```text
Verify login using valid email and password
```

Common mistake:

Giving an example in one style but expecting a different style in the output.

Where used:

Test title generation, classification labels, short structured outputs.

## 4. Few-shot prompting

Few-shot prompting means giving multiple examples before the real task.

Use when:

- the model must learn a pattern
- the task has subtle categories
- output consistency matters

Bad prompt:

```text
Classify these tickets.
```

Improved prompt:

```text
Classify each ticket as bug, feature, or question.
Return only the category.

Example 1:
Ticket: Login fails with 500 error.
Category: bug

Example 2:
Ticket: Add export to PDF option.
Category: feature

Example 3:
Ticket: How do I reset my password?
Category: question

Now classify:
Ticket: Dashboard chart does not load.
Category:
```

Why improved prompt is better:

- shows multiple label examples
- teaches category boundaries
- keeps output short

Expected output shape:

```text
bug
```

Common mistake:

Providing examples that are too different from the real task.

Where used:

Ticket classification, requirement risk classification, extraction patterns, evaluation prompts.

## 5. Persona-based prompting

Persona prompting gives the model a role.

Use when:

- you want domain-specific framing
- the task benefits from a viewpoint
- tone and focus matter

Bad prompt:

```text
Review this requirement.
```

Improved prompt:

```text
You are a senior QA analyst.
Review the requirement for ambiguity, missing acceptance criteria, and test risks.
Return concise bullets.

Requirement:
User can upload documents.
```

Why improved prompt is better:

The persona guides the review focus, but the task and output format still do the real control.

Expected output shape:

```text
- Ambiguity: supported file types are not specified.
- Missing rule: maximum file size is not defined.
- Test risk: error handling for failed upload is unclear.
```

Common mistake:

Using only persona and no task.

Bad:

```text
You are a senior QA analyst.
```

This does not tell the model what to do.

Where used:

Requirement analysis, test review, POC demo assistant role, agent system prompts.

## 6. Structured prompting

Structured prompting means organizing the prompt into clear sections.

Use when:

- the task has multiple parts
- output must follow a format
- context and instructions must be separated

Bad prompt:

```text
Generate tests for login and make it JSON and include all cases and keep it short.
```

Improved prompt:

```text
Role:
You are a QA analyst.

Task:
Generate functional test cases.

Context:
Requirement: User can log in with email and password.

Constraints:
- Include positive, negative, and edge cases.
- Do not include performance tests.

Output format:
Return a markdown table with columns: Title, Type, Priority, Expected Result.
```

Why improved prompt is better:

It separates role, task, context, constraints, and output format.

Expected output shape:

```text
| Title | Type | Priority | Expected Result |
|---|---|---|---|
| Valid login | Positive | P1 | Dashboard opens |
```

Common mistake:

Writing one long paragraph with mixed instructions that are hard to follow.

Where used:

Almost all practical AI Engineer prompts.

## 7. JSON output prompting

JSON prompting asks the model to return valid JSON.

Use when:

- application code must parse the result
- output will be validated by Pydantic
- FastAPI will return structured data

Bad prompt:

```text
Give me test cases in JSON.
```

Improved prompt:

```text
Return only valid JSON.
Do not include markdown.
Do not include explanation outside JSON.

Use this schema:
{
  "test_cases": [
    {
      "title": "string",
      "type": "positive|negative|edge",
      "priority": "P1|P2|P3",
      "steps": ["string"],
      "expected_result": "string"
    }
  ]
}

Requirement:
User can log in with email and password.
```

Why improved prompt is better:

- says JSON only
- blocks markdown wrappers
- gives exact keys
- gives allowed values

Expected output shape:

```json
{
  "test_cases": [
    {
      "title": "Valid login",
      "type": "positive",
      "priority": "P1",
      "steps": ["Open login page", "Enter valid credentials", "Click Login"],
      "expected_result": "Dashboard opens"
    }
  ]
}
```

Common mistake:

Trusting JSON prompting without validation. Use JSON parsing and Pydantic checks.

Where used:

FastAPI endpoints, mock LLM clients, Pydantic structured output, final POC.

## 8. Code-only prompting

Code-only prompting asks the model to return only code.

Use when:

- the output will be saved as code
- extra explanation would break copy/run flow
- the developer already knows where the code belongs

Bad prompt:

```text
Write Python code for a FastAPI health endpoint.
```

Improved prompt:

```text
Return only Python code.
Do not include markdown fences.
Do not include explanation.

Create a FastAPI app with one GET endpoint at /health.
The endpoint should return {"status": "ok"}.
```

Why improved prompt is better:

It prevents extra prose and markdown that may interfere with direct code use.

Expected output shape:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}
```

Common mistake:

Asking for code-only output but also asking "explain every line" in the same prompt.

Where used:

Code generation helpers, lab scaffolding, controlled developer tools.

## 9. Chain-of-thought concept and safe alternative

Chain-of-thought refers to detailed internal reasoning steps.

For practical applications, do not ask for hidden chain-of-thought. Ask for a concise reasoning summary.

Bad prompt:

```text
Show your full hidden chain of thought before answering.
```

Improved prompt:

```text
Provide the final answer.
Then provide a concise reasoning summary with 2-3 bullets.
```

Why improved prompt is better:

It gives useful user-facing explanation without relying on hidden reasoning.

Expected output shape:

```text
Final answer:
...

Concise reasoning summary:
- ...
- ...
```

Common mistake:

Thinking long reasoning text always means the answer is correct.

Where used:

Evaluation prompts, review nodes, interview-friendly model explanations.

## 10. Prompt pattern selection

Use this beginner decision guide:

- simple task: zero-shot
- format imitation: one-shot
- category or style learning: few-shot
- domain framing: persona
- parseable output: structured or JSON prompt
- grounded knowledge answer: RAG prompt
- tool-using workflow: agent system prompt
- answer checking: evaluation prompt

## 11. Where used in AI Engineer work

Prompt patterns appear in:

- OpenAI/Gemini API prompts
- RAG answer generation
- LangGraph generation nodes
- agent system prompts
- test case generation
- API test generation
- evaluation prompts
- POC demos
- interview explanations of output control
