import argparse
from models.ollama_runner import run_ollama_model
from models.token_counter import get_token_count

# Predefined model list
MODEL_LIST = {
    "base": "llama2:7b",
    "instruct": "mistral:instruct",
    "fine-tuned": "gemma2:2b"
}
# Static info for model comparison
MODEL_METADATA = {
    "llama2:7b": {
        "type": "Base",
        "context_window": "4096 tokens",
        "parameters": "7B",
        "instruction_following": "❌ No",
    },
    "mistral:instruct": {
        "type": "Instruct",
        "context_window": "8192 tokens",
        "parameters": "7B",
        "instruction_following": "✅ Yes",
    },
    "gemma2:2b": {
        "type": "Fine-tuned",
        "context_window": "8192 tokens",
        "parameters": "2B",
        "instruction_following": "✅ Yes (partially)",
    }
}


def compare_models(prompt: str):
    results = {}
    for model_type, model_name in MODEL_LIST.items():
        print(f"\n🔄 Running prompt on {model_type.upper()} model: {model_name}")
        output = run_ollama_model(model_name, prompt)
        total_tokens = get_token_count(model_name, prompt + output)
        results[model_type] = output
        # Print summary:
        print(f"\n🧠 {model_type.capitalize()} Model Summary")
        print("-" * 40)
        meta = MODEL_METADATA[model_name]
        print(f"🔹 Model Name: {model_name}")
        print(f"🔸 Type: {meta['type']}")
        print(f"🔸 Context Window: {meta['context_window']}")
        print(f"🔸 Parameters: {meta['parameters']}")
        print(f"🔸 Instruction Following: {meta['instruction_following']}")
        print(f"🔸 Actual Tokens Used: {total_tokens}")
        print("-" * 40)
        print(f"🧾 Output:\n{output}")
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare LLM model types using Ollama")
    parser.add_argument("--prompt", type=str, required=True, help="Prompt to run")
    args = parser.parse_args()

    compare_models(args.prompt)
