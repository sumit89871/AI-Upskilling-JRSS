# Prompt Engineering Interview Questions

Use these answers for Mettl-style screening, POC explanation, and AI Engineer interviews.

## 1. What is prompt engineering?

Short answer:

Prompt engineering is designing clear instructions so a language model returns useful, controlled output.

Expanded answer:

In AI applications, prompts often include task, context, constraints, examples, and output format. Prompt engineering helps make model output more reliable, parseable, and aligned with the application goal.

Project example:

In a QA assistant POC, a test-generation prompt can ask the model to return JSON test cases with title, type, priority, steps, and expected result.

Common wrong answer:

"Prompt engineering is just asking questions."

Why this is wrong:

Application prompts need structure, constraints, and output control.

## 2. Why do prompts matter?

Short answer:

Prompts shape model behavior, output format, scope, and quality.

Expanded answer:

A vague prompt may produce vague output. A structured prompt can reduce ambiguity, improve consistency, and make the output easier to validate with Pydantic or return through FastAPI.

Project example:

The final POC needs predictable test case output, so the prompt should define the JSON schema.

Common wrong answer:

"The model is smart, so the prompt does not matter."

Why this is wrong:

Even strong models need clear instructions and context for reliable application output.

## 3. What are the main parts of a good prompt?

Short answer:

Instruction, context, constraints, examples, and output format.

Expanded answer:

Instruction tells the model what to do. Context gives the information to use. Constraints limit scope. Examples teach the pattern. Output format controls the response shape.

Project example:

A RAG prompt includes retrieved context, the user question, a rule to answer only from context, and an output format.

Common wrong answer:

"A good prompt only needs a role."

Why this is wrong:

Persona helps, but task, context, constraints, and format are usually more important.

## 4. What is zero-shot prompting?

Short answer:

Zero-shot prompting gives the task without examples.

Expanded answer:

It works well for simple tasks where the model already understands the instruction and output format.

Project example:

```text
Classify this ticket as bug, feature, or question. Return only the label.
```

Common wrong answer:

"Zero-shot means no instruction."

Why this is wrong:

Zero-shot means no examples, not no instruction.

## 5. What is one-shot prompting?

Short answer:

One-shot prompting gives one example before the real task.

Expanded answer:

It helps the model copy a specific style or output pattern.

Project example:

Give one example test case title, then ask the model to create a new title for another requirement.

Common wrong answer:

"One-shot means asking the model only once."

Why this is wrong:

It refers to one example in the prompt.

## 6. What is few-shot prompting?

Short answer:

Few-shot prompting gives multiple examples before the real task.

Expanded answer:

Few-shot examples help the model learn category boundaries, output style, or extraction patterns.

Project example:

Provide examples of bug, feature, and question ticket classification before classifying a new ticket.

Common wrong answer:

"Few-shot means short prompt."

Why this is wrong:

It means a few examples are included.

## 7. What is persona-based prompting?

Short answer:

Persona prompting gives the model a role, such as QA analyst or API test engineer.

Expanded answer:

Persona helps guide tone and focus, but it must be combined with clear task, context, constraints, and output format.

Project example:

```text
You are a senior QA analyst. Review this requirement for ambiguity and test risks.
```

Common wrong answer:

"Persona alone is enough."

Why this is wrong:

A role without a task does not tell the model what to do.

## 8. What is structured prompting?

Short answer:

Structured prompting organizes the prompt into labeled sections.

Expanded answer:

It separates role, task, context, constraints, and output format so the model can follow the instruction more reliably.

Project example:

Use sections like `Task`, `Context`, `Rules`, and `Output format` in a test generation prompt.

Common wrong answer:

"Structured prompt means the output must be JSON."

Why this is wrong:

Structured prompting is about prompt organization. JSON output is one possible output format.

## 9. What is JSON output prompting?

Short answer:

JSON output prompting asks the model to return valid JSON in a specified schema.

Expanded answer:

