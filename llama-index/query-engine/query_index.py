import os
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
import nest_asyncio
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Retrieve HF_TOKEN from the environment variables
hf_token = os.getenv("HF_TOKEN")

db = chromadb.PersistentClient(path="./persona_chroma_db")
chroma_collection = db.get_or_create_collection(name="personas")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store, embed_model=embed_model
)

nest_asyncio.apply()  # This is needed to run the query engine
llm = HuggingFaceInferenceAPI(
    token=hf_token, 
    model="Qwen/Qwen2.5-Coder-32B-Instruct",
    task="text-generation"
)
query_engine = index.as_query_engine(
    llm=llm,
    response_mode="tree_summarize"
)
response = query_engine.query(
    "Respond using a persona that describes author and travel experiences?"
)

print(f"Response: {response}")