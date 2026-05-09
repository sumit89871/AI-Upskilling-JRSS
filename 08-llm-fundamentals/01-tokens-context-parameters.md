# Tokens, Context Window, and Parameters

## 1. What tokens are

Tokens are the small text units that an LLM processes.

Simple meaning:

```text
token = a piece of text used by the model
```

A token may be:

- a full word
- part of a word
- punctuation
- a space pattern
- a symbol

Important beginner point:

Models do not directly think in human words. They process tokens.

## 2. Token vs word

A word and a token are not always the same.

Example:

```text
unbelievable
```

This may be split into multiple tokens, such as:

```text
un + believable
```

Exact tokenization depends on the model tokenizer.

Comparison:

| Concept | Meaning |
|---|---|
| Word | Human reading unit |
| Token | Model processing unit |

Why it matters:

Model limits, cost, and output length are often based on tokens, not words.

## 3. Tokenization

Tokenization is the process of splitting text into tokens.

Mental model:

```text
your text -> tokenizer -> tokens -> model
```

Example:

```text
Generate login tests.
```

The tokenizer may break it into pieces similar to:

```text
Generate | login | tests | .
```

This is simplified. Real tokenization can split text in less obvious ways.

What the developer usually does:

- estimates token usage
- avoids sending too much text
- chunks documents for RAG
- sets output limits

What the model provider does:

- runs the tokenizer
- counts tokens
- processes token IDs internally

## 4. Beginner mental model

Use this model:

```text
Prompt text -> tokenization -> input tokens -> model predicts output tokens -> response text
```

For API work:

```text
system message + user message + RAG context + chat history + output = total token usage
```

## 5. Context window

Context window is the maximum amount of text, measured in tokens, that the model can consider in one request.

Simple meaning:

```text
context window = model's working space for one request
```

It includes:

- system instructions
- user question
- chat history
- retrieved RAG context
- tool results included in prompt
- generated response

Important:

The context window is not only input. The output also uses tokens.

## 6. Why context window matters

If your prompt is too long, the request may fail, truncate, become expensive, or produce weaker answers.

Example:

You have a 200-page policy document.

Bad approach:

```text
Paste the whole document into every prompt.
```

Better approach:

```text
Chunk the document -> retrieve relevant chunks -> include only useful context
```

This is why RAG is important.

## 7. Context window vs memory

Context window and memory are not the same.

| Concept | Meaning |
|---|---|
| Context window | Text the model can see in one request |
| Memory | Information stored by the application across requests |

If old conversation text is not included in the current request or stored/retrieved by the app, the model may not have access to it.

## 8. max tokens

`max_tokens` usually controls the maximum output length.

Simple meaning:

```text
max_tokens = how many tokens the model is allowed to generate
```

Example:

```python
config = {"max_tokens": 500}
```

Syntax breakdown:

- `config` is a Python dictionary variable.
- `{}` creates a dictionary.
- `"max_tokens"` is the key.
- `500` is the value.
- this means the model may generate up to about 500 output tokens.

Common mistake:

Thinking `max_tokens` means maximum words. It means output tokens, not words.

If `max_tokens` is too low, the answer may stop halfway.

## 9. Temperature

Temperature controls randomness.

Simple meaning:

```text
lower temperature = more consistent
higher temperature = more varied
```

Example:

```python
config = {"temperature": 0.2}
```

Use low temperature for:

- JSON output
- classification
- extraction
- test case format
- API payload generation
- interview-style precise answers

Use higher temperature for:

- brainstorming
- creative writing
- idea generation

Common mistake:

Thinking higher temperature means smarter. It does not. It means more random or varied.

## 10. top_p

`top_p` is another generation control parameter.

Simple meaning:

```text
top_p controls how wide the model's token choice pool is
```

It is often called nucleus sampling.

Beginner-level explanation:

When generating the next token, the model has many possible choices. `top_p` controls how many likely choices are considered.

Example:

```python
config = {"top_p": 0.9}
```

In beginner projects, do not over-tune both `temperature` and `top_p` at the same time. Start with provider defaults or simple low-temperature settings.

## 11. Example parameter config

```python
config = {
    "temperature": 0.2,
    "top_p": 0.9,
    "max_tokens": 500
}
```

Read it slowly:

- `config` is a dictionary.
- `"temperature": 0.2` asks for fairly consistent output.
- `"top_p": 0.9` keeps token choice reasonably controlled.
- `"max_tokens": 500` limits generated output length.
- commas separate dictionary entries.

This kind of config appears in OpenAI, Gemini, and other model API calls, although exact parameter names may vary by provider.

## 12. Parameter choices by use case

Strict JSON output:

```python
temperature = 0.0
max_tokens = 500
```

Why:

You want consistent format and less creative variation.

Test case generation:

```python
temperature = 0.2
max_tokens = 800
```

Why:

You want useful variety but still controlled structure.

Brainstorming:

```python
temperature = 0.7
max_tokens = 1000
```

Why:

You want more diverse ideas.

## 13. Expected results

Low temperature:

```text
More predictable, consistent output.
```

High temperature:

```text
More varied, less predictable output.
```

Low max tokens:

```text
Shorter answer, possible cutoff.
```

High max tokens:

```text
Longer answer possible, higher cost and latency.
```

## 14. Debugging token and parameter issues

Problem:

```text
Answer is cut off.
```

Likely cause:

`max_tokens` is too low.

Problem:

```text
Model ignores some document content.
```

Likely cause:

Too much context, irrelevant context, or important text outside effective attention.

Problem:

```text
JSON output keeps changing shape.
```

Likely cause:

Temperature too high, prompt not strict enough, or no structured output validation.

Problem:

```text
Cost is high.
```

Likely cause:

Too many input tokens, too much chat history, too large RAG chunks, or overly high output limit.

## 15. Similar concepts beginners confuse

### Token vs word

A word is what humans read. A token is what the model processes.

### Context window vs max tokens

Context window is total model working space.

`max_tokens` usually controls output length.

### Temperature vs top_p

Both affect randomness, but they do it differently. Beginners should avoid over-tuning both at once.

### Bigger context vs better answer

A bigger context window allows more text, but irrelevant text can still confuse the model.

## 16. Quick practice

Choose parameters for:

1. Strict JSON output for API test cases.
2. Creative brainstorming for possible edge cases.
3. Short summary of a requirement.

Expected answer style:

```text
Use low temperature for strict JSON because format consistency matters.
Use higher temperature for brainstorming because variation is useful.
Use moderate or low max_tokens for short summaries to avoid long output.
```

## 17. Where used in AI Engineer work

Tokens, context windows, and parameters appear in:

- OpenAI/Gemini API calls
- RAG chunk size decisions
- prompt engineering
- output truncation debugging
- cost estimation
- structured JSON response generation
- LangGraph generation nodes
- final POC test case generation
- Mettl and interview questions
