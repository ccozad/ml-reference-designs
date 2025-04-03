# Introduction

This example shows how an assistant can be used to make travel arrangement. The work is based on a detailed tutorial by LangGraph https://langchain-ai.github.io/langgraph/tutorials/customer-support/customer-support/ 

# Dependencies

You will need all of the following dependencies to run this example:

 - API Keys
   - Anthropic
   - OpenAI
 - Python virtual environment

## API Keys

Create an environment file named `.env`. Add the following content to your environment file.

```ini
ANTHROPIC_API_KEY=<your key>
OPENAI_API_KEY=<your key>
```

## Python Virtual Environment

 - Move to the workout-agents folder
   - `cd <lang-graph/travel-agent>`
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

## Zero shot agent

Run the command `python zero_shot_agent.py`


```