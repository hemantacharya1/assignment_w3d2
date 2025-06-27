import os
from transformers import AutoTokenizer
from dotenv import load_dotenv

load_dotenv()

# Maps Ollama model names to compatible HF tokenizer IDs
TOKENIZER_MAP = {
    "llama2:7b": "NousResearch/Llama-2-7b-hf",
    "mistral:instruct": "NousResearch/Llama-2-7b-hf",
    "gemma2:2b": "google/gemma-2b-it"
}

tokenizer_cache = {}

def get_token_count(model_name: str, text: str) -> int:
    if model_name not in tokenizer_cache:
        tokenizer = AutoTokenizer.from_pretrained(
            TOKENIZER_MAP[model_name],
            token=os.getenv("HF_TOKEN"))
        tokenizer_cache[model_name] = tokenizer
    else:
        tokenizer = tokenizer_cache[model_name]

    tokens = tokenizer.encode(text, add_special_tokens=False)
    return len(tokens)
