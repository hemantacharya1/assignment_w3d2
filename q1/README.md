# 🧠 LLM Comparison CLI

This is a command-line tool that allows users to compare **Base**, **Instruct**, and **Fine-tuned** models from different providers using **locally running LLMs via Ollama**.

## 📦 Features

- Compare outputs of models like `llama2`, `mistral:instruct`, and `gemma:2`
- View model metadata: parameter size, instruction-following ability, context window, etc.
- See actual token usage using Hugging Face tokenizers
- Run fully locally (no OpenAI/Anthropic API keys required)
- Easily extendable

---

## 🚀 Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install transformers sentencepiece python-dotenv
```

### 2. Install & run Ollama models

Make sure you have Ollama installed and running.

```bash
ollama run llama2
ollama run mistral:instruct
ollama run gemma:2
```

### 3. Create .env file (optional if using gated models)

```env
HF_TOKEN=your_huggingface_token_here  # only needed if accessing gated models
```

### 4. Run the CLI tool

```bash
python main.py --prompt "Explain blackhole to a 5yr old"
```

## 📁 Project Structure

```
llm-comparator/
├── main.py                  # CLI entry point
├── models/
│   └── ollama_runner.py     # Runs local LLMs via Ollama
├── utils/
│   └── token_counter.py     # Counts tokens using HF tokenizers
├── comparisons.md           # Summary table of 5 prompts (your task)
├── .env.example             # Sample env file
└── README.md
```

## ✅ Supported Models

| Model | Type | Parameters | Context Size | Instruction Following |
|-------|------|------------|--------------|----------------------|
| llama2 | Base | 7B | 4096 tokens | ❌ No |
| mistral:instruct | Instruct | 7B | 8192 tokens | ✅ Yes |
| gemma:2 | Fine-tuned | 2B | 8192 tokens | ✅ Partial |

## 🔓 License

MIT License

---