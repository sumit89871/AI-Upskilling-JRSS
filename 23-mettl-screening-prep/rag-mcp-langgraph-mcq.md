# RAG, MCP, and LangGraph MCQs

## MCQ 1: RAG meaning

Question:

What does RAG stand for?

Options:

A. Retrieval Augmented Generation  
B. Runtime API Gateway  
C. Remote Agent Graph  
D. Random Answer Generator

Correct answer:

A. Retrieval Augmented Generation

Explanation:

RAG retrieves relevant context before asking the model to generate an answer.

Common trap:

Thinking RAG means the model is permanently trained on documents.

## MCQ 2: RAG flow

Question:

Which flow best describes RAG?

Options:

A. Question -> retrieve context -> add context to prompt -> model answers  
B. Question -> Docker build -> Git push  
C. Question -> model guesses without context  
D. Question -> Kubernetes service only

Correct answer:

A. Question -> retrieve context -> add context to prompt -> model answers

Explanation:

RAG grounds the answer using retrieved context.

Common trap:

Skipping retrieval and calling it RAG anyway.

## MCQ 3: Embedding

Question:

What is an embedding?

Options:

A. Numeric vector representing text meaning  
B. Final LLM answer  
C. Git commit hash  
D. HTTP status code

Correct answer:

A. Numeric vector representing text meaning

Explanation:

Embeddings are used for similarity search in vector databases.

Common trap:

Thinking embedding is human-readable output.

## MCQ 4: Vector database

Question:

What is a vector database used for in RAG?

Options:

A. Store and search embeddings by similarity  
B. Run FastAPI routes  
C. Replace Python functions  
D. Create Docker images

Correct answer:

A. Store and search embeddings by similarity

Explanation:

Vector databases help find document chunks similar to a user question.

Common trap:

Confusing vector search with exact keyword search.

## MCQ 5: MCP meaning

Question:

What is MCP used for?

Options:

A. Connecting AI clients to tools, resources, and prompts through a standard protocol  
B. Building Docker images only  
C. Formatting Python code  
D. Replacing all APIs

Correct answer:

A. Connecting AI clients to tools, resources, and prompts through a standard protocol

Explanation:

MCP helps AI systems discover and call external capabilities.

Common trap:

Thinking MCP is the LLM itself.

## MCQ 6: MCP tool

Question:

What is an MCP tool?

Options:

A. A callable action exposed by an MCP server  
B. A static document only  
C. A Kubernetes pod  
D. A Git branch

Correct answer:

A. A callable action exposed by an MCP server

Explanation:

Tools usually map to functions that can perform actions, such as fetching test data.

Common trap:

Confusing tool with resource. A resource is read-only context; a tool performs an action.

## MCQ 7: MCP server vs client

Question:

Which statement is correct?

Options:

A. MCP server exposes tools; MCP client discovers and calls them  
B. MCP client exposes Dockerfiles  
C. MCP server is always the LLM  
D. MCP has no tools

Correct answer:

A. MCP server exposes tools; MCP client discovers and calls them

Explanation:

The server provides capabilities. The client uses them.

Common trap:

Reversing server and client responsibilities.

## MCQ 8: LangGraph state

Question:

What is state in LangGraph?

Options:

A. Shared data passed through workflow nodes  
B. A Docker image  
C. A Git tag  
D. A CSS style

Correct answer:

A. Shared data passed through workflow nodes

Explanation:

Nodes read from state and write updates back to state.

Common trap:

Thinking state is only a local variable inside one function.

## MCQ 9: LangGraph node

Question:

What is a node in LangGraph?

Options:

A. One workflow step, often implemented as a function  
B. A Kubernetes node only  
C. A database column  
D. An API key

Correct answer:

A. One workflow step, often implemented as a function

Explanation:

Nodes perform work such as retrieve context, generate answer, or review output.

Common trap:

Confusing LangGraph node with Kubernetes node.

## MCQ 10: Conditional edge

Question:

What does a conditional edge do?

Options:

A. Chooses the next node based on state  
B. Deletes the graph  
C. Installs Pydantic  
D. Builds an image

Correct answer:

A. Chooses the next node based on state

Explanation:

Conditional edges support branching, such as review passed -> final, review failed -> revise.

Common trap:

Thinking conditional edge runs every possible path.

## MCQ 11: Checkpoint

Question:

What is checkpointing in LangGraph-style workflows?

Options:

A. Saving workflow state so execution can resume or be inspected  
B. Deleting state  
C. Creating a prompt only  
D. Running kubectl

Correct answer:

A. Saving workflow state so execution can resume or be inspected

Explanation:

Checkpoints help debug and resume long workflows.

Common trap:

Thinking checkpoint is the final answer. It is saved progress.

## MCQ 12: RAG vs fine-tuning

Question:

Which statement is best?

Options:

A. RAG provides context at answer time; fine-tuning changes model behavior through training  
B. RAG and fine-tuning are identical  
C. RAG means Docker deployment  
D. Fine-tuning is always required for private documents

Correct answer:

A. RAG provides context at answer time; fine-tuning changes model behavior through training

Explanation:

For changing documents and knowledge assistants, RAG is usually the first practical approach.

Common trap:

Choosing fine-tuning first when the real need is document-grounded answers.
