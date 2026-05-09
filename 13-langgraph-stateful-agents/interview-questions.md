# LangGraph Interview Questions

Use these answers for AI Engineer JRSS screening, POC explanation, and technical interviews.

## 1. What is LangGraph?

Short answer:

LangGraph is a framework for building controlled, stateful LLM and agent workflows using graphs, nodes, edges, and state.

Expanded answer:

LangGraph helps structure multi-step AI workflows. Instead of calling functions randomly, you define a graph. The graph contains nodes for workflow steps, edges for routing, and state for shared data. This is useful for agent systems that need branching, retries, review, checkpointing, or human approval.

Project example:

In the final QA assistant POC, LangGraph can control this flow:

```text
understand query -> retrieve context -> generate test cases -> review -> final response
```

Common wrong answer:

"LangGraph is just an LLM."

Why this is wrong:

LangGraph does not generate text by itself. It controls the workflow around LLM calls, tools, retrieval, and review.

## 2. Why use LangGraph instead of a simple function chain?

Short answer:

Use LangGraph when the workflow needs state, branching, retries, checkpointing, or human approval.

Expanded answer:

A simple function chain is fine when every step always runs in the same order. LangGraph is useful when the next step depends on state or when the workflow needs to pause, retry, branch, or resume.

Project example:

If generated test cases fail review, the graph can route back to a revise node instead of returning weak output.

Common wrong answer:

"LangGraph is always better than functions."

Why this is wrong:

For one-step tasks, a normal function or simple script is easier and better.

## 3. What is state in LangGraph?

Short answer:

State is the shared data passed through the workflow.

Expanded answer:

Each node reads from state and writes updates back to state. State may contain the user question, retrieved context, draft answer, review status, and final output.

Project example:

```python
state = {
    "question": "What are login rules?",
    "retrieved_context": [],
    "draft_answer": None,
    "final_answer": None,
}
```

Common wrong answer:

"State is just a variable inside one function."

Why this is wrong:

A local variable may disappear when a function ends. State is passed across workflow steps.

## 4. What is a node?

Short answer:

A node is one workflow step, often implemented as a Python function.

Expanded answer:

A node receives state, performs one responsibility, updates state, and returns state. Good nodes have clear names such as `retrieve_context`, `generate_answer`, or `review_output`.

Project example:

```python
def generate_scenarios(state: dict) -> dict:
    state["scenarios"] = ["valid case", "invalid case"]
    return state
```

Common wrong answer:

"A node is only a function."

Why this is incomplete:

A node may be implemented as a function, but in graph terminology it means a workflow step.

## 5. What is an edge?

Short answer:

An edge connects one node to the next node.

Expanded answer:

Edges define workflow order. A simple edge always moves from one node to another. A conditional edge chooses the next node based on state.

Project example:

```text
retrieve_context -> generate_answer
```

Common wrong answer:

"An edge performs the work."

Why this is wrong:

Nodes perform work. Edges define where the workflow goes next.

## 6. What is a conditional edge?

Short answer:

A conditional edge chooses the next node based on state.

Expanded answer:

Conditional edges are useful when the workflow can branch. For example, after review, the workflow may go to `final` if approved or `revise` if changes are needed.

Project example:

```python
def route_after_review(state: dict) -> str:
    if state["review_status"] == "approved":
        return "final"
    return "revise"
```

Common wrong answer:

"Conditional edge means running both paths."

Why this is wrong:

A conditional edge selects a route. It does not automatically run every possible route.

## 7. What is checkpointing?

Short answer:

Checkpointing saves workflow state so execution can resume or be inspected later.

Expanded answer:

Checkpoints are useful for long-running workflows, expensive retrieval, human approval, or failure recovery. If a later step fails, the graph may resume from saved progress instead of starting again.

Project example:

Save state after retrieving context. If LLM generation fails, reuse the retrieved context instead of repeating retrieval.

Common wrong answer:

"Checkpointing is the final output."

Why this is wrong:

A checkpoint is saved progress. The final output is what the user receives.

