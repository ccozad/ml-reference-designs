import os

# Library for parsing HTML and XML documents
from bs4 import BeautifulSoup, SoupStrainer
# Class for loading web documents
from langchain_community.document_loaders import WebBaseLoader
# Our open source vectorstore
from langchain_chroma import Chroma
# OpenAI embeddings, accessed remotely using an OpenAI API key
from langchain_openai import OpenAIEmbeddings
# Text splitter that splits text into chunks of a certain size
from langchain_text_splitters import RecursiveCharacterTextSplitter

print("Index pipeline")

# Load the OpenAI API key from the environment.
print("Loading OpenAI API key...")
import dotenv
dotenv.load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Load the document from the web.
print("Loading document from the web...")
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()
print(f"Document length: {len(docs[0].page_content)}")

# Split the document into chunks of 1000 characters with 200 characters of overlap.
print("Splitting document into chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200)
splits = text_splitter.split_documents(docs)
print(f"Number of splits: {len(splits)}")
print(f"Length of first split: {len(splits[0].page_content)}")
print(f"Metadata of second split: {splits[1].metadata}")

# Create a Chroma object with the OpenAI embeddings.
print("Adding splits to embedding vectorstore...")
vectorstore = Chroma.from_documents(
    documents=splits, 
    embedding=OpenAIEmbeddings(),
    collection_name="demo",
    persist_directory=".")

print("Index pipeline complete")