import os
from langchain_chroma import Chroma
# Open source embeddings from Hugging Face
from langchain_community.embeddings import HuggingFaceEmbeddings
# Library for interacting with AWS Bedrock
from langchain_aws import BedrockLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

print("RAG pipeline")

# Initialize the vectorstore to a Chroma client with default settings
vectorstore = Chroma(
    collection_name="demo", 
    embedding_function=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
    persist_directory=".")

# Get the top 6 most similar documents to the query.
print("Retrieving documents similar to query...")
query = "What are the approaches to Task Decomposition?"
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
retrieved_docs = retriever.invoke(query)
print(f"Retrieved {len(retrieved_docs)} documents")

# Initialize the Bedrock client with the Meta's Llama 3 8b model
print("Initializing Bedrock client...")
llm = BedrockLLM(model_id="meta.llama3-8b-instruct-v1:0")

# Based on https://smith.langchain.com/hub/rlm/rag-prompt
template = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise. 

Question: {question} 

Context: {context} 

Answer:
"""

prompt_template = PromptTemplate.from_template(template)

# Format the documents by separating them with newlines
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt_template
    | llm
    | StrOutputParser()
)

# Ask the RAG pipeline a question
print("Asking the RAG pipeline a question...")
print(f"\nQuestion: {query}")
response = rag_chain.invoke(query)

print(f"\nResponse: {response}")
print("\nRAG pipeline complete")

