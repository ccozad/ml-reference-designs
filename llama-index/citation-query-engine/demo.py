from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.schema import MetadataMode
from llama_index.embeddings.openai import OpenAIEmbedding
from citation_query_engine import CitationQueryEngineWorkflow

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

import logging

logging.basicConfig(level=logging.WARNING)

async def main():
    documents = SimpleDirectoryReader("data/paul_graham").load_data()
    index = VectorStoreIndex.from_documents(
        documents=documents,
        embed_model=OpenAIEmbedding(model_name="text-embedding-3-small"),
    )

    w = CitationQueryEngineWorkflow()

    # Run a query
    result = await w.run(query="What information do you have about YC?", index=index)
    print("\nSummary:")
    print(result)
    # print out the citations
    #for i, source_node in enumerate(result.source_nodes):
    #    print(f"\nCitation {i}:")
    #    print(source_node.node.get_content(metadata_mode=MetadataMode.ALL))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())