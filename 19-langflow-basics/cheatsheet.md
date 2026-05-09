# Langflow Cheatsheet

## Node

Meaning: One component in a visual flow.

Use when: Building a pipeline block.

Example: Prompt node, LLM node, Retriever node.

Be careful: Node name does not explain all behavior; understand its input/output.

## Edge

Meaning: Connection from one node to another.

Use when: Passing data through the flow.

Example: Retriever -> Prompt.

Be careful: Wrong edge means wrong data goes to next step.

## RAG Flow

Meaning: Retrieve context before generation.

Use when: Answer must come from documents.

Example: Question -> Retriever -> Prompt -> LLM.

Be careful: RAG requires useful documents and retrieval.

## Limitation

Meaning: Visual flow is not always production-ready.

Use when: Explaining prototype tradeoffs.

Be careful: Production still needs code, testing, security, and deployment.
