# LLM Fundamentals Exercises

These exercises are conceptual but practical. Answer in simple language first, then connect the concept to AI Engineer work.

## Exercise 1: Explain LLM vs application

### Task

Explain the difference between an LLM and an AI application.

### Expected answer style

```text
An LLM generates text. An AI application is the software around the model that handles user input, prompt building, API calls, RAG, tool calls, validation, UI, and security.
```

### Hint

Use this comparison:

```text
model = engine
application = full vehicle around the engine
```

### Self-check

If you build a FastAPI backend that calls OpenAI, did you build the LLM itself?

Expected answer:

No. You built an application that uses an LLM.

### Solution outline

Mention what the model does and what the application does separately.

### Common mistake

Saying "I built an LLM" when you only integrated an LLM API.

## Exercise 2: Prompt vs completion

### Task

Write one example prompt and one possible completion.

### Expected answer style

Prompt:

```text
Generate three test cases for password reset.
```

Completion:

```text
1. Valid email receives reset link.
2. Unknown email receives a safe generic message.
3. Expired reset link is rejected.
```

### Hint

Prompt is input. Completion or response is output.

### Self-check

Can two model calls produce slightly different completions for the same prompt?

Expected answer:

Yes, especially when generation settings allow randomness.

### Common mistake

Calling the model output the prompt. The prompt is what you send to the model.

## Exercise 3: Token vs word

### Task

Explain why a token is not always the same as a word.

### Expected answer style

```text
A word is a human reading unit. A token is a model processing unit. A token may be a full word, part of a word, punctuation, or spacing.
```

### Hint

Think of long words that may be split into smaller pieces.

### Self-check

Does `max_tokens` mean maximum words?

Expected answer:

No. It means maximum output tokens.

### Solution outline

Define word, define token, then explain why model limits use tokens.

### Common mistake

Estimating model cost or output length using exact word count only.

## Exercise 4: Context window scenario

### Task

Explain why context window matters when answering questions from a long policy document.

### Expected answer style

```text
The model can only consider a limited number of tokens in one request. If the document is too long, we should not paste everything. We should chunk the document and retrieve relevant chunks using RAG.
```

### Hint

Context window includes system prompt, user question, chat history, RAG context, and output.

### Self-check

Does a larger context window automatically guarantee a better answer?

Expected answer:

No. Irrelevant or noisy context can still reduce answer quality.

### Common mistake

Trying to paste all documents into every prompt.

## Exercise 5: Choose parameters

### Task

Choose suitable settings for:

1. Strict JSON output.
2. Brainstorming edge test cases.
3. Short summary.

### Expected answer style

```text
Strict JSON: low temperature, enough max_tokens for full JSON.
Brainstorming: higher temperature for variety.
Short summary: low or moderate temperature and limited max_tokens.
```

### Hint

Temperature controls randomness. `max_tokens` controls output length.

### Self-check

Why is high temperature risky for strict JSON?

Expected answer:

It may produce more variation and break the required format.

### Common mistake

Thinking higher temperature means smarter output.

## Exercise 6: Hallucination and grounding

### Task

Explain hallucination and grounding using a company policy example.

### Expected answer style

```text
Hallucination is when the model invents a policy or gives unsupported information. Grounding means giving the model trusted policy text and asking it to answer using that context.
```

### Hint

Use this flow:

```text
trusted policy text + question -> grounded prompt -> answer
```

### Self-check

Does grounding remove all risk?

Expected answer:

No. It reduces risk, but the app should still validate, cite sources, and review important answers.

### Common mistake

Trusting a confident answer without checking sources.

## Exercise 7: RAG vs fine-tuning

### Task

Choose RAG or fine-tuning for each case:

1. Answer questions from frequently changing project documents.
2. Make the model consistently write in a company-specific format.
3. Build a QA assistant that cites source chunks.

### Expected answer

1. RAG.
2. Fine-tuning may help later, but prompt templates or examples may be tried first.
3. RAG.

### Hint

RAG gives context at answer time. Fine-tuning changes model behavior through training.

### Self-check

Does RAG permanently update the model weights?

Expected answer:

No.

### Common mistake

Saying fine-tuning is always the best way to add company knowledge.

## Exercise 8: Hosted vs local model

### Task

Compare hosted and local models for a beginner POC.

### Expected answer style

```text
Hosted model is easier and often stronger, but needs internet, API key, cost control, and privacy review. Local model gives more local control and offline possibilities, but may be slower or lower quality on a normal laptop.
```

### Hint

Compare where the model runs and who handles infrastructure.

### Self-check

Does local model always mean better answer quality?

Expected answer:

No. Quality depends on the model and hardware.

### Common mistake

Thinking local model always means private if the application still sends data to external APIs.

## Exercise 9: Open vs closed model

### Task

Explain open model vs closed model.

### Expected answer style

```text
An open model is usually more accessible for local running or adaptation depending on license. A closed model is usually accessed through a provider API and the weights are not public.
```

### Hint

Mention license and provider dependency.

### Self-check

Does open always mean free for any commercial use?

Expected answer:

No. License must be checked.

### Common mistake

Ignoring model licenses in enterprise work.
