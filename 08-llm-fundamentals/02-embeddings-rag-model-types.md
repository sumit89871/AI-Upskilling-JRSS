# Embeddings, RAG, and Model Types

## 1. What embeddings are

Embeddings are numeric representations of text meaning.

Simple meaning:

```text
embedding = text converted into a list of numbers that represents meaning
```

Example:

```python
embedding = [0.12, -0.44, 0.87, 0.05]
```

This list is simplified. Real embeddings usually have many more numbers.

Why numbers?

Computers compare numbers more easily than raw meaning. Embeddings let systems compare whether two pieces of text are semantically similar.

## 2. Embedding vs token

Tokens and embeddings are different.

| Concept | Meaning | Used for |
|---|---|---|
| Token | Small text unit processed by the model | generation and context limits |
| Embedding | Numeric vector representing meaning | search and similarity |

Token example:

```text
password reset -> password | reset
```

Embedding example:

```text
"password reset" -> [0.12, -0.44, 0.87, ...]
```

Common beginner mistake:

Thinking an embedding is the final answer. It is not. It is a numeric representation used for search.

## 3. Vector

A vector is a list of numbers.

Example:

```python
embedding = [0.12, -0.44, 0.87]
```

Syntax breakdown:

- `embedding` is a Python variable name.
- `=` assigns a value.
- `[]` creates a list.
- `0.12`, `-0.44`, and `0.87` are decimal numbers.
- commas separate list items.

In RAG, vectors represent text chunks and user questions.

## 4. Why embeddings matter

LLMs do not automatically know your private documents.

If a user asks:

```text
What is our login lockout rule?
```

The model may not know your project's rule.

Embeddings help your app search your documents by meaning and retrieve relevant context.

Example:

```text
question: "What happens after failed login attempts?"
retrieved chunk: "After 5 failed attempts, the account is locked for 15 minutes."
```

The words are different, but the meaning is related.

## 5. RAG

RAG means Retrieval Augmented Generation.

Simple meaning:

```text
RAG retrieves relevant information first, then gives it to the LLM to answer.
```

RAG mental model:

```text
Question -> retrieve context -> add context to prompt -> model answers using context
```

More detailed:

```text
Documents -> chunks -> embeddings -> vector database
User question -> question embedding -> similarity search -> relevant chunks
Relevant chunks + question -> prompt -> LLM answer
```

## 6. Why RAG exists

RAG exists because LLMs have limitations:

- they may not know private documents
- they may not know your latest project updates
- they may hallucinate when context is missing
- they cannot fit every document into every prompt
- they need grounding for enterprise answers

RAG gives the model relevant context at answer time.

## 7. RAG vs fine-tuning

RAG and fine-tuning solve different problems.

| Concept | What it does | Use when |
|---|---|---|
| RAG | Provides external context at answer time | answers depend on documents or latest knowledge |
| Fine-tuning | Adjusts model behavior through additional training | repeated style, format, or task behavior needs improvement |

Beginner rule:

Use RAG first for knowledge-based assistants.

Example:

If your QA assistant must answer from requirement notes, use RAG.

If the model always needs to write in a specific company-approved style and many examples are available, fine-tuning may be considered later.

## 8. Fine-tuning basics

Fine-tuning means training an existing model further on additional examples.

Simple meaning:

```text
fine-tuning = changing model behavior through extra training
```

Fine-tuning does not usually replace RAG for private knowledge.

Why:

- documents change often
- retraining can be expensive
- factual knowledge may become stale
- citations are harder than RAG

For beginner AI Engineer work, understand the concept, but usually build RAG first.

## 9. Grounding with RAG

Grounding means tying the answer to provided context.

RAG supports grounding by retrieving relevant text and placing it into the prompt.

Example prompt idea:

```text
Use only the context below to answer.

Context:
After 5 failed login attempts, the account is locked for 15 minutes.

Question:
What is the login lockout rule?
```

Expected answer:

```text
After 5 failed login attempts, the account is locked for 15 minutes.
```

This is better than asking the model without context.

## 10. Keyword search vs similarity search

Keyword search looks for exact or close word matches.

Similarity search looks for similar meaning using embeddings.

Example:

Question:

```text
How do users recover access?
```

Relevant document:

```text
Password reset is available from the login page.
```

Keyword search may miss this because the exact words differ.

