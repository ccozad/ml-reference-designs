"""Shared configuration and helpers for the lang-chain/RAG example.

Keeping the index, RAG, and eval pipelines consistent means one place for the
model choices, environment loading, logging, and the Chroma vectorstore.
"""
import logging
import os
import sys

import dotenv

# --- Defaults (override via CLI flags or environment variables) ---
DEFAULT_SOURCE_URL = "https://lilianweng.github.io/posts/2023-06-23-agent/"
DEFAULT_QUERY = "What are the approaches to Task Decomposition?"

# --- Model choices (explicit, no implicit SDK defaults) ---
CHAT_MODEL = "gpt-5.4-nano"
EMBEDDING_MODEL = "text-embedding-3-small"

# --- Vectorstore location ---
# Persist into a single, predictable subdirectory so Chroma does not scatter a
# sqlite file plus a GUID-named collection folder across the example root.
COLLECTION_NAME = "demo"
PERSIST_DIR = "chroma_db"


def configure_logging():
    """Route all progress output through logging; level via the LOG_LEVEL env var."""
    level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(level=level, format="%(levelname)s %(message)s")
    # Keep the demo output focused on our own messages, not HTTP chatter.
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    return logging.getLogger("rag")


def load_environment():
    """Load variables from a local .env file, if present."""
    dotenv.load_dotenv()
    # WebBaseLoader emits a warning when this is unset; give it a sensible default.
    os.environ.setdefault("USER_AGENT", "ml-reference-designs-rag-example")


def require_openai_key(log):
    """Exit with a friendly one-liner if the key is missing (no stack trace)."""
    if not os.getenv("OPENAI_API_KEY"):
        log.error("Missing OPENAI_API_KEY. Copy .env.example to .env and add your key.")
        sys.exit(1)


def resolve(cli_value, env_var, default):
    """Resolve a setting in priority order: CLI flag > environment variable > default."""
    if cli_value is not None:
        return cli_value
    return os.getenv(env_var, default)


def get_embeddings():
    """OpenAI embedding model, named explicitly rather than relying on the SDK default."""
    from langchain_openai import OpenAIEmbeddings

    return OpenAIEmbeddings(model=EMBEDDING_MODEL)


def get_vectorstore():
    """Chroma vectorstore persisted to PERSIST_DIR."""
    from langchain_chroma import Chroma

    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=PERSIST_DIR,
    )
