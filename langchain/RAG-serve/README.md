# Introduction

This examples builds on the concepts shown in [Retrieval Augmented Generation Q&A pipeline using OpenAI Embeddings, OpenAI Chat and Chroma](/langchain/RAG/README.md)

We'll take the functioning RAG pipeline and wrap it in a REST API. We'll use Flask to begin with and different examples will show how to implement the same ideas with more full featured frameworks.

 ![RAG Pipeline](/images/flask-pipeline.png?raw=true "RAG Pipeline")

The goal of our API includes

 - Communicate over the internet
 - Add new web reference to index and add to our vectorstore
 - View a list of all references
 - Interact with the RAG pipeline by submitting a query and getting a response
 - View a list of interactions

To simplify this example we are intentionally leaving out:
 - Durable data storage
   - Data will only be kept in memory on the Flask side
   - Indexing data is a single node setup with memory based storage for chroma
 - Authentication
   - There are no users, groups or permissions
   - There is no individual resource ownership

Solution Components used
 - Prompt Template: based on https://smith.langchain.com/hub/rlm/rag-prompt
 - Embedding Model: OpenAI Embeddings, remote access (Requires paid account)
 - Large Language Model: OpenAI Chat, gpt-3.5-turbo-0125, remote access (Requires paid account)
 - Vectorstore: Chroma, local instance (Open source)
 - Web Framework: Flask

Paid model access should cost a few cents of usage fees.

# Concepts

## REST architecture basics

REST stands for representation state transfer. REST is an architecture style that was designed for the world wide web. Architecture principles for REST include:

- Uniform interface
  - Resources should look the same no matter where they come from
  - Each resource belongs to one uniform resource identifier (URI)
- Client-server
  - Client and server are independent
  - The client accesses the server using URIs
  - The server passes all data back in a response
- Statelessness
  - Each request includes all of the information needed to process the request
  - The server does not require any server side session data
- Cacheability
  - When possible, resources should be cacheable of the client or server side
- Layered system architecture
  - The client or server should not depend on speaking directly with one another
  - There may be layers in between such as proxies and caching systems

## Resources

A **Resource** is the fundamental unit of a REST API. A Resource has a type, associated data, relationships to other resources and a set of methods to operate on it. 

The methods to operate on a resource are reduced to few possible methods including 

 - **GET** Read a resource or collection of resources
 - **POST** Create a resource
 - **PATCH** Update a resource
 - **DELETE** Delete a resource

 There are other methods covered in the HTTP standard such at PUT and HEAD. We'll focus on just the GET and POST operations for the sake of brevity.

 Resurces can be represented in a variety of data formats. We'll focus on the JavaScript Object Notion (JSON) for this example.

 ## Universal resource identifier (URI)

 A URI can be used to identify any type of resource, not just those on the internet. Since our goal is making our resources available over the interet we'll focus on Universal resource locators (URL) when describing resources. The format of URLs has a convention for REST APIs, That convention is

### Collections
  - `GET <server>/<resources>`
    - Example: 
      - Get a collection of all users `GET https://server.com/users`
  - `POST <server>/<resources>`
    - Example: 
      - Create a new user `POST https://server.com/users`

### Single items
  - `GET <server>/<resources>/<id>`
    - Example: 
      - Get a user with id 1 `GET https://server.com/users/1`
  - `PATCH <server>/<resources>/<id>`
    - Example: 
      - Update a user with id 1 `PATCH https://server.com/users/1`
  - `DELETE <server>/<resources>/<id>`
    - Example: 
      - Delete a user with id 1 `DELETE https://server.com/users/1`

## RAG Domain

For the specific RAG domain we will have the following resources:

- **Reference** A source of knowledge we want the machine learning model to reason about
- **Interaction** An interaction with the RAG pipline

We'll define the following operations against these resources

- **Reference**
  - List all References `GET <server>/references`
  - Create a reference `POST <server>/references`
- **Interaction**
  - List all Interactions `GET <server>/interactions`
  - Create an interaction `POST <server>/interactions`

### Reference Data Format

Create new Reference request body.
```json
{
    "docType": "html",
    "url": "https://test.com/article-1"
}
```

Full Reference record
```json
{
    "id": "e578c227-675a-4935-9b95-dfb4231d7b24",
    "docType": "html",
    "url": "https://test.com/article-1"
}
```

Reference collection

```json
{
    "items": [
        {
            "id": "e578c227-675a-4935-9b95-dfb4231d7b24",
            "docType": "html",
            "url": "https://test.com/article-1"
        }, {
            "id": "e578c227-675a-4935-9b95-dfb4231d7b55",
            "docType": "html",
            "url": "https://test.com/article-2"
        }
    ]
}
```

### Interaction Data Format

Create new Interaction request body.
```json
{
    "query": "How do you make a pb&j sandwich?"
}
```

Full Interaction record
```json
{
    "id": "e578c227-675a-4935-9b95-dfb4231d7b62",
    "query": "How do you make a pb&j sandwich?",
    "answer": "You make a pb&j sandwich by spreading peanut butter and your favorite flavor of jelly on the inner faces of two pieces of bread."
}
```

Reference collection

```json
{
    "items": [
        {
            "id": "e578c227-675a-4935-9b95-dfb4231d7b62",
            "query": "How do you make a pb&j sandwich?",
            "answer": "You make a pb&j sandwich by spreading peanut butter and your favorite flavor of jelly on the inner faces of two pieces of bread."
        }, {
            "id": "6278c227-675a-4935-9b95-dfb4231d7b62",
            "query": "What is 2 + 2?",
            "answer": "4"
        }   
    ]
}
```

# Dependencies

All of the dependencies listed below need to be in place before running the code.

 - Funded OpenAI account
 - ChromaDB
 - Python virtual environment
 - Environment variables


## OpenAI Account

You'll need an OpenAI developer account an API Key. You will also need to purchase credits before making calls to the embedding model.

## ChromaDB 

ChromaDB is an open source embedding database. You can install the server using pip.

```
pip install chromadb
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

# Changes to previous code

Small modifications were needed to adapt the code to being served with Flask. Those changes center on using a class to share the connection to the vectorstore and encapsulating individual script behavior into parameterized methods.


# Running the code

Use the command `flask run --port 5001` to start the flask app listening on port 5001.

Messages are printed to console when different end points are accessed.

Example server output

```text
lask run --port 5001
Initializing vectorstore...
Initializing storage
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
Index html pipeline
Loading document from the web...
URL: https://lilianweng.github.io/posts/2023-06-23-agent/
Document length: 43131
Splitting document into chunks...
Number of splits: 66
Adding splits to embedding vectorstore...
Index pipeline complete
127.0.0.1 - - [14/May/2024 16:16:16] "POST /references HTTP/1.1" 200 -
RAG pipeline
Retrieving documents similar to query...
Retrieved 6 documents
RAG pipeline complete
127.0.0.1 - - [14/May/2024 16:16:24] "POST /interactions HTTP/1.1" 200 -
```

# Testing the code

## Create a Reference

```bash
curl --location --request POST 'http://localhost:5001/references' \
--header 'Content-Type: application/json' \
--data-raw '{
    "docType": "html",
    "url": "https://lilianweng.github.io/posts/2023-06-23-agent/"
```

## Read all References

```bash
curl --location --request GET 'http://localhost:5001/references'
```

## Create an Interaction

```bash
curl --location --request POST 'http://localhost:5001/interactions' \
--header 'Content-Type: application/json' \
--data-raw '{
    "query": "What are the approaches to Task Decomposition?"
}'
```

## Read all Interactions

```bash
curl --location --request GET 'http://localhost:5001/interactions'
```