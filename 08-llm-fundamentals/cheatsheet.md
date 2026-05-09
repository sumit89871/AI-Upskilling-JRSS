# LLM Fundamentals Cheatsheet

Use this for quick revision after studying the module.

## 1. LLM

Meaning:

A Large Language Model takes text input and generates text output.

When to use:

Use for summarization, Q&A, extraction, classification, test generation, and assistant workflows.

Example:

```text
Prompt: Generate login test cases.
Response: Valid login, invalid password, locked account...
```

Be careful:

An LLM is not the full application. Your app still handles RAG, validation, security, UI, and APIs.

## 2. Prompt

Meaning:

Input instruction or question sent to the model.

When to use:

Use to tell the model what task to perform and what output format is expected.

Example:

```text
Return three API test cases as JSON.
```

Be careful:

Vague prompts often produce vague outputs.

## 3. Completion / response

Meaning:

The generated output from the model.

When to use:

Use after the model processes the prompt.

Example:

```text
1. Verify 200 response for valid login.
```

Be careful:

Output can be wrong or unsupported. Validate important results.

## 4. Token

Meaning:

A small text unit processed by the model.

When to use:

Think about tokens when estimating context length, cost, and output limits.

Example:

```text
password reset
```

may be split into multiple tokens.

Be careful:

Token is not always the same as word.

## 5. Tokenization

Meaning:

The process of splitting text into tokens.

When to use:

Relevant when debugging context limits and chunking documents.

Example:

```text
text -> tokenizer -> tokens
```

Be careful:

Different models may tokenize text differently.

## 6. Context window

Meaning:

Maximum token space the model can consider in one request.

When to use:

Use when planning prompts, RAG context, and chat history.

Example:

```text
system prompt + question + retrieved chunks + output
```

Be careful:

More context does not automatically mean better answers.

## 7. Temperature

Meaning:

Controls randomness.

When to use:

Use low temperature for strict output and higher temperature for brainstorming.

Example:

```python
temperature = 0.2
```

Be careful:

Higher temperature does not mean smarter output.

## 8. top_p

Meaning:

Controls the pool of likely next tokens considered during generation.

When to use:

Use as a sampling control, usually without over-tuning it with temperature at beginner level.

Example:

```python
top_p = 0.9
```

Be careful:

Do not randomly change both temperature and `top_p` without testing.

## 9. max tokens

Meaning:

Maximum number of output tokens the model may generate.

When to use:

Use to limit response length and cost.

Example:

```python
max_tokens = 500
```

Be careful:

If too low, the answer may be cut off.

## 10. Embedding

Meaning:

Text converted into a numeric vector representing meaning.

When to use:

Use for semantic search and RAG retrieval.

Example:

```python
embedding = [0.12, -0.44, 0.87]
```

Be careful:

Embedding is not the final answer. It supports search.

## 11. RAG

Meaning:

Retrieval Augmented Generation retrieves relevant context before generating an answer.

When to use:

Use when answers must come from documents, policies, manuals, or project notes.

Example:

```text
question -> retrieve chunks -> prompt with context -> answer
```

Be careful:

RAG does not permanently train the model.

## 12. Hallucination

Meaning:

Confident but wrong, unsupported, or invented model output.

When to use:

Discuss as a risk in AI app design.

Example:

Model invents a refund policy that was not in the provided document.

Be careful:

Grounding reduces risk but does not eliminate it fully.

## 13. Grounding

Meaning:

Giving the model trusted context to base the answer on.

When to use:

Use for business, policy, legal, project, or knowledge-base answers.

Example:

```text
Use this context to answer...
```

Be careful:

Bad context can still produce bad answers.

## 14. Fine-tuning

Meaning:

Additional training to adjust model behavior.

When to use:

Consider for repeated style or task behavior after simpler options are tested.

Example:

Training on many examples of desired output format.

Be careful:

For changing documents or private knowledge, RAG is usually better first.

## 15. Inference

Meaning:

Running a trained model to get output.

When to use:

Every time your app sends a prompt and receives a response.

Example:

```text
prompt -> model -> response
```

Be careful:

Inference is not training.

## 16. Hosted model

Meaning:

Model runs on provider infrastructure and is accessed through API.

When to use:

Use for strong quality and quick setup.

Example:

OpenAI API or Gemini API.

Be careful:

Consider API keys, cost, rate limits, and data privacy.

## 17. Local model

Meaning:

Model runs on your machine or local server.

When to use:

Use for local demos, offline experiments, or privacy-sensitive exploration.

Example:

Ollama running a local model.

Be careful:

Laptop hardware may limit speed and quality.

## 18. Open model

Meaning:

Model is more accessible for local running or adaptation depending on license.

When to use:

Use when control, local deployment, or experimentation matters.

Example:

Open model from a model hub.

Be careful:

Open does not always mean unrestricted commercial use.

## 19. Closed model

Meaning:

Provider-controlled model usually accessed through API.

When to use:

Use when quality and managed infrastructure matter.

Example:

Commercial hosted model API.

Be careful:

You depend on provider pricing, limits, and terms.
