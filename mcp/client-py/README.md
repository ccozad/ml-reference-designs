## Anthropic API key

Create an API key using the Anthropic Dashboard. Copy that key for use in the next step. Create a file named `.env` in the folder where this `README.md` file resides.

Add the following line to your environment file:

```ini
ANTHROPIC_API_KEY=<your key>
```

## Python Virtual Environment

 - Move to the RAG folder
   - `cd <RAG>`
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