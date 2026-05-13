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

## MCQ 11: A2A

Question:

What does A2A mean in agentic AI discussions?

Options:

A. Agent-to-agent communication
B. API-to-API billing
C. Automatic Docker deployment
D. A Python data type

Correct answer:

A. Agent-to-agent communication

Explanation:

A2A describes agents communicating, requesting help, or handing work to each other in a multi-agent system.

Why other options are wrong:

B is unrelated to agent collaboration. C belongs to deployment. D belongs to programming basics.

Common trap:

Confusing A2A with MCP. MCP connects AI clients to tools/resources/prompts. A2A is about agents communicating with agents.

## MCQ 12: A2A vs supervisor pattern

Question:

Which statement is most accurate?

Options:

A. A supervisor pattern uses one controller to route agents; A2A focuses on agent communication
B. A2A means Kubernetes service discovery
C. A supervisor pattern is a Dockerfile command
D. A2A means an LLM cannot use tools

Correct answer:

A. A supervisor pattern uses one controller to route agents; A2A focuses on agent communication

Explanation:

Both can appear in multi-agent design. A supervisor is a controlled router. A2A is a communication or handoff concept between agents.

Common trap:

Thinking all multi-agent patterns are the same.

## MCQ 13: Agentic Studio awareness

Question:

If asked about Agent Studio or Agentic Studio and you do not have official internal details, what is the safest answer?

Options:

A. Explain it as enterprise agent-building awareness and say exact details should be validated from official resources
B. Invent detailed internal features
C. Say it is definitely the same as Docker
D. Say it replaces Python

Correct answer:

A. Explain it as enterprise agent-building awareness and say exact details should be validated from official resources

Explanation:

For internal or platform-specific terms, avoid guessing. Connect the term to enterprise agent tooling and official validation.

Common trap:

Overclaiming platform knowledge without documentation.

## MCQ 14: Certification-safe wording

Question:

What should you say about a credential or badge you have not completed yet?

Options:

A. "I am preparing for it and will only claim it after completion."
B. "I am certified" even without completion
C. "Credentials never matter"
D. "A badge is the same as a Docker image"

Correct answer:

A. "I am preparing for it and will only claim it after completion."

Explanation:

Honest wording matters in enterprise interviews. You can discuss preparation and skills without claiming a credential you do not hold.

Common trap:

Confusing awareness with completed certification.

## MCQ 15: IBM BOB awareness

Question:

If a screening question asks about IBM BOB and you only know it from the program PPT, what is the safest answer?

Options:

A. Acknowledge it as an IBM ecosystem item from program material and avoid inventing internal details
B. Invent exact product features confidently
C. Say it is a Python keyword
D. Say it is the same as Kubernetes

Correct answer:

A. Acknowledge it as an IBM ecosystem item from program material and avoid inventing internal details

Explanation:

Some organization-specific terms may require awareness rather than deep public technical explanation. A safe answer shows you recognized the term and understand that exact internal usage should come from official IBM resources.

Why other options are wrong:

B is risky because it invents unsupported details. C and D are wrong domains.

Common trap:

Overclaiming internal platform knowledge instead of giving a careful enterprise-aware answer.
