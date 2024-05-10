# Introduction 

LangChain is a framework for developing applications powered by large language models (LLMs) https://python.langchain.com/v0.1/docs/get_started/introduction

# API Terms

## langchain namespace

https://api.python.langchain.com/en/latest/langchain_api_reference.html

 - **Agents** 
   - An **agent** is a class that uses an LLM to choose a sequence of actions to take.
   - Agents use **Tools** and **Toolkits** for actions
 - **Callbacks**
   - **Callback handlers** allow listening to events in LangChain.
 - **Chains**
   - Sequence of calls to components.
   - **Chains** can
     - Have state
     - Can be observed using **Callbacks**
     - Can compose components and other chains
 - **Embedding models**
   - Wrappers around models that represent information encoding as numerical data LLM models can process
 - **Evaluation chains** 
   - Chains that can grade the output of primatives
   - Common evaluations
     - Compare a response with ground truth
     - Compare the output of two models
     - Calculate the difference outputs
 - **Hub**
   - Read and write a community collection of prompts
   - https://smith.langchain.com/hub
 - **Indexes**
   - An **Index** Helps avoid writing duplicated content into a vectorstore and to avoid overwiting content if it is unchanged
 - **Memory**
   - Holds state for a Chain
 - **Retrievers**
   - A **Retriever** returns documents given a text query
   - More general than a vector store
 - **Storage**
   - Implementations of key value stores and storage helpers