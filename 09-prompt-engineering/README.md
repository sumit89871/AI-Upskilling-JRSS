# 09 Prompt Engineering

## 1. What This Module Is

This module teaches practical prompt engineering for AI Engineer work.

Prompt engineering means designing clear instructions so a language model returns useful, controlled, and application-friendly output.

Simple meaning:

```text
Prompt engineering = writing model instructions that are clear enough for software use
```

This is not about magic wording. It is about giving the model the right task, context, constraints, examples, and output format.

## 2. Why It Matters

Bad prompts create vague, inconsistent, hard-to-parse, or unsafe answers.

Good prompts help with:

- requirement analysis
- test case generation
- API test generation
- JSON output
- RAG grounded answers
- agent system behavior
- evaluation checks
- POC demos
- interview explanation

In AI Engineer work, a prompt is often part of application design, not only a chat message.

## 3. What The Learner Should Finish Knowing

After this module, you should understand:

- instruction
- context
- constraints
- examples
- output format
- zero-shot prompting
- one-shot prompting
- few-shot prompting
- persona-based prompting
- structured prompting
- JSON output prompting
- code-only prompting
- chain-of-thought caution
- concise reasoning summary
- test-case generation prompts
- RAG prompt templates
- agent system prompts
- evaluation prompts
- common prompt mistakes

## 4. Study Order

1. Read `00-overview.md`.
2. Read `01-prompt-patterns.md`.
3. Read `02-ai-engineer-prompts.md`.
4. Complete `exercises.md`.
5. Revise with `cheatsheet.md`.
6. Practice `interview-questions.md`.

## 5. File List

- `README.md`: this module guide.
- `00-overview.md`: beginner mental model, prompt parts, why prompts matter, and core mistakes.
- `01-prompt-patterns.md`: zero-shot, one-shot, few-shot, persona, structured, JSON, code-only, and reasoning-summary patterns.
- `02-ai-engineer-prompts.md`: practical templates for test generation, RAG, agent prompts, and evaluation prompts.
- `exercises.md`: prompt rewriting exercises with bad prompts, improved prompts, expected output style, hints, and common mistakes.
- `cheatsheet.md`: concise but explained prompt engineering revision guide.
- `interview-questions.md`: interview-ready Q&A with short answer, expanded answer, project example, and common wrong answer.

## 6. Practical Scope

This module focuses on prompts used in real AI Engineer tasks:

- OpenAI/Gemini API calls
- FastAPI GenAI endpoints
- RAG answer generation
- LangGraph generation and review nodes
- MCP tool-using agents
- final POC demo prompts

## 7. What Not To Over-Focus On

Do not over-focus on memorizing prompt tricks.

Focus on the structure:

```text
Instruction + context + constraints + examples + output format -> better model response
```

Do not depend on hidden chain-of-thought. For applications and demos, ask for a concise reasoning summary when explanation is needed.

## 8. How This Helps In AI Engineer JRSS / Mettl / POC / Interview

For JRSS labs, prompt engineering helps you control GenAI outputs.

For Mettl-style screening, you should know zero-shot, few-shot, structured prompting, RAG prompting, and hallucination reduction.

For the final POC, prompts control requirement analysis, test generation, RAG answers, and review output.

For interviews, you can explain how you make model output reliable enough for application use.
