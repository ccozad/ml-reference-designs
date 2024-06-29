# Introduction

Anthropic offers a number of state of the art LLMs that are competitive in features to market leader OpenAI. This example shows the very basic code to call the Claude 3.5 model. Other examples will show more advanced usage, such as tool calling.

# Resources

 - https://www.anthropic.com

# Dependencies

You will need all of the following dependencies to run this example:

 - Paid Anthropic account
 - Anthropic API Key
 - Python virtual environment

## Paid Anthropic Account

You'll need to register for an Anthropic API account and add some paid credits to your account. This example should cost less than a few cents.

## Anthropic API Key

Create an API key using the Anthropic Dashboard. Copy that key for use in the next step. Create a file named `.env` in the folder where this `README.md` file resides.

Add the following line to your environment file:

```ini
ANTHROPIC_API_KEY=<your key>
```

## Python Virtual Environment

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
PEMDAS is an acronym used to remember the order of operations in mathematics. Let's break down each step:

1. P - Parentheses
   • First, solve any operations inside parentheses or brackets.

2. E - Exponents
   • Next, calculate any exponents or roots.

3. M - Multiplication
   • Perform multiplication from left to right.

4. D - Division
   • Perform division from left to right.
   • Note: Multiplication and division have the same priority and should be done in order from left to right.

5. A - Addition
   • Perform addition from left to right.

6. S - Subtraction
   • Perform subtraction from left to right.
   • Note: Addition and subtraction have the same priority and should be done in order from left to right.

Remember, when operations have the same priority (like multiplication and division, or addition and subtraction), you work from left to right in the expression.

By following PEMDAS, you can solve complex mathematical expressions step-by-step in the correct order.
```