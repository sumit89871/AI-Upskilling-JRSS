# Local Models Exercises

## Exercise 1: Explain local vs hosted

Task:

Compare local and hosted models.

Expected answer:

Hosted models run on provider infrastructure through API. Local models run on your machine or server.

Hint:

Compare cost, privacy, quality, and hardware.

Self-check:

Does local always mean better quality?

Common mistake:

Assuming local automatically means production-ready.

## Exercise 2: Ollama command explanation

Task:

Explain this command:

```powershell
ollama pull llama3
```

Expected answer:

- `ollama` runs the Ollama CLI.
- `pull` downloads a model.
- `llama3` is the model name.

Expected result:

Model files are downloaded locally if the model is available.

Common mistake:

Running pull without enough disk space or internet.

## Exercise 3: Run local model

Task:

Explain:

```powershell
ollama run llama3
```

Expected answer:

It starts an interactive local chat with the model.

Expected output style:

Ollama opens a prompt where you can type a question.

Common mistake:

Expecting hosted API quality from a small local model on a weak laptop.

## Exercise 4: Hugging Face model card

Task:

Open a model card and identify:

- model purpose
- license
- input/output type
- hardware notes

Expected answer:

A model card explains how the model should be used and what limits apply.

Common mistake:

Ignoring license and hardware requirements.
