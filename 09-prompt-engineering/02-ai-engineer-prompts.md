# AI Engineer Prompt Examples

## 1. What these prompts are

These are practical prompt templates for common AI Engineer tasks.

They are not meant to be copied blindly. They show how to structure prompts for:

- requirement analysis
- test case generation
- API test generation
- summarization
- classification
- extraction
- RAG answers
- agent system behavior
- evaluation and review

## 2. Placeholder syntax

Many templates use placeholders:

```text
{requirement}
{context}
{question}
{api_spec}
```

Meaning:

- curly braces `{}` mark a value to fill later
- `requirement` is a placeholder name
- your Python code or app replaces the placeholder with real text

Python example:

```python
template = "Summarize this requirement: {requirement}"
prompt = template.format(requirement="User can login")
print(prompt)
```

Expected output:

```text
Summarize this requirement: User can login
```

Common mistake:

Forgetting to replace placeholders before sending the prompt to the model.

## 3. Requirement analysis prompt

Bad prompt:

```text
Analyze this requirement.
```

Improved prompt:

```text
You are a senior QA analyst.

Task:
Analyze the requirement for ambiguity, missing rules, assumptions, and test risks.

Requirement:
{requirement}

Output format:
Return concise bullets under these headings:
- Summary
- Ambiguities
- Missing Rules
- Test Risks
- Questions for Product Owner
```

Why improved prompt is better:

- sets QA role
- defines analysis categories
- gives a consistent output shape
- supports interview and POC discussion

Expected output shape:

```text
Summary:
- ...

Ambiguities:
- ...

Missing Rules:
- ...
```

Common mistake:

Asking for analysis without saying what kind of analysis is needed.

Where used:

LangGraph requirement analysis node, POC demo, QA assistant.

## 4. Test-case generation prompt

Bad prompt:

```text
Make test cases.
```

Improved prompt:

