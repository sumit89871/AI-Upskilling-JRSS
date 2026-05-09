# GenAI, LLM, Prompt Engineering, and Agentic AI MCQs

## MCQ 1: LLM

Question:

What does an LLM mainly do?

Options:

A. Takes text input and generates text output  
B. Stores Docker images  
C. Creates Git branches  
D. Replaces all application code

Correct answer:

A. Takes text input and generates text output

Explanation:

An LLM predicts and generates text based on prompt input.

Common trap:

Thinking an LLM is the entire application. The application still handles APIs, validation, UI, RAG, tools, and security.

## MCQ 2: Prompt vs completion

Question:

What is a prompt?

Options:

A. Input instruction sent to the model  
B. Model output  
C. Docker command  
D. Kubernetes pod

Correct answer:

A. Input instruction sent to the model

Explanation:

The prompt is what you send. The completion or response is what the model returns.

Common trap:

Mixing up input and output terminology.

## MCQ 3: Token

Question:

Which statement is true?

Options:

A. A token is always exactly one word  
B. A token is a model text unit and may be part of a word  
C. A token is only an API key  
D. A token is a Docker container

Correct answer:

B. A token is a model text unit and may be part of a word

Explanation:

Models process tokens, not exact human words. One word may be one token or multiple tokens.

Common trap:

Estimating cost and limits only by word count.

## MCQ 4: Temperature

Question:

For strict JSON output, which temperature is usually safer?

Options:

A. Low temperature  
B. Very high temperature  
C. Temperature does not matter  
D. Temperature installs packages

Correct answer:

A. Low temperature

Explanation:

Low temperature makes output more consistent and less random.

Common trap:

Thinking higher temperature means smarter output. It means more randomness.

## MCQ 5: Hallucination

Question:

What is hallucination in LLM output?

Options:

A. Confident but wrong or unsupported output  
B. A successful API call  
C. A Docker build error  
D. A Git merge

Correct answer:

A. Confident but wrong or unsupported output

Explanation:

The model may invent facts when it lacks reliable context.

Common trap:

Trusting fluent output without checking sources.

## MCQ 6: Grounding

Question:

What does grounding mean?

Options:

A. Providing trusted context so the model answers based on it  
B. Running code locally only  
C. Creating a Git commit  
D. Deleting hallucinations automatically

Correct answer:

A. Providing trusted context so the model answers based on it

Explanation:

Grounding reduces hallucination risk by giving reliable source material.

Common trap:

Thinking grounding guarantees correctness. It reduces risk but does not eliminate review.

## MCQ 7: JSON prompt

Question:

If an app must parse model output, what should the prompt include?

Options:

A. Clear output schema and instruction to return valid JSON  
B. Only "be creative"  
C. No constraints  
D. Git branch name

Correct answer:

A. Clear output schema and instruction to return valid JSON

Explanation:

Structured output makes parsing and Pydantic validation easier.

Common trap:

Assuming "give JSON" is enough without schema or validation.

## MCQ 8: Chain-of-thought safety

Question:

What is a safer alternative to asking for hidden chain-of-thought?

Options:

A. Ask for final answer and concise reasoning summary  
B. Ask for no answer  
C. Ask for Docker logs  
D. Ask for full hidden reasoning only

Correct answer:

A. Ask for final answer and concise reasoning summary

Explanation:

Applications usually need user-facing explanation, not hidden internal reasoning.

Common trap:

Thinking long reasoning text proves correctness.

## MCQ 9: AI agent

Question:

What makes an AI agent different from a simple LLM call?

Options:

A. It can use workflow state, tools, decisions, or multi-step actions  
B. It is always a Kubernetes pod  
C. It never uses prompts  
D. It cannot call tools

Correct answer:

A. It can use workflow state, tools, decisions, or multi-step actions

Explanation:

An agent is an AI workflow that may decide actions, call tools, and manage state.

Common trap:

Calling every chatbot an agent. A simple prompt-response chatbot may not be agentic.

## MCQ 10: When not to use agents

Question:

When should you avoid agentic design?

Options:

A. When a simple deterministic function or one LLM call is enough  
B. Always use agents for every task  
C. Only when Python is installed  
D. When using JSON

Correct answer:

A. When a simple deterministic function or one LLM call is enough

Explanation:

Agents add complexity. Use them when workflow decisions, tools, retries, or state are needed.

Common trap:

Using agents because they sound advanced, not because they solve a real problem.
