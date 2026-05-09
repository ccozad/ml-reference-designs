# Introduction

https://huggingface.co/learn/agents-course/unit2/llama-index/components

# Resources

 - https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader/
 - https://www.llamaindex.ai/llamaparse
 - https://llamahub.ai/

# Known Issues

There was a problem since the original Hugging Face notebook was published where 404 errors will happen when trying to call the model as conversational. Hopefully this issue will be resolved at a later time, and if not, here are related notes.

 - https://huggingface.co/agents-course/notebooks/discussions/82
 - https://github.com/run-llama/llama_index/issues/18547


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

Set up a Python virtual environment ([instructions](../../docs/setup/python-venv.md)), then install this example's dependencies with `pip install -r requirements.txt`.

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