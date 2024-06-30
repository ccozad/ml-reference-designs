# Introduction

This example adds simple tool calling to Claude 3.5 model interactions shown in the [Claude 3.5 Hello World Example](/llm/claude-3-5/hello-world/README.md)

 ![Tool Calling](/images/tool-calling.png?raw=true "Tool Calling")

Tool calling involves the model processing natural language in context and suggesting a tool to call. Tool descriptions provided to the model explains in natural language when to use the tool, when not to use the tool and how to call the tool, including any information about named parameters. 

All tool execution is handled by the client and the results of running the tool are passed back to the model for further processing.

Tool calling is a useful pattern to extend the capabilities of a natural language model beyond the foundation model training material to include new information, dynamic data and data housed in traditional databases and APIs.

Pipeline Components used
 - Framework: Anthropic library
 - Large Language Model: Anthropic, `claude-3-5-sonnet-20240620`, remote access (Requires paid account)

## New information

Models are trained on a snapshot of publicly available information. Information formed after the model was trained can be accessed through tool calls that can perform internet searches and data retrieval from privately indexed content.

## Dynamic data

Some types of data such as weather information, stock prices and home prices are constantly changing. A tool is used to call systems where the data is stored.

## Traditional databases

Traditional databases store large volumes of structured and semi-structured data. Tool calls can be used to create, read, update and delete entries in database systems.

## APIs

Data managed by third parties is often accessed through application programming interfaces (APIs). Examples might include sales data, medical records or inventory systems. A tool can bridge the gap between natural language and existing systems with important information.

# Key Ideas

At it's core, tool calling is simple message protocol where the model tells the client when a tool should be invoked. The model has no server side tools it can execute and the model relies on the caller or client to process tool requests.

The process involves the following idea:

 - Tool contracts are defined using natural language
 - The model processes natural language and tells the client which tools to run
 - Tools are implemented using client side code
 - The model performs additional processing on the tool output

## Tool contracts are defined using natural language

The caller is responsible for telling the model what tools are available. Tool descriptions include:

 - A name for the tool
   - Should be unique between all tools defined
   - Will be reflected back as the tool ID to use
 - A description
   - Explains what the tool does
   - Explains when the tool should used or not used
   - Information about return values
 - Info about any parameters
   - Parameter names
   - Value type
   - Validation rules
   - Description for mapping from context
   - Whether the parameter is required or optional

This example has only one tool that takes no parameters. Other examples will expand the tool concept into more advanced usage with parameters and multiple tools.

```python
tools = [
    {
        "name": "random_quote",
        "description": "A tool that returns a random quote. Returns the quote and author.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]
```

## The model processes natural language and tells the client which tools to run

The model's main super power is processing natural language with context. Included in the context provided by the caller is a list of known tools. The description is the primary means that the model uses to suggest a tool. The model will extract relevant parameters and pass back a parsed dictionary of parameters back to the caller along with a tool name.

Here's an example of a model response with a tool call.

```python
[
    TextBlock(
        text="Certainly! I'd be happy to share an inspiring quote with you. To do that, I'll use the random quote tool to fetch a quote for you. Let me do that now.", 
        type='text'
    ), 
    ToolUseBlock(
        id='toolu_018aGePyErVSuRbXATnbfGWu', 
        input={}, 
        name='random_quote', 
        type='tool_use'
    )
]
```

## Tools are implemented using client side code

The caller or client side is responsible for processing all tool requests.

```python
if message.stop_reason == "tool_use":
        tool_use = next(block for block in message.content if block.type == "tool_use")
        tool_name = tool_use.name
        tool_input = tool_use.input

        tool_result = process_tool_call(tool_name, tool_input)

        response = client.messages.create(
            model=MODEL,
            max_tokens=4096,
            messages=[
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": message.content},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": str(tool_result),
                        }
                    ],
                },
            ],
            tools=tools,
        )
```
## The model performs additional processing on the tool output

