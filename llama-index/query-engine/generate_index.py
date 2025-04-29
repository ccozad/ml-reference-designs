# Load files from a directory
from llama_index.core import SimpleDirectoryReader
# Embedding actions
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
# Vector storage
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore

reader = SimpleDirectoryReader(input_dir="data")
documents = reader.load_data()
print(f"Document count: {len(documents)}")

db = chromadb.PersistentClient(path="./persona_chroma_db")
chroma_collection = db.get_or_create_collection(name="personas")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(),
        HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5"),
    ],
    vector_store=vector_store,
)

nodes = pipeline.run(documents=documents)
print(f"nodes count: {len(nodes)}")