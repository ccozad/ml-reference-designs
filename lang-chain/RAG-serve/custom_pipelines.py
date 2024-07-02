import os

import dotenv
dotenv.load_dotenv()

from bs4 import BeautifulSoup, SoupStrainer
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

class CustomPipelines:
    def __init__(self):
        print("Initializing vectorstore...")
        self.vectorstore = Chroma(
            collection_name="demo", 
            embedding_function=OpenAIEmbeddings())

    def index_html_pipeline(self, url):
        print("Index html pipeline")
        print("Loading document from the web...")
        print(f"URL: {url}")
        loader = WebBaseLoader(
            web_paths=(url,),
            bs_kwargs=dict(
                parse_only=SoupStrainer(
                    class_=("post-content", "post-title", "post-header")
                )
            ),
        )
        docs = loader.load()
        if len(docs) == 0:
            print("No documents found")
            return False
        else:
            print(f"Document length: {len(docs[0].page_content)}")
            print("Splitting document into chunks...")
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000, 
                chunk_overlap=200)
            splits = text_splitter.split_documents(docs)
            print(f"Number of splits: {len(splits)}")

            print("Adding splits to embedding vectorstore...")
            vectorstore = self.vectorstore.add_documents(documents=splits)

            print("Index pipeline complete")
            return True

    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def rag_pipeline(self, query):
        print("RAG pipeline")

        print("Retrieving documents similar to query...")
        retriever = self.vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
        retrieved_docs = retriever.invoke(query)
        print(f"Retrieved {len(retrieved_docs)} documents")

        llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

        template = """
        You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise. 

        Question: {question} 

        Context: {context} 

        Answer:
        """

        prompt_template = PromptTemplate.from_template(template)

        rag_chain = (
            {"context": retriever | self.format_docs, "question": RunnablePassthrough()}
            | prompt_template
            | llm
            | StrOutputParser()
        )

        response = rag_chain.invoke(query)
        print("RAG pipeline complete")
        return True, response