Once the model receives the tool response further reasoning can be performed such as calling other tools or elaborating on the output. In our example the model gave expanded commentary as its knowledge base included information about the author and the subject of the quote.

```text
Thank you for your patience. I've retrieved an inspiring quote for you:

"We are continually faced by great opportunities brilliantly disguised as insoluble problems." - Lee Iacocca

This quote by Lee Iacocca, a renowned American automobile executive and author, offers a powerful perspective on challenges and opportunities. It encourages us to view seemingly insurmountable problems as potential opportunities for growth, innovation, and success.

Iacocca's words remind us that what may initially appear as an obstacle or difficulty could actually be a chance for us to learn, improve, or create something remarkable. It's a call to approach challenges with optimism and creativity, recognizing that within every problem lies the seed of an opportunity.

This mindset can be particularly inspiring in both personal and professional contexts, encouraging us to persist in the face of adversity and to look for the potential benefits or lessons in every situation we encounter.
```

# Resources

 - https://www.anthropic.com
 - https://docs.anthropic.com/en/docs/build-with-claude/tool-use
 - https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/calculator_tool.ipynb

# Dependencies

You will need all of the following dependencies to run this example:

 - Paid Anthropic account
 - Anthropic API Key
 - Python virtual environment

## Paid Anthropic account

You'll need to register for an Anthropic API account and add some paid credits to your account. This example should cost less than a few cents.

## Anthropic API key

Create an API key using the Anthropic Dashboard. Copy that key for use in the next step. Create a file named `.env` in the folder where this `README.md` file resides.

Add the following line to your environment file:

```ini
ANTHROPIC_API_KEY=<your key>
```

## Python virtual environment

 - Move to the hello world folder
   - `cd <llm/claude-3-5/hello-world>`
 - Create a virtual environment
   - On Mac: `python3 -m venv .venv`
   - On Windows: `python -m venv .venv`
 - Activate the virtual environment
   - On Mac: `source .venv/bin/activate`
   - On Windows: `.venv\Scripts\activate`
 - Install dependencies
   - On Mac: `pip3 install -r requirements.txt`
   - On Windows: `pip install -r requirements.txt`
 - Call a specific script
   - On Mac: `python3 <script_name>.py`
   - On Windows: `python <script_name>.py`
 - Deactivate virtual environment
   - `deactivate`

# Running the code

After all setup steps are complete, run the command `python app.py`, which will produce output like the following:

```text

==================================================
User Message: Tell me an inspiring quote.
==================================================

Initial Response:
Stop Reason: tool_use
Content: [TextBlock(text="Certainly! I'd be happy to share an inspiring quote with you. To do this, I'll use the random_quote tool, which will provide us with a quote and its author. Let me fetch that for you.", type='text'), ToolUseBlock(id='toolu_01KJeUFLxoJdCPPotCsLCQVD', input={}, name='random_quote', type='tool_use')]

Tool Used: random_quote
Tool Input: {}
Tool Result: {'quote': 'We are continually faced by great opportunities brilliantly disguised as insoluble problems.', 'author': 'Lee Iacocca'}

Final Response: Thank you for your patience. I've retrieved an inspiring quote for you:

"We are continually faced by great opportunities brilliantly disguised as insoluble problems." - Lee Iacocca

This quote by Lee Iacocca, a renowned American automobile executive and author, offers a powerful perspective on challenges and opportunities. It encourages us to view seemingly insurmountable problems as potential opportunities for growth, innovation, and success.

Iacocca's words remind us that what may initially appear as an obstacle or difficulty could actually be a chance for us to learn, improve, or create something remarkable. It's a call to approach challenges with optimism and creativity, recognizing that within every problem lies the seed of an opportunity.

This mindset can be particularly inspiring in both personal and professional contexts, encouraging us to persist in the face of adversity and to look for the potential benefits or lessons in every situation we encounter.
```