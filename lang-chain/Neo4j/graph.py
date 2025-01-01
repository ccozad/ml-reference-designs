from langchain_anthropic import ChatAnthropic
from langchain_neo4j import GraphCypherQAChain, Neo4jGraph

model = ChatAnthropic(model='claude-3-opus-20240229')

