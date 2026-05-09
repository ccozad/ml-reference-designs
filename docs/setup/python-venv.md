# Python Virtual Environment

These steps apply to every Python example in this repository. Run them from the example's own folder (the directory that contains its `requirements.txt`).

 - Create a virtual environment
   - On Mac/Linux: `python3 -m venv .venv`
   - On Windows: `python -m venv .venv`
 - Activate the virtual environment
   - On Mac/Linux: `source .venv/bin/activate`
   - On Windows: `.venv\Scripts\activate`
 - Install dependencies
   - On Mac/Linux: `pip3 install -r requirements.txt`
   - On Windows: `pip install -r requirements.txt`
 - Run a script
   - On Mac/Linux: `python3 <script_name>.py`
   - On Windows: `python <script_name>.py`
 - Deactivate the virtual environment when finished
   - `deactivate`
