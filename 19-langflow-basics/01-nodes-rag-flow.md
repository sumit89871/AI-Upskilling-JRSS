# Nodes and RAG Flow

## Node

A node is one block in a visual workflow.

Example nodes:

- text input node
- prompt node
- LLM node
- document loader node
- embedding node
- vector store node
- retriever node
- output node

## Edge

An edge connects the output of one node to the input of another node.

Example:

```text
Prompt node -> LLM node
```

## Prompt node

What it does:

Holds the instruction template.

Example:

```text
Answer the question using this context:
{context}
Question: {question}
```

Common mistake:

Putting document text and question together without labels.

## LLM node

What it does:

Sends the prompt to a model and returns generated text.

Common mistake:

Thinking the LLM node automatically knows your documents.

## Retriever node

What it does:

Finds relevant chunks from a vector store.

RAG flow:

```text
Question -> retriever -> relevant chunks -> prompt -> LLM -> answer
```

## Where Langflow fits

Langflow is good for seeing how components connect. Once the flow is stable, an AI Engineer may implement the production version in Python with FastAPI, LangChain, or LangGraph.
