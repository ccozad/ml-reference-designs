# Introduction
https://huggingface.co/blog/gradio-mcp

![Gradio MCP Server](/images/gradio-mcp.png?raw=true "Gradio MCP Server")


# Dependencies

You will need all of the following dependencies to run this example:

 - Hugging Face token
 - Python virtual environment

## Python Virtual Environment

 - Move to the code-agents folder
   - `cd <mcp/gradio/hello-world>`
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

python app.py
* Running on local URL:  http://127.0.0.1:7860
* To create a public link, set `share=True` in `launch()`.

🔨 MCP server (using SSE) running at: http://127.0.0.1:7860/gradio_api/mcp/sse
Keyboard interruption in main thread... closing server.