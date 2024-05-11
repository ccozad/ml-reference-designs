import os
# Our open source vectorstore
from langchain_chroma import Chroma

# OpenAI embeddings, and chat model accessed remotely using an OpenAI API key
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# Prompt template for formatting the input to the language model
from langchain_core.prompts import PromptTemplate
# Output parser for parsing the output of the language model
from langchain_core.output_parsers import StrOutputParser
# Passthrough runnable for passing the input to the prompt template
from langchain_core.runnables import RunnablePassthrough

print("RAG pipeline")

# Load the OpenAI API key from the environment.
print("Loading OpenAI API key...")
import dotenv
dotenv.load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the vectorstore to a Chroma client with default settings
vectorstore = Chroma(
    collection_name="demo", 
    embedding_function=OpenAIEmbeddings(),
    persist_directory=".")

# Get the top 6 most similar documents to the query.
print("Retrieving documents similar to query...")
query = "What are the approaches to Task Decomposition?"
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
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

