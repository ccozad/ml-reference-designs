import os
# Open source embeddings from Hugging Face
from langchain_community.embeddings import HuggingFaceEmbeddings

# OpenAI embeddings, and chat model accessed remotely using an OpenAI API key
from langchain_openai import ChatOpenAI

# Chin related imports
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Azure
from langchain_community.vectorstores.azuresearch import AzureSearch

print("Loading Azure credentials...")
import dotenv
dotenv.load_dotenv()
vector_store_address = os.getenv("VECTOR_STORE_ADDRESS")
vector_store_key = os.getenv("VECTOR_STORE_KEY")
vector_store_name = os.getenv("VECTOR_STORE_NAME")

print("RAG pipeline")

# Initialize the vectorstore to a Chroma client with default settings
vectorstore = AzureSearch(
    azure_search_endpoint = vector_store_address,
    azure_search_key = vector_store_key,
    index_name = vector_store_name,
    embedding_function=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2").embed_query,
    additional_search_client_options={"retry_total": 4}
)

# Get the top 6 most similar documents to the query.
print("Retrieving documents similar to query...")
query = "What are the approaches to Task Decomposition?"
retriever = vectorstore.as_retriever(search_type="similarity", k=6)
retrieved_docs = retriever.invoke(query)
print(f"Retrieved {len(retrieved_docs)} documents")

# Initiatialize the large language model
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

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

