# Introduction

Retrieval Augmented Generation (RAG) is a technique where context is loaded from a datastore and the model is directed to work on the data provided.

Based on concepts presented in https://python.langchain.com/v0.1/docs/use_cases/question_answering/quickstart/

Pipeline Components used
 - Prompt Template: based on https://smith.langchain.com/hub/rlm/rag-prompt
 - Embedding Model: OpenAI Embeddings, remote access (Requires paid account)
 - Large Language Model: OpenAI Chat, gpt-3.5-turbo-0125, remote access (Requires paid account)
 - Vectorstore: Chroma, local instance (Open source)

Paid model access should cost a few cents of usage fees.

# Concepts

First we index the data and then we do RAG using the user's question.

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

You'll need an OpenAI developer account an API Key. You will also need to purchase credits before making calls to the embedding model.

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

# Running the code

## Index Pipeline

After all setup steps are complete, run the command `python3 index_pipeline`, which will produce output like the following:

```text
Index pipeline
Loading OpenAI API key...
Loading document from the web...
Document length: 43131
Splitting document into chunks...
Number of splits: 66
Length of first split: 969
Metadata of second split: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Adding splits to embedding vectorstore...
Index pipeline complete
```

## RAG Pipeline

After the index pipeline is run we can can run the Retrieval Augmented Generation pipeline with the command `python3 rag_pipeline.py`, which will produce output like the following:

```text
RAG pipeline
Loading OpenAI API key...
Retrieving documents similar to query...
Retrieved 6 documents
Asking the RAG pipeline a question...

Question: What are the approaches to Task Decomposition?

Response: Approaches to Task Decomposition include using a Language Model (LLM) with simple prompting, task-specific instructions, or human inputs. Another approach involves LLM+P, which utilizes an external classical planner for long-horizon planning using Planning Domain Definition Language (PDDL). Self-reflection is essential for autonomous agents to improve iteratively by refining past actions and correcting mistakes.

RAG pipeline complete
```

