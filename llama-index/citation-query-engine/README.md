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

## Run a query

```
python3 demo.py

Query the database with: What information do you have about YC?

Retrieved 2 nodes.
Processing node with score: 0.5156701239092963
Processing node with score: 0.4996543388285388

Summary:
YC, or Y Combinator, is known for its distinctive batch model, which involves funding multiple startups simultaneously, twice a year. This approach allows for intensive support over three months, helping startups grow while also providing a community for founders to share experiences and solutions to common problems [1]. The first batch of startups included notable companies such as Reddit and Twitch, and the program was designed to be more appealing to founders by offering a supportive environment compared to traditional summer jobs at established companies [2]. YC initially operated without being a formal fund, but it transitioned to a fund model in 2009 due to its growth, before returning to self-funding after achieving financial stability [4].
```