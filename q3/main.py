import os
import re
import google.generativeai as genai
from dotenv import load_dotenv
from tools import math_tools, string_tools

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

# Tool function mapping
TOOL_FUNCTIONS = {
    "average": math_tools.average,
    "square_root": math_tools.square_root,
    "count_vowels": string_tools.count_vowels,
    "string_length": string_tools.string_length
}

def extract_tool_calls(text: str):
    pattern = r"\[TOOL:\s*(\w+)\((.*?)\)\]"
    matches = re.findall(pattern, text)
    tool_calls = []
    for func_name, args_str in matches:
        args = {}
        for pair in args_str.split(","):
            if not pair.strip():
                continue
            k, v = pair.split("=")
            k = k.strip()
            v = v.strip().strip("'\"")
            if v.replace('.', '', 1).isdigit():
                v = float(v) if '.' in v else int(v)
            args[k] = v
        tool_calls.append((func_name, args))
    return tool_calls

def call_tools(tool_calls):
    results = {}
    for func_name, args in tool_calls:
        func = TOOL_FUNCTIONS.get(func_name)
        if func:
            try:
                result = func(**args)
                results[func_name] = result
            except Exception as e:
                results[func_name] = f"Error: {str(e)}"
        else:
            results[func_name] = "Unknown function"
    return results

def load_prompt_template():
    with open("prompts/reasoning_prompt.txt") as f:
        return f.read()

def main():
    query = input("Enter your query: ")
    template = load_prompt_template()
    prompt = template.format(query=query)

    response = model.generate_content(prompt)
    reasoning_text = response.text.strip()

    print("\n--- LLM Reasoning ---")
    print(reasoning_text)

    tool_calls = extract_tool_calls(reasoning_text)
    if tool_calls:
        print("\n--- Tools Used ---")
        results = call_tools(tool_calls)
        for func_name, result in results.items():
            print(f"{func_name} -> {result}")
        print("\n--- Final Answer ---")
        print(f"{list(results.values())[-1]}")
    else:
        print("\nNo tool needed.")

if __name__ == "__main__":
    main()
