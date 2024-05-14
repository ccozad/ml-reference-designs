# Import and RAG pipeline imports
import os

from bs4 import BeautifulSoup, SoupStrainer
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Flask imports
from flask import Flask, request, Response
# Used to generate globally unique identifiers
from uuid import uuid4
# Used to serialize and deserialize Python objects
import json

app = Flask(__name__)

# Our storage for this example will simply be an in memory dictionary
print("Initializing storage")
storage = {
    'references': {},
    'interactions': {}
}

print("Loading OpenAI API key...")
import dotenv
dotenv.load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def index_html_pipeline(url):
    print("Index html pipeline")
    print("Loading document from the web...")
    print(f"URL: {url}")
    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs=dict(
            parse_only=SoupStrainer(
                class_=("post-content", "post-title", "post-header")
            )
        ),
    )
    docs = loader.load()
    if len(docs) == 0:
        print("No documents found")
        return False
    else:
        print(f"Document length: {len(docs[0].page_content)}")
        print("Splitting document into chunks...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        print(f"Number of splits: {len(splits)}")

        print("Adding splits to embedding vectorstore...")
        vectorstore = Chroma.from_documents(
            documents=splits, 
            embedding=OpenAIEmbeddings(),
            collection_name="demo",
            persist_directory=".")

        print("Index pipeline complete")
        return True

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def rag_pipeline(query):
    print("RAG pipeline")
    vectorstore = Chroma(
        collection_name="demo", 
        embedding_function=OpenAIEmbeddings(),
        persist_directory=".")

    print("Retrieving documents similar to query...")
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
    retrieved_docs = retriever.invoke(query)
    print(f"Retrieved {len(retrieved_docs)} documents")

    llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

    template = """
    You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise. 

    Question: {question} 

    Context: {context} 

    Answer:
    """

    prompt_template = PromptTemplate.from_template(template)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser()
    )

    response = rag_chain.invoke(query)
    return True, response

@app.route("/references", methods=['GET', 'POST'])
def all_references():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is not None and 'url' in body and 'docType' in body:
            if body['docType'] == 'html':
                index_success = index_html_pipeline(body['url'])
                if index_success:
                    id = uuid4()
                    body['id'] = str(id)
                    storage['references'][str(id)] = body
                    return Response(json.dumps(body, indent=4), status=200, mimetype='application/json')
                else:
                    return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
            else:
                return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
    elif request.method == 'GET':
        all_references = {
            'items': []
        }
        for k,v in storage['references'].items():
            all_references['items'].append(v)
        return Response(json.dumps(all_references, indent=4), status=200, mimetype='application/json')

@app.route("/interactions", methods=['GET', 'POST'])
def all_interactions():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is not None and 'query' in body:
            rag_success, answer = rag_pipeline(body['query'])
            if rag_success:
                id = uuid4()
                body['id'] = str(id)
                body['answer'] = answer
                storage['interactions'][str(id)] = body
                return Response(json.dumps(body, indent=4), status=200, mimetype='application/json')
            else:
                return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
    elif request.method == 'GET':
        all_interactions = {
            'items': []
        }
        for k,v in storage['interactions'].items():
            all_interactions['items'].append(v)
        return Response(json.dumps(all_interactions, indent=4), status=200, mimetype='application/json')