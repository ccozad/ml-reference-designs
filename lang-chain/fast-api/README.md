# Dependencies

You will need all of the following dependencies to run this example:

 - Funded OpenAI API Key
 - Python virtual environment

## Funded OpenAI API Key

Create an environment file named `.env`. Add the following line to your environment file:

```ini
OPENAI_API_KEY=<your key>
```

## Python Virtual Environment

 - Move to the fast-api folder
   - `cd <lang-chain/fast-api>`
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