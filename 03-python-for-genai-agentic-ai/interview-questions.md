# Python For GenAI Interview Questions

## 1. Why is Python popular for GenAI?

Python is readable, has strong AI/ML libraries, has good API tooling, and is widely supported by GenAI frameworks.

## 2. What is structured output?

Structured output is model output shaped in a predictable format such as JSON. It is easier to validate, parse, display, and pass to another step.

## 3. Why do agents need state?

Agents perform multiple steps. State stores the user goal, intermediate results, tool outputs, errors, and final answer.

## 4. What is a tool in agentic AI?

A tool is usually a normal function exposed to an AI system so the model or workflow can request an action such as lookup, calculation, file search, or API call.

## 5. What is the difference between a tool and an LLM?

An LLM generates or reasons over text. A tool performs a specific operation using code or an external system.

## 6. Why use a mock LLM first?

Mock mode allows the app structure, API, UI, state flow, and tests to work without paid keys, network dependency, or model variability.

## 7. What is retry logic?

Retry logic repeats an operation after temporary failure. It should have a limit and should not retry invalid input forever.

## 8. What should not be logged?

Secrets, API keys, passwords, private user data, and sensitive business data should not be logged.

## 9. What is `async` used for?

`async` is used for operations that wait, such as API calls or streaming, so the app can handle work more efficiently.

## 10. What is streaming?

Streaming receives output piece by piece instead of waiting for the full response. It improves user experience in chat-style apps.

## 11. What is a prompt template?

A prompt template is reusable prompt text with placeholders filled at runtime.

## 12. What is a common agent loop mistake?

Not having a clear stop condition or max step count, which can cause infinite loops or high API cost.