## 8. What is a reducer?

Short answer:

A reducer decides how state updates are combined.

Expanded answer:

Reducers are useful when multiple nodes update the same field. For example, if multiple nodes add messages, a reducer can append new messages instead of replacing the old list.

Project example:

```text
old messages ["analyzed"] + new messages ["generated"] -> ["analyzed", "generated"]
```

Common wrong answer:

"Reducer is another name for a node."

Why this is wrong:

A node performs work. A reducer controls how state updates are merged.

## 9. What does compile mean in LangGraph?

Short answer:

Compile means preparing the graph definition so it can run.

Expanded answer:

After defining state, nodes, and edges, the graph is compiled into a runnable object. This step checks and prepares the workflow structure.

Project example:

```python
app = graph.compile()
```

Common wrong answer:

"Compile means training the LLM."

Why this is wrong:

Compile prepares the workflow graph. It does not train a model.

## 10. What does invoke mean in LangGraph?

Short answer:

Invoke means running the compiled graph with input state.

Expanded answer:

Once the graph is compiled, you invoke it by passing initial state. The graph runs nodes according to edges and returns the result.

Project example:

```python
result = app.invoke({"requirement": "User can login"})
```

Common wrong answer:

"Invoke means importing the graph."

Why this is wrong:

Importing loads code. Invoking runs the graph.

## 11. What is the difference between state and memory?

Short answer:

State is workflow data during execution. Memory usually means stored information across sessions or conversations.

Expanded answer:

State moves through nodes in one workflow run. Memory may persist beyond one run, such as user preferences or conversation history.

Project example:

State may contain `draft_answer` for the current question. Memory may contain user profile preferences across conversations.

Common wrong answer:

"State and memory are always the same."

Why this is wrong:

They can overlap in some systems, but they are not the same concept.

## 12. What is a retry node?

Short answer:

A retry node or retry route handles temporary failure by trying a step again.

Expanded answer:

Retry is useful for timeouts, rate limits, or temporary provider errors. It should not be used forever, and it should not hide permanent problems such as invalid input or broken state keys.

Project example:

If an LLM API call times out, route to a retry node up to two times before returning an error.

Common wrong answer:

"Retry should fix every error."

Why this is wrong:

Retry only helps temporary failures. It will not fix bad code or missing required state.

## 13. What is a human approval node?

Short answer:

A human approval node pauses the workflow for a person to review before continuing.

Expanded answer:

This is useful when AI output affects important decisions or stakeholder-facing deliverables. It adds control and accountability.

Project example:

Generated test cases can be reviewed by a QA lead before being exported or shared.

Common wrong answer:

"Human approval means the AI failed."

Why this is wrong:

Human approval is a safety and governance step, not necessarily a failure.

## 14. What is the supervisor pattern?

Short answer:

A supervisor pattern uses a controller to route work to specialized agents or workers.

Expanded answer:

The supervisor decides which worker should handle the next task. This is useful in multi-agent workflows where different agents have different responsibilities.

Project example:

```text
Supervisor -> Requirement Analyst
Supervisor -> Test Case Generator
Supervisor -> Reviewer
```

Common wrong answer:

"Supervisor means one agent does all the work."

Why this is wrong:

The supervisor routes or coordinates work. Specialized workers do the actual tasks.

## 15. How would you explain LangGraph in your POC?

Short answer:

I used LangGraph-style workflow control to move state through requirement analysis, retrieval, generation, review, and final response.

Expanded answer:

The POC is not just a single prompt. It has multiple steps. State carries the user query, retrieved context, draft output, review result, and final response. Each node performs one responsibility. Edges define the order, and conditional routing can send weak output back for revision.

Project example:

```text
User asks question
State stores question
Retrieve node adds context
Generate node creates draft answer
Review node checks quality
Final node returns structured response
```

Common wrong answer:

"I used LangGraph because it is popular."

Why this is weak:

The better answer explains the practical need: controlled stateful workflow, branching, review, and production-readiness.
