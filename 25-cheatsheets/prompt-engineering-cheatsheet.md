# Prompt Engineering Cheatsheet

## Prompt Structure

Syntax: `Instruction + context + constraints + examples + output format`

Meaning: Complete instruction design for useful model output.

Use when: Building LLM prompts for apps.

Example: role, task, requirement, rules, JSON schema.

Be careful: Vague prompts produce vague output.

## JSON Prompt

Syntax: `Return only valid JSON. Do not include markdown.`

Meaning: Ask for parseable model output.

Use when: App will parse and validate response.

Example: generated test cases.

Be careful: Still validate with Pydantic.

## RAG Prompt

Syntax: `Use only the provided context. If insufficient, say so.`

Meaning: Ground answer in retrieved context.

Use when: Answering from documents.

Be careful: Separate context and question clearly.

## Concise Reasoning Summary

Syntax: `Provide final answer and concise reasoning summary.`

Meaning: User-facing explanation without hidden reasoning.

Use when: Review or explanation is needed.

Be careful: Long reasoning is not proof of correctness.
