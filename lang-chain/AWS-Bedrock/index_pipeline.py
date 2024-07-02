import os

from bs4 import BeautifulSoup, SoupStrainer
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
# Open source embeddings from Hugging Face
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

print("Index pipeline")

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
    embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
    collection_name="demo",
    persist_directory=".")

print("Index pipeline complete")