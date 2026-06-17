"""Index pipeline: load a web document, split it, embed it, and store it in Chroma.

Run this once before rag_pipeline.py or eval_pipeline.py. The document URL can be
overridden with --source-url or the SOURCE_URL environment variable.
"""
import argparse

# Library for selecting which parts of the HTML to keep
from bs4 import SoupStrainer
# Class for loading web documents
from langchain_community.document_loaders import WebBaseLoader
# Text splitter that splits text into chunks of a certain size
from langchain_text_splitters import RecursiveCharacterTextSplitter

import rag_common as rc


def parse_args():
    parser = argparse.ArgumentParser(description="Index a web document into Chroma for RAG.")
    parser.add_argument(
        "--source-url",
        help=f"Document URL to index (env SOURCE_URL; default: {rc.DEFAULT_SOURCE_URL})",
    )
    return parser.parse_args()


def main():
    log = rc.configure_logging()
    rc.load_environment()
    rc.require_openai_key(log)

    args = parse_args()
    source_url = rc.resolve(args.source_url, "SOURCE_URL", rc.DEFAULT_SOURCE_URL)

    log.info("Index pipeline")

    # Load the document from the web, keeping only the post body, title, and header.
    log.info("Loading document from the web: %s", source_url)
    loader = WebBaseLoader(
        web_paths=(source_url,),
        bs_kwargs=dict(
            parse_only=SoupStrainer(class_=("post-content", "post-title", "post-header"))
        ),
    )
    docs = loader.load()
    log.info("Document length: %d", len(docs[0].page_content))

    # Split the document into chunks of 1000 characters with 200 characters of overlap.
    log.info("Splitting document into chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = splitter.split_documents(docs)
    log.info("Number of splits: %d", len(splits))
    log.info("Length of first split: %d", len(splits[0].page_content))
    log.info("Metadata of second split: %s", splits[1].metadata)

    # Embed the chunks and persist them to the Chroma vectorstore.
    log.info("Adding splits to embedding vectorstore (model: %s)...", rc.EMBEDDING_MODEL)
    vectorstore = rc.get_vectorstore()
    vectorstore.add_documents(splits)
    log.info("Index pipeline complete")


if __name__ == "__main__":
    main()
