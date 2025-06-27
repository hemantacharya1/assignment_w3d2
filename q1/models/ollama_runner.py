import subprocess

def run_ollama_model(model_name: str, prompt: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", model_name],
            input=prompt.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=8000
        )
        output = result.stdout.decode("utf-8")
        return output
    except Exception as e:
        return f"[ERROR running {model_name}]: {str(e)}"
