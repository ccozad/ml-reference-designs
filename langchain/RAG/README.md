# Introduction

Retrieval Augmented Generation (RAG) is a technique where context is loaded from a datastore and the model is directed to work on the data provided.

# Concepts

First we index the data and then we do RAG using the quer's question.

## Indexing

Indexing involves making the data searchable. The process involves

1. Load: Load documents using a **Document Loader**
2. Split: Divide documents into chunks with a **Text Splitter**
3. Store: Convert text to numbers with an **Embedding Model** and store it in a **Vector Store**

## Retrieve and Generate

1. Retrieve: Use the user input to retrieve relevant context chunk susing a **Retriever**
2. Generate: A **Chat Model** or **LLM** generates a response using the prompt and context

# Dependencies

## OpenAI Account

You'll need an OpenAI developer account an API Key

## ChromaDB

ChromaDB is an open source embedding database. You can install the server using pip.

```
pip install chromadb
chroma run
```

For more details see https://www.trychroma.com

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

## Environment Variables

Create a file named `.env` with the contents shown below

```
OPENAI_API_KEY=<your key>
```


