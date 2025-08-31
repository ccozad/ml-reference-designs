# Introduction

Based on
 - https://www.youtube.com/watch?v=P4xHWojIB-M
 - https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/workflow/citation_query_engine.ipynb

# Resources



# Dependencies

You will need all of the following dependencies to run this example:

 - Funded OpenAI API token
 - Python virtual environment
 - Download the data

## Funded OpenAI API token

Log in to OpenAI and retrieve your access token.

Create an environment file named `.env`. Add the following line to your environment file:

```ini
OPENAI_API_KEY=your token>
```

## Python Virtual Environment

 - Move to the query-engine folder
   - `cd <llama-index/citation-query-engine>`
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

## Download the data

```
mkdir -p 'data/paul_graham/'
wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt' -O 'data/paul_graham/paul_graham_essay.txt'
```

If you run into the problem 

```
nltk.download('stopwords')
[nltk_data] Error loading stopwords: <urlopen error [SSL:
[nltk_data]     CERTIFICATE_VERIFY_FAILED] certificate verify failed:
[nltk_data]     unable to get local issuer certificate (_ssl.c:1000)>
```

See this StackOverflow article https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed

This code from the top response resolved the error for the author

```
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
```

# Running the Code

## Load the data

Issue the command `python load_data.py` which will download persona data to the data folder

## Generate the index

Issue the command `python generate_index.py` which will load all of the JSON document personas in the data folder and addd them to a Chroma DB vector index.

## Query the index

Issue the command `python query_index.py`

```
python query_index.py
Response:  An author with a deep passion for cultural exploration and language, this individual often delves into the rich tapestry of Eastern European history, weaving stories that transport readers to ancient sites and bustling markets. With a background in linguistics or education, they bring a unique perspective to their travel writing, highlighting the linguistic nuances and historical significance of each destination. Another persona is a history or travel enthusiast who captivates general audiences with their vivid descriptions of cultural and archaeological sites. As a content creator or blogger, they share their extensive knowledge and personal experiences, making history and travel accessible and engaging for everyone.
```