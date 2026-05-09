# Prompt Engineering Exercises

Each exercise starts with a weak prompt. Improve it using instruction, context, constraints, examples, and output format.

## Exercise 1: Improve a zero-shot summarization prompt

### Task

Improve this bad prompt:

```text
Summarize this.
```

Requirement:

```text
Users can reset their password using a registered email. The reset link expires after 15 minutes.
```

### Expected improved prompt

```text
Summarize the requirement below in 3 concise bullets.
Focus on user action, system behavior, and test risk.

Requirement:
Users can reset their password using a registered email. The reset link expires after 15 minutes.
```

### Expected output style

```text
- User action: User resets password using registered email.
- System behavior: System sends a reset link that expires after 15 minutes.
- Test risk: Expired link behavior must be tested.
```

### Hint

Tell the model what kind of summary you want.

### Self-check

Does the improved prompt define length and focus?

### Solution outline

Add task, requirement context, bullet count, and focus areas.

### Common mistake

Asking for a summary without saying whether it should be short, detailed, technical, or test-focused.

## Exercise 2: Create a few-shot classification prompt

### Task

Improve this bad prompt:

```text
Classify the ticket.
```

Ticket:

```text
Dashboard chart does not load.
```

### Expected improved prompt

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

### Expected output style

```text
bug
```

### Hint

Few-shot means give examples before the real task.

### Self-check

Do the examples use the same output labels you expect?

### Common mistake

Giving examples in paragraph form but expecting a one-word label.

## Exercise 3: JSON test-case prompt

### Task

Improve this bad prompt:

```text
Make test cases for login in JSON.
```

Requirement:

```text
User can log in with email and password.
```

### Expected improved prompt

```text
You are a QA test designer.

Task:
Generate functional test cases for the requirement below.

Requirement:
User can log in with email and password.

Constraints:
- Include positive, negative, and edge cases.
- Do not include performance tests.

Output format:
Return only valid JSON.
Do not include markdown or explanation.
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
```

### Expected output style

Valid JSON only, no markdown fences.

### Hint

JSON prompting should define keys and tell the model not to include prose.

### Self-check

Could a Pydantic model validate the output shape?

### Common mistake

Writing "in JSON" but not defining the schema.

## Exercise 4: RAG prompt with refusal behavior

### Task

Improve this bad prompt:

```text
Answer the question.
```

Question:

```text
What is the account lockout rule?
```

Context:

```text
Users can log in with email and password.
```

### Expected improved prompt

```text
You are a grounded QA knowledge assistant.

Use only the provided context to answer the question.
If the context is insufficient, say:
"I do not know from the provided context."

Context:
Users can log in with email and password.

Question:
What is the account lockout rule?

Output format:
Return:
- Answer
- Source summary
- Missing information
```

### Expected output style

```text
Answer:
I do not know from the provided context.

Source summary:
The context only says users can log in with email and password.

Missing information:
Account lockout rule is not provided.
```

### Hint

RAG prompts must say what to do when context is insufficient.

### Self-check

Does the improved prompt prevent the model from inventing a lockout rule?

### Common mistake

Providing context but not instructing the model to stay inside it.

## Exercise 5: Agent system prompt

### Task

Improve this bad prompt:

```text
You are an agent. Use tools.
```

### Expected improved prompt

```text
You are a controlled QA assistant agent.

Responsibilities:
- Answer requirement questions using provided context.
- Generate test scenarios when asked.
- Use tools only when needed.
- Do not invent project facts.

Tool behavior:
- Use the test data tool only for demo test data lookup.
- Do not call tools for simple explanation questions.

If information is missing:
Ask for clarification or say what information is missing.

Response style:
Be concise and structured.
```

### Expected output style

The model should answer directly, call tools only when needed, and avoid unsupported facts.

### Hint

Agent prompts need responsibilities, tool rules, and boundaries.

### Self-check

Does the prompt explain when not to use tools?

### Common mistake

Giving tools to an agent without usage rules.

## Exercise 6: Evaluation prompt

### Task

Improve this bad prompt:

```text
Check if this answer is good.
```

### Expected improved prompt

```text
You are an evaluator.

Task:
Check whether the generated answer follows the required schema and uses only the provided context.

Required schema:
{schema}

Provided context:
{context}

Generated answer:
{answer}

Rules:
- Mark "pass" only if required fields are present.
- Mark "fail" if the answer includes unsupported facts.
- Mark "fail" if JSON is invalid.

Output format:
{
  "status": "pass|fail",
  "issues": ["string"],
  "concise_reasoning_summary": "string"
}
```

### Expected output style

Valid JSON with `status`, `issues`, and `concise_reasoning_summary`.

### Hint

Evaluation prompts need criteria.

### Self-check

Does the improved prompt define what "good" means?

### Common mistake

Asking for judgment without objective rules.

## Exercise 7: Code-only prompt

### Task

Improve this bad prompt:

```text
Write code for FastAPI and explain it.
```

### Expected improved prompt

```text
Return only Python code.
Do not include markdown.
Do not include explanation.

Task:
Create a FastAPI app with one GET endpoint at /health.
The endpoint should return {"status": "ok"}.
```

### Expected output style

Python code only.

### Hint

Do not ask for code-only and explanation at the same time.

### Self-check

Would markdown fences break a direct code insertion workflow?

### Common mistake

Mixing code output and teaching output in one prompt.
