from langchain_neo4j import Neo4jGraph

import os
import dotenv
dotenv.load_dotenv()
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_user = os.getenv("NEO4J_USER")
neo4j_password = os.getenv("NEO4J_PASSWORD")

graph = Neo4jGraph(
    url=neo4j_uri ,
    username=neo4j_user,
    password=neo4j_password
)

print("\nData for Top Gun:")

result = graph.query("""
MATCH (m:Movie{title: 'Top Gun'}) 
RETURN m
""")

print(result)

print("\nGraph Schema:")
print(graph.schema)

