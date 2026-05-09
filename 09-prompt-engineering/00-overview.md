# Prompt Engineering Overview

## 1. What prompt engineering is

Prompt engineering means designing instructions so a model returns useful output.

For beginner AI Engineer work, a prompt is not just a question typed into a chatbot.

A prompt can include:

- instruction
- context
- constraints
- examples
- output format
- safety rules
- tool usage guidance
- refusal behavior when context is insufficient

Simple meaning:

```text
Prompt engineering = clear task design for a language model
```

## 2. The most important beginner idea

The model responds based on what you give it.

If the prompt is vague, the output will often be vague.

Bad prompt:

```text
Write tests.
```

Improved prompt:

```text
You are a QA analyst.
Generate functional test cases for the requirement below.
Include positive, negative, and edge cases.
Return a JSON array.

Requirement:
User can reset password using a registered email.
```

Why improved prompt is better:

- tells the model the role
- gives the task
- provides the requirement
- sets test categories
- asks for a parseable output shape

## 3. Beginner mental model

Use this structure:

```text
Instruction + context + constraints + examples + output format -> better model response
```

Meaning:

- instruction tells the model what to do
- context gives information to use
- constraints say what must or must not happen
- examples show the pattern
- output format controls the shape of the response

## 4. Why prompts matter

Prompts matter because model output becomes part of the application.

In an AI Engineer POC, prompt output may be:

- displayed in Streamlit
- returned from FastAPI
- validated with Pydantic
- passed to a LangGraph review node
- used to call an MCP tool
- stored as generated test cases

If output is inconsistent, the application becomes harder to parse, test, and explain.

## 5. Instruction

Instruction tells the model what task to perform.

Bad instruction:

```text
Do login.
```

Improved instruction:

```text
Generate functional test cases for the login requirement.
```

Why improved prompt is better:

It says the exact task: generate functional test cases.

Expected output shape:

```text
List of test cases or JSON test case objects.
```

Common mistake:

Using one or two vague words and expecting the model to infer the full task.

Where used:

All OpenAI/Gemini calls, RAG prompts, LangGraph nodes, and POC test generation.

## 6. Context

Context is the information the model should use.

Bad prompt:

```text
Generate tests for this feature.
```

Improved prompt:

```text
Generate tests for this requirement:
Users can log in with email and password. After 5 failed attempts, the account is locked for 15 minutes.
```

Why improved prompt is better:

The model now knows the actual business rule.

Expected output shape:

```text
Test cases covering valid login, invalid password, and account lockout.
```

Common mistake:

Assuming the model knows private project requirements without being given them.

Where used:

RAG, final POC, requirement analysis, API test generation.

## 7. Constraints

Constraints are rules that limit the output.

Bad prompt:

```text
Generate test cases.
```

Improved prompt:

```text
Generate exactly 5 test cases.
Include at least one positive, one negative, and one edge case.
Do not include performance or security tests.
```

Why improved prompt is better:

It reduces scope and controls what the model should include or exclude.

Expected output shape:

```text
Exactly 5 functional test cases.
```

Common mistake:

Adding too many conflicting constraints, such as "be very detailed" and "return only one line."

Where used:

POC demos, structured GenAI output, API test generation, evaluation prompts.

## 8. Examples

Examples show the model the pattern you want.

Bad prompt:

```text
Classify tickets.
```

Improved prompt:

```text
Classify each ticket as bug, feature, or question.

Example:
Ticket: App crashes on login.
Category: bug

Now classify:
Ticket: Add dark mode to dashboard.
Category:
```

Why improved prompt is better:

The example teaches the expected label style.

Expected output shape:

```text
feature
```

Common mistake:

Giving examples that do not match the desired output format.

Where used:

Few-shot classification, extraction, evaluation, test case style control.

## 9. Output format

Output format tells the model how to structure the answer.

Bad prompt:

```text
Generate test cases.
```

Improved prompt:

```text
Return only valid JSON using this schema:
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

Why improved prompt is better:

It gives the model a target structure that code can parse and validate.

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

Asking for JSON but allowing markdown, explanation, and extra text around it.

Where used:

Pydantic validation, FastAPI responses, structured GenAI output, final POC.

## 10. Chain-of-thought caution

Chain-of-thought means detailed internal reasoning steps.

For application work, do not depend on hidden internal reasoning.

Safer instruction:

```text
Provide the final answer and a concise reasoning summary.
```

Why this is better:

It gives useful explanation without requiring hidden reasoning details.

Expected output shape:

```text
Answer:
...

Concise reasoning summary:
...
```

Common mistake:

Asking the model to expose hidden chain-of-thought instead of asking for a user-facing summary.

Where used:

Interview answers, evaluation prompts, review nodes, POC explanations.

## 11. Prompt engineering vs fine-tuning

Prompt engineering changes the instruction.

Fine-tuning changes model behavior through additional training.

Use prompt engineering first because it is faster, cheaper, and easier to test.

Use fine-tuning only when many examples and repeated behavior requirements justify it.

## 12. Prompt engineering vs RAG

Prompt engineering improves instructions.

RAG adds external context.

If the model lacks information, a better prompt alone may not be enough. You need grounding context.

Example:

```text
Good prompt + no policy text = model may guess.
Good prompt + retrieved policy text = grounded answer.
```

## 13. Common prompt mistakes

- vague task
- missing context
- no output format
- too many tasks in one prompt
- conflicting constraints
- asking for strict JSON but allowing prose
- not saying what to do if context is insufficient
- relying on model output without validation
- using persona without a clear task
- giving examples that do not match desired output

## 14. Where used in AI Engineer work

Prompt engineering appears in:

- OpenAI/Gemini API calls
- RAG answer prompts
- LangGraph generation and review nodes
- MCP tool-using agent prompts
- FastAPI GenAI endpoints
- Streamlit demos
- structured output validated by Pydantic
- Mettl and interview discussion
- final POC demo scripts
