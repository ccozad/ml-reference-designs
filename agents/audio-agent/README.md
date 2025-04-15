# Overview

Based on a voice agent cookbook recipe by OpenAI https://cookbook.openai.com/examples/agents_sdk/app_assistant_voice_agents

# Dependencies

You will need all of the following dependencies to run this example:

 - OpenAI API key
 - Python virtual environment

## OpenAI API token

Log in to OpenAI and retrieve your API key

Create an environment file named `.env`. Add the following line to your environment file:

```ini
OPENAI_API_KEY=<your token>
```

## Python Virtual Environment

 - Move to the multi-agents folder
   - `cd <agents/audio-agent>`
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