It is useful when application code needs to parse the response. However, prompt instructions alone are not enough. The app should still parse and validate the JSON.

Project example:

The POC can ask for test cases as JSON and validate them with Pydantic.

Common wrong answer:

"If I ask for JSON, it will always be valid."

Why this is wrong:

Models can still return invalid JSON or extra text. Validation is required.

## 10. What is code-only prompting?

Short answer:

Code-only prompting asks the model to return only code and no explanation.

Expanded answer:

It is useful when the output will be inserted into a file or tested directly. It should not be mixed with requests for explanation.

Project example:

Generate only a FastAPI route function with no markdown fences.

Common wrong answer:

"Code-only prompt should also explain every line."

Why this is wrong:

That conflicts with code-only output.

## 11. What is the safe alternative to asking for hidden chain-of-thought?

Short answer:

Ask for a concise reasoning summary.

Expanded answer:

For application output, you usually need a user-facing explanation, not hidden internal reasoning. A concise reasoning summary gives useful context without requiring hidden chain-of-thought.

Project example:

In an evaluation node, ask for `status`, `issues`, and `concise_reasoning_summary`.

Common wrong answer:

"Always ask for full hidden chain-of-thought."

Why this is wrong:

Production apps should use concise, user-facing explanations and objective checks.

## 12. What is a RAG prompt?

Short answer:

A RAG prompt includes retrieved context and asks the model to answer using that context.

Expanded answer:

It should clearly separate context from the user question and say what to do if the context is insufficient.

Project example:

```text
Use only the provided context. If insufficient, say you do not know from the provided context.
```

Common wrong answer:

"A RAG prompt is just any question sent to an LLM."

Why this is wrong:

RAG prompts include retrieved context and grounding rules.

## 13. What is an agent system prompt?

Short answer:

An agent system prompt defines the agent's role, responsibilities, tool rules, boundaries, and response style.

Expanded answer:

Agents may call tools or make routing decisions. The system prompt should explain when tools should be used, when not to use them, and how to handle missing information.

Project example:

An MCP-enabled QA agent prompt can say: use the test data tool only for demo test data lookup and do not invent project facts.

Common wrong answer:

"Agent prompt only needs 'You are helpful.'"

Why this is wrong:

Tool-using agents need clear boundaries and tool-use rules.

## 14. What is an evaluation prompt?

Short answer:

An evaluation prompt asks the model to check an output against rules or a schema.

Expanded answer:

It should define the criteria for pass/fail, such as schema validity, supported facts, required fields, or formatting rules.

Project example:

A LangGraph review node can evaluate whether generated test cases include title, type, priority, steps, and expected result.

Common wrong answer:

"Evaluation prompt means asking if the answer is good."

Why this is weak:

"Good" is vague. The prompt needs objective criteria.

## 15. How do prompts help reduce hallucination?

Short answer:

Prompts reduce hallucination by providing context, grounding rules, and instructions for insufficient information.

Expanded answer:

For knowledge-based questions, the prompt should tell the model to answer only from provided context and say when the context is insufficient. RAG improves this by retrieving relevant context first.

Project example:

In a RAG QA assistant, the prompt says: "Use only the provided context. If context is insufficient, say so."

Common wrong answer:

"A better prompt removes hallucination completely."

Why this is wrong:

Prompting reduces risk but does not eliminate it. Retrieval quality, validation, and review still matter.

## 16. How would you explain prompt engineering in your POC?

Short answer:

I used structured prompts to control the model's role, context, constraints, and output format.

Expanded answer:

For test generation, I used a prompt that includes the requirement, required test categories, and JSON schema. For RAG answers, I used a prompt that includes retrieved context and instructs the model not to invent facts. For review, I used an evaluation prompt with pass/fail criteria.

Project example:

```text
Requirement -> structured generation prompt -> JSON test cases -> Pydantic validation -> reviewed final response
```

Common wrong answer:

"I just asked the model to generate tests."

Why this is weak:

It does not explain output control, grounding, or validation.
