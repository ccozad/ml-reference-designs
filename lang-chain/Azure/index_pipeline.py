import os

from bs4 import BeautifulSoup, SoupStrainer
from langchain_community.document_loaders import WebBaseLoader
# Open source embeddings from Hugging Face
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Azure
from langchain_community.vectorstores.azuresearch import AzureSearch

print("Loading Azure credentials...")
import dotenv
dotenv.load_dotenv()
vector_store_address = os.getenv("VECTOR_STORE_ADDRESS")
vector_store_key = os.getenv("VECTOR_STORE_KEY")
vector_store_name = os.getenv("VECTOR_STORE_NAME")

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

# Create an Azure Search with the OpenAI embeddings.
print("Adding splits to embedding vector store...")

vectorstore = AzureSearch(
    azure_search_endpoint = vector_store_address,
    azure_search_key = vector_store_key,
    index_name = vector_store_name,
    embedding_function=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2").embed_query,
    additional_search_client_options={"retry_total": 4}
)

vectorstore.add_documents(documents = splits)

print("Index pipeline complete")