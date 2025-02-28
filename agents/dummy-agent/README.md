# Introduction

Based on this notebook from the Hugging Face agent course https://huggingface.co/agents-course/notebooks/blob/main/dummy_agent_library.ipynb 

# Dependencies

You will need all of the following dependencies to run this example:

 - Hugging Face token
 - Python virtual environment

## Hugging Face token

Log in to Hugging Face and retrieve your token from https://hf.co/settings/tokens

Create an environment file named `.env`. Add the following line to your environment file:

```ini
HF_TOKEN=<your token>
```

## Python Virtual Environment

 - Move to the hello world folder
   - `cd <agents/dummy-agent>`
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

## Bad template

This example shows what happens when the instruct model is called with a bad template format.

Run the command `python bad_template.py` and you will get output

```text
 Paris. The capital of France is Paris. The capital of France is Paris. The capital of France is Paris. The capital of France is Paris. The capital of France is Paris. The capital of France is Paris. The capital of France is Paris. The capital of France is Paris. The capital of France is Paris. The capital of France is Paris. The capital of France is Paris. The capital of France is Paris. The capital of France is Paris. The capital of France is Paris.
```

## Good template

This example shows what happens when the instruct model is called with the expected template format.

Run the command `python good_template.py` and you will get output

```text
...Paris!
```

## Chat approach

Raw tokens can be awkward to work with so we can use the chat approach to make more compact and concise code.

Run the command `python chat.py` and you will get output

```text
Paris.
```

## Weather agent

This example simulates what a chat would look like for an agent that can call out to a weather tool.

Run the command `python weather_agent.py` and you will get output

```text
Final Answer: The current weather in London is sunny with low temperatures.
```