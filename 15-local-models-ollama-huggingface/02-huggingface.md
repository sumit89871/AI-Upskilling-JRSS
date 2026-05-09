# Hugging Face Basics

## 1. What It Is

Hugging Face is a model hub and tooling ecosystem.

## 2. Why It Matters

Many open models, tokenizers, datasets, and demos are hosted there.

## 3. How It Works

Pipeline concept:

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print(classifier("This app is useful"))
```

## 4. Syntax Breakdown

- `pipeline` creates a ready-to-use ML task wrapper.
- `"sentiment-analysis"` is the task name.

## 5. Tokenizer

A tokenizer converts text into model tokens.

## 6. vLLM Awareness

vLLM is used for efficient model serving, usually beyond beginner laptop setup.

## 7. Common Mistakes

- Installing heavy packages without checking hardware.
- Using models without checking license.

## 8. Beginner Deep Dive

Hugging Face is a model ecosystem, not one model.

Mental model:

```text
model hub -> model card -> tokenizer/model files -> pipeline or custom code -> output
```

Always check the model card before using a model. It usually explains intended use, limits, license, and examples.

Common beginner confusion:

- Tokenizer is not the model.
- Pipeline is a helper interface, not the only way to use a model.
- Downloading a model does not guarantee your laptop can run it.
- Open availability does not always mean unrestricted enterprise use.

Where this appears in AI Engineer work:

- local model awareness
- tokenizer explanation
- model selection
- license and hardware discussions