```text
You are a QA test designer.

Task:
Generate functional test cases for the requirement below.

Requirement:
{requirement}

Constraints:
- Include positive, negative, and edge cases.
- Do not include performance or security tests unless explicitly required.
- Keep steps beginner-readable.

Output format:
Return only valid JSON with this schema:
{
  "requirement": "string",
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

Why improved prompt is better:

- tells the model the domain role
- limits test types
- requires parseable JSON
- matches Pydantic validation patterns

Expected output shape:

```json
{
  "requirement": "User can log in",
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

Letting the model decide field names. This causes parsing problems.

Where used:

FastAPI `/generate-test-cases`, Streamlit UI, final POC.

## 5. API test generation prompt

Bad prompt:

```text
Make API tests for login.
```

Improved prompt:

```text
You are an API test engineer.

Task:
Generate API test ideas from the API details below.

API details:
{api_spec}

Constraints:
- Include success, validation failure, authentication failure, and edge cases.
- Mention HTTP method, endpoint, request body, expected status code, and expected response check.
- Do not invent fields that are not in the API details.

Output format:
Return a markdown table with columns:
Title | Method | Endpoint | Request Body | Expected Status | Expected Check
```

Why improved prompt is better:

- focuses on API testing
- requires method, endpoint, body, status, and response check
- reduces hallucinated API fields

Expected output shape:

```text
| Title | Method | Endpoint | Request Body | Expected Status | Expected Check |
|---|---|---|---|---|---|
```

Common mistake:

Not providing API details and expecting the model to know endpoint paths.

Where used:

API test generation labs, final POC, interview scenarios.

## 6. RAG prompt template

Bad prompt:

```text
Answer this question: {question}
```

Improved prompt:

```text
You are a grounded QA knowledge assistant.

Use only the provided context to answer the question.
If the context is insufficient, say:
"I do not know from the provided context."

Context:
{context}

Question:
{question}

Output format:
Return:
- Answer
- Source summary
- Missing information, if any
```

Why improved prompt is better:

- separates context from question
- tells the model not to invent unsupported facts
- defines refusal behavior when context is insufficient
- supports grounded RAG answers

Expected output shape:

```text
Answer:
...

Source summary:
...

Missing information:
...
```

Common mistake:

Putting context and question together without clear labels.

Where used:

RAG module, final POC `/ask-context`, LangGraph RAG node.

## 7. Agent system prompt

Bad prompt:

```text
You are an agent. Help the user.
```

Improved prompt:

```text
You are a controlled QA assistant agent.

Responsibilities:
- Answer questions about requirements using provided context.
- Generate test scenarios when asked.
- Use available tools only when they are needed.
- Do not invent project facts.
- If context is missing, ask for clarification or say what information is missing.

Tool behavior:
- Use the test data tool only for demo test data lookup.
- Do not call tools for simple explanation questions.

Response style:
- Be concise.
- Return structured output when requested.
```

Why improved prompt is better:

- defines role and boundaries
- explains tool usage
- controls hallucination risk
- guides response style

Expected output shape:

```text
Direct answer or structured response depending on task.
```

Common mistake:

Giving the agent tools but not explaining when to use them.

Where used:

MCP tool agents, LangGraph supervisor/worker prompts, final POC.

## 8. Evaluation prompt

Bad prompt:

```text
Is this good?
```

Improved prompt:

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

Evaluation rules:
- Mark "pass" only if the answer follows the schema.
- Mark "fail" if required fields are missing.
- Mark "fail" if the answer includes facts not supported by context.

Output format:
{
  "status": "pass|fail",
  "issues": ["string"],
  "concise_reasoning_summary": "string"
}
```

Why improved prompt is better:

- defines evaluation criteria
- separates schema, context, and answer
- returns structured review output
- avoids vague judgment

Expected output shape:

```json
{
  "status": "fail",
  "issues": ["Missing expected_result"],
  "concise_reasoning_summary": "The answer does not match the required schema."
}
```

Common mistake:

Asking a model to judge quality without criteria.

Where used:

LangGraph review node, final POC response review, automated output checks.

## 9. Code-only prompt

Bad prompt:

```text
Write code and explain it.
```

Improved prompt:

```text
Return only Python code.
Do not include markdown.
Do not include explanation.

Task:
Create a function named normalize_priority that accepts a string and returns uppercase priority.
If input is empty, return "P3".
```

Why improved prompt is better:

It avoids mixing code output and explanation when code-only output is needed.

Expected output shape:

```python
def normalize_priority(priority: str) -> str:
    if not priority:
        return "P3"
    return priority.upper()
```

Common mistake:

Asking for code-only output while also requesting a long explanation.

Where used:

Developer helpers, local scaffolding, controlled code generation tasks.

## 10. Summary prompt

Bad prompt:

```text
Summarize.
```

Improved prompt:

```text
Summarize the requirement below in 3 bullets.
Focus on user action, system behavior, and test risk.

Requirement:
{requirement}
```

Expected output shape:

```text
- User action: ...
- System behavior: ...
- Test risk: ...
```

Where used:

Requirement analysis, stand-and-deliver demo prep, interview explanations.

## 11. Classification prompt

Bad prompt:

```text
What is this?
```

Improved prompt:

```text
Classify the requirement risk as low, medium, or high.
Return only one label.

Requirement:
{requirement}
```

Expected output shape:

```text
medium
```

Where used:

Risk tagging, triage, evaluation nodes.

## 12. Extraction prompt

Bad prompt:

```text
Find stuff from this text.
```

Improved prompt:

```text
Extract the following fields from the text:
- user_action
- system_response
- validation_rules
- error_conditions

Return only valid JSON.

Text:
{requirement}
```

Expected output shape:

```json
{
  "user_action": "string",
  "system_response": "string",
  "validation_rules": ["string"],
  "error_conditions": ["string"]
}
```

Where used:

Requirement parsing, Pydantic structured output, LangGraph analysis node.

## 13. Practical reminder

Prompt output is not a backend contract by itself.

Use:

- prompt to guide the model
- Pydantic to validate structure
- RAG to provide context
- LangGraph to control workflow
- MCP tools for approved external actions

This combination is more reliable than prompt wording alone.
