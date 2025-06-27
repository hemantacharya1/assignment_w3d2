# Tool-Enhanced Reasoning with Gemini API

A Python application that combines Google Gemini API's natural language reasoning with external tools to answer complex queries through step-by-step problem solving.

## Overview

This project demonstrates how to build an intelligent reasoning system that:
- Uses Gemini API for natural language understanding and chain-of-thought reasoning
- Automatically decides when to invoke external tools based on query requirements
- Combines LLM reasoning with tool outputs for accurate final answers
- Maintains full transparency in the reasoning process

The system interprets natural language queries, breaks them down into logical steps, calls appropriate tools when needed, and synthesizes results into comprehensive answers.

## Features

- **Step-by-Step Reasoning**: Leverages Gemini's natural language processing for logical problem decomposition
- **Automatic Tool Selection**: Intelligently chooses appropriate tools based on query context
- **Manual Tool Invocation**: Transparent tool calling mechanism using regex parsing
- **Modular Architecture**: Clean separation between reasoning logic and tool implementations
- **Built-in Tools**: 
  - Math operations (`average`, `square_root`)
  - String processing (`count_vowels`, `string_length`)
- **No External Frameworks**: Simple, transparent implementation without complex agent frameworks

## Installation

### Prerequisites

- Python 3.7+
- Google Gemini API key

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tool_reasoning_project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API key**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Gemini API key:
   ```env
   GOOGLE_API_KEY=your-gemini-api-key-here
   ```

## Usage

### Basic Usage

Run the main script:
```bash
python main.py
```

Enter your natural language query when prompted, and the system will:
1. Analyze the query using Gemini API
2. Determine necessary tools and steps
3. Execute tool calls as needed
4. Provide a comprehensive answer with reasoning

### Example Interactions

#### Mathematical Reasoning
```
Input: What is the square root of the average of 15 and 18?

Output:
--- LLM Reasoning ---
Step 1: Find the average of 15 and 18.
[TOOL: average(a=15, b=18)]
Step 2: Calculate the square root of the average obtained in Step 1.
[TOOL: square_root(x=16.5)]

The square root of the average of 15 and 18 is approximately 4.06.

--- Tools Used ---
average -> 16.5
square_root -> 4.06201920231798

--- Final Answer ---
4.06201920231798
```

#### String Processing
```
Input: How many vowels are in 'Multimodality'?

Output:
--- LLM Reasoning ---
To answer "How many vowels are in 'Multimodality'?", I need to count 
the vowels (a, e, i, o, u) in the word.
[TOOL: count_vowels(word="Multimodality")]

--- Tools Used ---
count_vowels -> 5

--- Final Answer ---
5
```

#### Simple String Operations
```
Input: Length of 'Artificial'?

Output:
--- LLM Reasoning ---
To find the length of the word 'Artificial', I'll use the string_length tool.
[TOOL: string_length(word='Artificial')]

--- Tools Used ---
string_length -> 10

--- Final Answer ---
10
```

## Project Structure

```
tool_reasoning_project/
├── main.py                   # Main application logic and Gemini integration
├── tools/
│   ├── math_tools.py        # Mathematical utility functions
│   └── string_tools.py      # String processing utilities
├── prompts/
│   └── reasoning_prompt.txt # System prompt template for Gemini
├── .env.example            # Environment variable template
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Available Tools

### Math Tools (`tools/math_tools.py`)
- `average(a, b)`: Calculates the average of two numbers
- `square_root(x)`: Computes the square root of a number

### String Tools (`tools/string_tools.py`)
- `count_vowels(word)`: Counts vowels (a, e, i, o, u) in a string
- `string_length(word)`: Returns the length of a string

## How It Works

### 1. Query Processing
The system uses a carefully crafted prompt that instructs Gemini to:
- Analyze queries step-by-step
- Identify when external tools are needed
- Format tool calls in a specific syntax: `[TOOL: function_name(param=value)]`
- Provide reasoning for each step

### 2. Tool Detection and Execution
- Regex patterns extract tool calls from Gemini's response
- Parameters are parsed and validated
- Corresponding Python functions are executed
- Results are collected and formatted

### 3. Result Synthesis
- Tool outputs are combined with Gemini's reasoning
- Final answers are presented with full transparency
- Both reasoning process and tool results are displayed

## Extending the System

### Adding New Tools

1. **Create tool function** in appropriate module (`tools/math_tools.py` or `tools/string_tools.py`)
2. **Update the system prompt** in `prompts/reasoning_prompt.txt` to include the new tool
3. **Add tool mapping** in `main.py` to connect function names with implementations

Example:
```python
# In tools/math_tools.py
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

# In main.py, add to tool mapping
'multiply': math_tools.multiply,
```

### Customizing Prompts

Edit `prompts/reasoning_prompt.txt` to:
- Modify reasoning style
- Add new tool descriptions
- Change output formatting
- Adjust problem-solving approach

## Dependencies

- `google-generativeai`: Google Gemini API client
- `python-dotenv`: Environment variable management
- `re`: Regular expressions (built-in)

## Notes and Considerations

- **Tool Priority**: When tools are available, their results take precedence over Gemini's internal calculations
- **Error Handling**: Basic error handling is implemented for API calls and tool execution
- **Parameter Parsing**: Care is taken to properly extract and format parameters for tool calls
- **Extensibility**: The modular design makes it easy to add new tools and reasoning capabilities

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure your Gemini API key is correctly set in the `.env` file
2. **Tool Call Parsing**: If tools aren't being called, check the prompt format and regex patterns
3. **Parameter Errors**: Verify parameter names and types match tool function signatures

### Getting Help

- Check the example queries and outputs for expected behavior
- Review the system prompt to understand expected tool call format
- Examine the tool implementations for parameter requirements

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]