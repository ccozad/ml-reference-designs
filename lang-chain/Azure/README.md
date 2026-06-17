# Dependencies

All of the dependencies listed below need to be in place before running the code.

 - Azure account
 - Azure AI Search
 - OpenAI API key
 - Environment variables
 - Python virtual environment
 - Create vector index

## Azure account

You will need an Azure account to create a search service.

## Azure AI Search

Azure AI Search includes support for traditional search approaches as well as semantic search using vector store concepts. There is a free tier that allows 50 MB of data to be stored in one index.

Follow these instructions for how to create An Azure AI Search instance using the Azure Portal https://learn.microsoft.com/en-us/azure/search/search-create-service-portal

The index is created the first time it is referenced if it doesn't already exist. You will need to use an admin key to successfully create the index.

Further Reading
- https://azure.microsoft.com/en-us/pricing/details/search/
- https://learn.microsoft.com/en-us/azure/search/search-security-api-keys

## OpenAI API key

This example stores and searches embeddings in Azure AI Search, but the embeddings themselves are generated locally with an open-source Hugging Face model (`all-MiniLM-L6-v2`) — no OpenAI key is required for indexing or retrieval. The OpenAI key is used only by the RAG pipeline's chat model (`gpt-5.4-nano` in `rag_pipeline.py`), which writes the final natural-language answer from the retrieved documents. Retrieve your key from https://platform.openai.com/api-keys

## Environment variables

Create a file named `.env` in the project directory and add the following content

```ini
VECTOR_STORE_ADDRESS=
VECTOR_STORE_KEY=
VECTOR_STORE_NAME=
OPENAI_API_KEY=
```

## Python Virtual Environment

Set up a Python virtual environment ([instructions](../../docs/setup/python-venv.md)), then install this example's dependencies with `pip install -r requirements.txt`.

# Running the code

## Index Pipeline

After all setup steps are complete, run the command `python3 index_pipeline`, which will produce output like the following:

```text
Index pipeline
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

Retrieving documents similar to query...
Retrieved 6 documents
Asking the RAG pipeline a question...

Question: What are the approaches to Task Decomposition?

Response: There are three approaches to Task Decomposition: (1) by LLM with simple prompting, (2) by using task-specific instructions, and (3) with human inputs. These approaches can be used to decompose complex tasks into smaller and simpler steps. 

RAG pipeline complete
```




