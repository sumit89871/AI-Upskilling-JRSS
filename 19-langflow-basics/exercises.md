# Langflow Exercises

## Exercise 1: Design a simple prompt flow

Task:

Draw this flow in text:

```text
User input -> prompt -> LLM -> output
```

Expected answer:

```text
Text Input Node -> Prompt Node -> LLM Node -> Output Node
```

Hint:

Each node has one responsibility.

Self-check:

Can you explain what the prompt node adds?

Common mistake:

Saying the LLM node is responsible for retrieving documents.

## Exercise 2: Design a RAG flow

Task:

List the nodes needed for RAG.

Expected answer:

```text
Document Loader -> Text Splitter -> Embedding Node -> Vector Store -> Retriever -> Prompt -> LLM -> Output
```

Hint:

RAG needs retrieval before generation.

Self-check:

Which node finds relevant chunks?

Common mistake:

Skipping the retriever and calling it RAG.

## Exercise 3: Prototype vs production

Task:

Explain why a visual flow may need to be converted into code for production.

Expected answer:

Production needs testing, logging, security, deployment, version control, and custom error handling.

Common mistake:

Assuming a visual prototype is automatically production-ready.
