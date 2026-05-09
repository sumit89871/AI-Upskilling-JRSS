# Local Models Cheatsheet

## ollama pull

Command: `ollama pull llama3`

Meaning: Download a model locally.

Use when: You want to run a model with Ollama.

Be careful: Needs internet, disk space, and supported model name.

## ollama run

Command: `ollama run llama3`

Meaning: Start local model interaction.

Use when: Testing prompts locally.

Be careful: Local speed depends on hardware.

## Hugging Face Hub

Meaning: Online hub for models, datasets, and model cards.

Use when: Finding open models or checking model details.

Be careful: Always check license and intended use.

## Tokenizer

Meaning: Splits text into model tokens.

Use when: Understanding input length and model processing.

Be careful: Different models may use different tokenizers.

## Pipeline

Meaning: Simple Hugging Face helper for running a model task.

Use when: Trying tasks such as text generation or classification.

Be careful: Pipelines may download large files.
