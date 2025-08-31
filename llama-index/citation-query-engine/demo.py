from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.core.schema import MetadataMode
from llama_index.embeddings.openai import OpenAIEmbedding
from citation_query_engine import CitationQueryEngineWorkflow
from config import (
    DEFAULT_CITATION_CHUNK_SIZE,
    DEFAULT_CITATION_CHUNK_OVERLAP,
)

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

import logging

logging.basicConfig(level=logging.WARNING)

async def main():
    documents = SimpleDirectoryReader("data/paul_graham").load_data()
    Settings.chunk_size = DEFAULT_CITATION_CHUNK_SIZE
    Settings.chunk_overlap = DEFAULT_CITATION_CHUNK_OVERLAP
    index = VectorStoreIndex.from_documents(
        documents=documents,
        embed_model=OpenAIEmbedding(model_name="text-embedding-3-small"),
    )

    w = CitationQueryEngineWorkflow()

    # Run a query
    result = await w.run(query="What information do you have about YC?", index=index)
    print("\nSummary:")
    print(result)
    print("\nSource Nodes:")
    for i, source_node in enumerate(result.source_nodes):
        print(source_node.node.get_content())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())