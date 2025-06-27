# 📊 LLM Model Output Comparison

This document compares responses from 3 model types — **Base**, **Instruct**, and **Fine-tuned** — for a set of diverse prompts using locally-run LLMs via Ollama.

---

### ✅ Prompt 1: "Explain blackhole to a 5yr old"

| Model            | Tokens Used | Output Summary |
|------------------|-------------|----------------|
| llama2 (Base)    | 309         | Long, imaginative, but less focused. Uses storytelling tone. |
| mistral (Instruct) | 182       | Precise, clear analogy with toys. Very age-appropriate. |
| gemma:2 (Fine-tuned) | 163     | Concise and friendly with emojis. Slightly less detailed. |

**Best for this prompt:** `mistral:instruct` – most age-appropriate and well-aligned.

---

### ✅ Prompt 2: "Write a breakup message that's gentle but honest"

| Model            | Tokens Used | Output Summary |
|------------------|-------------|----------------|
| llama2           | 287         | Slightly rambling and poetic, lacks directness. |
| mistral:instruct | 198         | Kind and balanced, directly communicates the message. |
| gemma:2          | 174         | Very short, generic, a bit emotionally flat. |

**Best for this prompt:** `mistral:instruct` – best balance of honesty and tone.

---

### ✅ Prompt 3: "Summarize the plot of Inception in one paragraph"

| Model            | Tokens Used | Output Summary |
|------------------|-------------|----------------|
| llama2           | 241         | Vague and overly abstract. Uses general phrases. |
| mistral:instruct | 206         | Accurate, includes dream layers and mission details. |
| gemma:2          | 179         | Acceptable summary but missed key concepts. |

**Best for this prompt:** `mistral:instruct` – nails the key plot points clearly.

---

### ✅ Prompt 4: "What are the pros and cons of electric cars?"

| Model            | Tokens Used | Output Summary |
|------------------|-------------|----------------|
| llama2           | 315         | Lists generic info with little structure or logic. |
| mistral:instruct | 232         | Clear point-by-point list. Balanced pros/cons. |
| gemma:2          | 193         | Short list, but misses depth and specifics. |

**Best for this prompt:** `mistral:instruct` – most informative and logically structured.

---

### ✅ Prompt 5: "Translate: 'The cat sat on the mat' into French"

| Model            | Tokens Used | Output Summary |
|------------------|-------------|----------------|
| llama2           | 44          | Translation: "Le chat s'est assis sur le tapis" ✅ |
| mistral:instruct | 36          | Correct translation, simple and clear ✅ |
| gemma:2          | 35          | Correct but returned extra explanation 📄 |

**Best for this prompt:** Tie between `llama2` and `mistral`.

---

## 📌 Observations

- **Instruct models** (like Mistral) consistently give the most aligned and usable outputs for tasks like explanation, reasoning, and polite communication.
- **Base models** (like LLaMA2) are verbose, creative, but often miss the intent without explicit instruction.
- **Fine-tuned small models** (like Gemma-2B) are decent but struggle with longer or structured outputs.

---