# Prompt Engineering Cheatsheet

Use this for quick revision after reading the module.

## 1. Good prompt structure

Syntax:

```text
Role:
Task:
Context:
Constraints:
Examples:
Output format:
```

Meaning:

A clear prompt separates what the model should do, what information it should use, what rules it must follow, and what shape the output should have.

When to use:

Use for most AI Engineer prompts.

Example:

```text
Role: You are a QA analyst.
Task: Generate test cases.
Context: Requirement...
Output format: JSON...
```

Be careful:

A long prompt is not automatically a good prompt. It must be clear and non-conflicting.

## 2. Zero-shot

Meaning:

Task prompt with no examples.

When to use:

Use for simple tasks.

Example:

```text
Classify this ticket as bug, feature, or question. Return only the label.
```

Be careful:

For complex formats, examples may be needed.

## 3. One-shot

Meaning:

Prompt with one example before the real task.

When to use:

Use when one example clarifies style or format.

Example:

```text
Example: Requirement: Reset password. Title: Verify reset using registered email.
Now write a title for: User can login.
```

Be careful:

The example should match the desired output.

## 4. Few-shot

Meaning:

Prompt with multiple examples.

When to use:

Use for classification, extraction, or style imitation.

Example:

```text
Ticket: Login fails. Category: bug
Ticket: Add export. Category: feature
Ticket: How to reset? Category: question
```

Be careful:

Bad examples teach bad patterns.

## 5. Persona prompt

Meaning:

Prompt that gives the model a role.

When to use:

Use when domain focus matters.

Example:

```text
You are a senior QA analyst. Review the requirement for ambiguity.
```

Be careful:

Persona does not replace task, context, constraints, or output format.

## 6. Structured prompt

Meaning:

Prompt divided into labeled sections.

When to use:

Use for multi-part tasks.

Example:

```text
Task:
Context:
Rules:
Output:
```

Be careful:

Avoid mixing unrelated objectives in one prompt.

## 7. JSON output prompt

Meaning:

Prompt that asks the model to return valid JSON.

When to use:

Use when application code must parse the output.

Example:

```text
Return only valid JSON. Do not include markdown.
Use this schema: {"summary": "string"}
```

Be careful:

Still validate with JSON parsing and Pydantic.

## 8. Code-only prompt

Meaning:

Prompt that asks for only code with no explanation.

When to use:

Use when the code will be inserted into a file or tested directly.

Example:

```text
Return only Python code. Do not include markdown or explanation.
```

Be careful:

Do not also ask for line-by-line explanation in the same prompt.

## 9. Concise reasoning summary

Meaning:

User-facing explanation of why an answer was chosen.

When to use:

Use when you need explanation without hidden chain-of-thought.

Example:

```text
Provide the final answer and a concise reasoning summary in 2 bullets.
```

Be careful:

Do not rely on long reasoning text as proof of correctness.

## 10. RAG prompt

Meaning:

Prompt that includes retrieved context and tells the model to answer from it.

When to use:

Use for document-grounded answers.

Example:

```text
Use only the provided context. If insufficient, say you do not know from the context.
```

Be careful:

Separate context and question clearly.

## 11. Agent system prompt

Meaning:

Prompt that defines agent role, rules, tools, and boundaries.

When to use:

Use for LangGraph agents, MCP tool workflows, or multi-step assistants.

Example:

```text
Use tools only when needed. Do not invent source facts.
```

Be careful:

Explain when not to use tools.

## 12. Evaluation prompt

Meaning:

Prompt that checks whether an answer follows rules or schema.

When to use:

Use in review nodes, output validation, and POC quality checks.

Example:

```text
Mark pass only if required fields are present and facts are supported by context.
```

Be careful:

Define evaluation criteria. Do not ask only "Is this good?"

## 13. Common prompt mistakes

Avoid:

- vague task
- missing context
- no output format
- conflicting constraints
- asking for JSON plus prose
- not handling insufficient context
- relying on prompts without validation
- giving examples that do not match desired output
