# 08 LLM Fundamentals

## 1. What This Module Is

This module explains Large Language Model fundamentals from beginner level.

The goal is not to turn you into a model researcher. The goal is to help you understand the LLM concepts that appear in real AI Engineer work.

Simple meaning:

```text
LLM fundamentals = the basic ideas needed to use language models safely in applications
```

You will learn what an LLM does, what it does not do, why prompts matter, why tokens matter, how embeddings and RAG work, and how model settings affect output.

## 2. Why It Matters

AI Engineers usually do not train huge models from scratch.

In practical work, you usually:

- call OpenAI, Gemini, watsonx, or another hosted model
- run a smaller local model through Ollama or Hugging Face
- build prompts
- pass business context with RAG
- validate structured output
- connect models to tools through MCP
- orchestrate steps with LangGraph
- expose results through FastAPI or Streamlit

If you do not understand LLM basics, you may misuse the model, overtrust output, pass too much context, choose wrong parameters, or fail to explain your POC in an interview.

## 3. What The Learner Should Finish Knowing

After this module, you should be able to explain:

- what an LLM is
- model vs application
- prompt vs completion
- token vs word
- tokenization
- context window
- embeddings
- embedding vs token
- attention basics
- transformer basics
- foundation model
- MoE basics
- temperature
- top_p
- max tokens
- hallucination
- grounding
- RAG
- fine-tuning basics
- inference
- local model vs hosted model
- open model vs closed model

## 4. Study Order

1. Read `00-overview.md`.
2. Read `01-tokens-context-parameters.md`.
3. Read `02-embeddings-rag-model-types.md`.
4. Complete `exercises.md`.
5. Revise with `cheatsheet.md`.
6. Practice `interview-questions.md`.

## 5. File List

- `README.md`: this module guide.
- `00-overview.md`: beginner explanation of LLMs, model vs application, prompt/completion, inference, attention, transformers, hallucination, grounding, and POC usage.
- `01-tokens-context-parameters.md`: tokens, tokenization, context window, temperature, top_p, max tokens, and parameter selection.
- `02-embeddings-rag-model-types.md`: embeddings, RAG, fine-tuning, hosted/local models, open/closed models, foundation models, and MoE basics.
- `exercises.md`: hands-on conceptual practice with expected answer style, hints, self-checks, and common mistakes.
- `cheatsheet.md`: concise but explained revision notes.
- `interview-questions.md`: short answers, expanded answers, project examples, and common wrong answers.

## 6. Practical Scope

This module focuses on implementation-level understanding.

You should understand enough to:

- configure LLM API calls
- explain RAG design
- debug token/context issues
- choose lower or higher temperature intentionally
- explain hallucination risk
- compare hosted and local model usage
- discuss model limitations in a POC demo

## 7. What Not To Over-Focus On

Do not over-focus on transformer mathematics, training infrastructure, GPU optimization, or research-level architecture details at this stage.

First become strong with practical concepts:

- prompt input
- generated output
- token limits
- grounding
- retrieval
- model settings
- validation and safety

## 8. How This Helps In AI Engineer JRSS / Mettl / POC / Interview

For JRSS labs, this module helps you understand why GenAI examples are written a certain way.

For Mettl-style screening, it prepares you for conceptual LLM, RAG, token, temperature, and hallucination questions.

For the final POC, it helps you explain what the model does, what your application does, and why RAG or validation is needed.

For interviews, it helps you avoid shallow answers like "LLM is AI" and instead explain practical system design clearly.
