from langchain_anthropic import ChatAnthropic
from langchain_neo4j import GraphCypherQAChain, Neo4jGraph
from langchain.prompts import PromptTemplate

import os
import dotenv
dotenv.load_dotenv()
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_user = os.getenv("NEO4J_USER")
neo4j_password = os.getenv("NEO4J_PASSWORD")

llm = ChatAnthropic(
    model="claude-3-sonnet-20240229",
    temperature=0
)

graph = Neo4jGraph(
    url=neo4j_uri ,
    username=neo4j_user,
    password=neo4j_password
)

CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher to answer questions about movies and provide recommendations.
Convert the user's question based on the schema.

Schema: {schema}
Question: {question}
"""

cypher_generation_prompt = PromptTemplate(
    template=CYPHER_GENERATION_TEMPLATE,
    input_variables=["schema", "question"],
)

cypher_chain = GraphCypherQAChain.from_llm(
    llm,
    graph=graph,
    cypher_prompt=cypher_generation_prompt,
    verbose=True,
    allow_dangerous_requests=True
)

query = "What is the tagline of the movie Top Gun?"
print("\nQuery:")
print(query)

print("\nGraph Schema:")
print(graph.schema)

cypher_chain.invoke({"query": "What is the tagline of the movie Top Gun?"})