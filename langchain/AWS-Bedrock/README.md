# Introduction

This examples builds on the concepts shown in [Retrieval Augmented Generation Q&A pipeline using OpenAI Embeddings, OpenAI Chat and Chroma](/langchain/RAG/README.md)

Instead of using OpenAI services, we'll use an open source embedding model from Hugging Face and a foundation model accessed through the AWS Bedrock service.

Pipeline Components used
 - Prompt Template: based on https://smith.langchain.com/hub/rlm/rag-prompt
 - Embedding Model: Hugging Face Embeddings, all-MiniLM-L6-v2 model, local access
 - Large Language Model: AWS Bedrock, foundation model `meta.llama3-8b-instruct-v1:0`, remote access (Requires paid account)
 - Vectorstore: Chroma, local instance (Open source)

Paid model access should cost a few cents of usage fees.

# Concepts

## Hugging Face Embeddings

There are many options for creating embedding information. Paid options include OpenAI and open source options include models created by the Hugging Face community. The key idea for an embedding model is that the same model or algorithm has to be used to index information and retrieve the information later. Most open source models can be loaded dynamically upon first use. As your systems begin to move from development to production it is advisable to store off the models and model weights in case there is a network issue or the model is no longer distributed. The `~/.cache` folder is used on MacOS, other operating systems should have a similar location with the home directory or user directory on Windows.

The vectorstore code is almost exactly as it was in the OpenAI example except now we provide a Hugging Face embedding implementation.

```python
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

vectorstore = Chroma(
    collection_name="demo", 
    embedding_function=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
    persist_directory=".")
```

## AWS Bedrock

Hosting state of the art large language models (LLMs) requires servers with large amounts of RAM, storage and advanced GPU cards. These server configurations are expensive to run for consumers when provisioned on a dedicated server so AWS created a fully hosted solution that allows for usage based pricing. AWS Bedrock allows access to a number of foundation models from many popular publishers such as Meta, Anthropic, AI21 and AWS. You typically need to request access to models before you can make calls. In this example we use the Llama 3 8B model from Meta. Other foundation models you have access to can be readily referenced by model ID in the Bedrock set up code in the `rag_pipeline.py` implementation.

We initialize our LLM hosted on AWS Bedrock as follows.

```python
from langchain_aws import BedrockLLM

# Initialize the Bedrock client with the Meta's Llama 3 8b model
print("Initializing Bedrock client...")
llm = BedrockLLM(model_id="meta.llama3-8b-instruct-v1:0")
```

The Provider detail page has information on specific model ID strings.

If you want to see what goes into setting up a Llama 3B 8B model from scratch without Bedrock, please refer to [Run Llama 3 on an AWS EC2 instance](/llm/llama-3/hello-world/README.md).

## LangChain Composition

The LangChain composition remains unchanged from our original OpenAI sample because the Bedrock implementation uses the same LLM class interface that the OpenAI implementation uses. This is a core idea of LangChain where implementations can be swapped out without breaking the application.

In computer science terms, this is the `Liskov Substitution Principle` and `Polymorphism` in practice.

Further reading:
 - https://stackify.com/solid-design-liskov-substitution-principle
 - https://www.baeldung.com/cs/polymorphism

# Dependencies

All of the dependencies listed below need to be in place before running the code.

 - Paid AWS account
 - AWS Bedrock foundation model access
 - AWS user with Bedrock access
 - ChromaDB
 - Python virtual environment

## Paid AWS account

You will need an AWS account with a credit card activated. While Bedrock is very economical to use, it is not available on the AWS free tier.

## AWS Bedrock foundation model access

Each foundation model must be individually requested to be granted access. You will need to state your intended usage for compliance with the terms of use a given LLM family. This sample uses the Llama 3 8B model from Meta.

## AWS user with Bedrock access

Once you have model access you will need to use `IAM` in the AWS console or command line to create a user that is part of group that has access to AWS Bedrock. Assigning the AWS managed policy of `AmazonBedrockFullAccess` to the user's group is sufficient for this sample. Once you create your user, you will need to generate an access key for local code. Information for the AWS access key ID and secret will be shown on screen. Use that information to set the following environment variables to the appropriate values

 - `AWS_ACCESS_KEY_ID`
 - `AWS_SECRET_ACCESS_KEY`

 If you do not wish to use environment variables to specify this information you can also set credentials based on the process described in the AWS docs: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html.

 If you add credentials to any profile besides the default you may need to specify the profile using the `credentials_profile_name`. See https://python.langchain.com/v0.1/docs/integrations/platforms/aws/ 

 Editor's note: At the time of publication we had problems with the credential profile name so the fall back was to use the environment variable approach.

## ChromaDB 

ChromaDB is an open source embedding database. You can install the server using pip.

```
pip install chromadb
```

For more details see https://www.trychroma.com

## Python Virtual Environment

 - Move to the RAG folder
   - `cd <AWS-Bedrock>`
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

Retrieving documents similar to query...
Retrieved 6 documents
Initializing Bedrock client...
Asking the RAG pipeline a question...

Question: What are the approaches to Task Decomposition?

Response: There are three approaches to Task Decomposition: (1) by LLM with simple prompting, (2) by using task-specific instructions, and (3) with human inputs. These approaches can be used to decompose complex tasks into smaller and simpler steps. 

RAG pipeline complete
```




