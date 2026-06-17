"""RAG pipeline: retrieve context from Chroma and answer a question with an LLM.

Run index_pipeline.py first. The question can be overridden with --query or the
QUERY environment variable.
"""
import argparse

# Output parser for turning the chat message into a plain string
from langchain_core.output_parsers import StrOutputParser
# Prompt template for formatting the input to the language model
from langchain_core.prompts import PromptTemplate
# Passthrough runnable for passing the input straight to the prompt template
from langchain_core.runnables import RunnablePassthrough
# OpenAI chat model accessed remotely using an OpenAI API key
from langchain_openai import ChatOpenAI

import rag_common as rc

# Based on https://smith.langchain.com/hub/rlm/rag-prompt
RAG_TEMPLATE = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

Question: {question}

Context: {context}

Answer:
"""


def format_docs(docs):
    """Join retrieved documents into a single context string."""
    return "\n\n".join(doc.page_content for doc in docs)


def build_rag_chain(retriever):
    """Compose retriever -> prompt -> chat model -> string output."""
    llm = ChatOpenAI(model=rc.CHAT_MODEL)
    prompt_template = PromptTemplate.from_template(RAG_TEMPLATE)
    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser()
    )


def parse_args():
    parser = argparse.ArgumentParser(description="Answer a question using RAG over the indexed corpus.")
    parser.add_argument(
        "--query",
        help=f"Question to ask (env QUERY; default: {rc.DEFAULT_QUERY!r})",
    )
    return parser.parse_args()


def main():
    log = rc.configure_logging()
    rc.load_environment()
    rc.require_openai_key(log)

    args = parse_args()
    query = rc.resolve(args.query, "QUERY", rc.DEFAULT_QUERY)

    log.info("RAG pipeline")

    # Get the top 6 most similar documents to the query.
    vectorstore = rc.get_vectorstore()
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
    log.info("Retrieving documents similar to query...")
    retrieved_docs = retriever.invoke(query)
    log.info("Retrieved %d documents", len(retrieved_docs))

    rag_chain = build_rag_chain(retriever)
    log.info("Asking the RAG pipeline a question...")
    log.info("Question: %s", query)
    response = rag_chain.invoke(query)
    log.info("Response: %s", response)
    log.info("RAG pipeline complete")


if __name__ == "__main__":
    main()