Similarity search may find it because the meaning is related.

## 11. Hosted model

A hosted model runs on a provider's infrastructure and is accessed through an API.

Examples:

- OpenAI API
- Gemini API
- watsonx API
- other cloud model endpoints

Beginner meaning:

```text
hosted model = model runs elsewhere, your app calls it over network
```

Pros:

- no local GPU required
- usually strong models
- easier to start
- provider manages infrastructure

Cons:

- API cost
- network dependency
- data privacy review needed
- rate limits
- provider-specific SDK/API behavior

## 12. Local model

A local model runs on your own machine or local server.

Examples:

- Ollama running a local model
- Hugging Face model loaded locally
- local inference server

Beginner meaning:

```text
local model = model runs on your hardware
```

Pros:

- can work offline after setup
- more control over runtime
- useful for demos and privacy-sensitive experiments

Cons:

- weaker model may produce lower quality
- needs RAM/VRAM/CPU resources
- slower on normal laptops
- setup can be harder

## 13. Hosted model vs local model

| Concept | Hosted model | Local model |
|---|---|---|
| Runs where | Provider infrastructure | Your machine/server |
| Needs internet | Usually yes | Not after setup |
| Hardware burden | Provider handles it | You handle it |
| Cost | API usage cost | hardware/time cost |
| Privacy | needs provider review | more local control |
| Quality | often stronger | depends on model/hardware |

Use hosted models when you need quality and quick setup.

Use local models when privacy, offline demos, or local experimentation matters.

## 14. Open model

An open model usually means model weights or usage rights are more accessible than closed commercial models.

Examples may include models from open model ecosystems.

Practical meaning:

```text
open model = easier to run, inspect, or adapt locally depending on license
```

Important:

"Open" does not always mean fully unrestricted. Always check the license before commercial or enterprise use.

## 15. Closed model

A closed model is usually accessed through a provider API, and the model weights are not publicly available.

Examples:

- many commercial hosted models

Practical meaning:

```text
closed model = you use the model through provider-controlled access
```

Pros:

- strong quality
- managed infrastructure
- easy API integration

Cons:

- less internal visibility
- provider dependency
- data governance review needed
- pricing and limits

## 16. Open model vs closed model

| Concept | Open model | Closed model |
|---|---|---|
| Access | often downloadable or locally runnable | usually API only |
| Control | more control | less control |
| Setup | may require local infrastructure | easier API call |
| Quality | varies | often high |
| License | must check carefully | provider terms |

Beginner mistake:

Thinking open model always means free for any use. License still matters.

## 17. Foundation model

A foundation model is a broadly trained model that can support many tasks.

Example tasks:

- chat
- summarization
- code help
- classification
- extraction
- test case generation

Practical meaning:

```text
foundation model = general base model used as the engine for many AI apps
```

Your final POC will likely use a foundation model through API or local runtime.

## 18. MoE basics

MoE means Mixture of Experts.

Simple meaning:

```text
MoE = architecture where selected expert parts of the model are used for each input
```

Analogy:

A supervisor routes different tasks to different specialists.

Why it matters:

MoE is one way modern models scale efficiently. For this course, you only need awareness, not implementation.

## 19. Model type choice in final POC

For the final POC, a practical setup is:

```text
mock LLM first -> optional hosted model -> optional local model
```

Why mock first:

- no API key needed
- easy demo
- predictable output
- beginner-friendly debugging

Why optional hosted model:

- better generation quality
- realistic API integration

Why optional local model:

- useful for privacy/offline awareness
- demonstrates local AI capability

## 20. Common mistakes

- Confusing embedding with final answer.
- Thinking RAG permanently trains the model.
- Using RAG with low-quality or irrelevant chunks.
- Thinking fine-tuning is always better than RAG.
- Assuming local model means no privacy risk if the app still sends data elsewhere.
- Thinking hosted model means no validation is needed.
- Treating open model licenses casually.

## 21. Where used in AI Engineer work

Embeddings appear in:

- vector search
- RAG retrieval
- ChromaDB and FAISS examples

RAG appears in:

- knowledge assistants
- final POC
- enterprise document QA
- hallucination control

Model type decisions appear in:

- OpenAI/Gemini API integration
- Ollama/local model labs
- Hugging Face awareness
- enterprise architecture discussion
- interview tradeoff questions
