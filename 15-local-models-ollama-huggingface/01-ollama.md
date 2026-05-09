# Ollama Basics

## 1. What It Is

Ollama is a tool for running local LLMs.

## 2. Why It Matters

It makes local model testing easier.

## 3. How It Works

Pull model:

```powershell
ollama pull llama3.1
```

- `ollama` runs Ollama CLI.
- `pull` downloads a model.
- `llama3.1` is the model name.

Where to run:

Run this in PowerShell after Ollama is installed.

Expected output:

```text
pulling manifest
pulling ...
success
```

How to verify:

```powershell
ollama list
```

Expected verification:

The model name should appear in the local model list.

Common error:

```text
ollama is not recognized
```

Meaning:

Ollama is not installed or the command is not available in PATH.

Run model:

```powershell
ollama run llama3.1
```

- `run` starts interactive model chat.

Command breakdown:

- `ollama` runs the local model CLI.
- `run` starts the selected model.
- `llama3.1` is the model to run.

Expected output:

Ollama opens an interactive prompt where you can type a message.

Example:

```text
>>> Explain RAG simply
```

How to verify:

If the model replies, local inference is working.

Common error:

If the model is not downloaded, Ollama may pull it first or show a model-not-found message.

## 4. How I Use It

Python can call Ollama HTTP API if the Ollama service is running.

## 5. Small Example

```python
import requests

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama3.1",
    "prompt": "Explain RAG simply",
    "stream": False
})
print(response.json()["response"])
```

## 6. Common Mistakes

- Ollama service not running.
- Model not pulled.
- Laptop too slow for selected model.

## 7. Beginner Deep Dive

Ollama is a local model runner. It lets your machine run supported models and expose them through a local interface.

Mental model:

```text
ollama pull -> model downloaded
ollama run -> model starts locally
Python request -> local Ollama service -> model response
```

Common beginner confusion:

- Pulling a model downloads it; it does not mean your Python app is already using it.
- Running a model starts an interactive/local model session.
- Local model quality and speed depend on hardware.
- If Ollama is not running, Python calls to it fail.

Where this appears in AI Engineer work:

- local model demos
- mock-to-local upgrade path
- privacy-aware labs
- hosted vs local model interview comparisons
