# Introduction

Neo4j is an enterprise grade, high speed, native graph database that stores information about nodes and edges.

In this example we'll show several ways to use Neo4j in language chains including conversation memory, knowledge graph queries, semantic search and as a vector store.

# Dependencies

All of the dependencies listed below need to be in place before running the code.

 - Python virtual environment
 - Run Neo4j in a container
 - Seed the graph with data
 - Environment variables

## Python Virtual Environment

 - Move to the Neo4j folder
   - `cd <Neo4j>`
 - Create a virtual environment
   - On Mac: `python3 -m venv .venv`
   - On Windows: `python -m venv .venv`
 - Activate the virtual environment
   - On Mac: `source .venv/bin/activate`
   - On Windows: `.venv\Scripts\activate`
 - Install dependencies
   - On Mac: `pip3 install -r requirements.txt`
   - On Windows: `pip install -r requirements.txt`
 - Call a specific script
   - On Mac: `python3 <script_name>.py`
   - On Windows: `python <script_name>.py`
 - Deactivate virtual environment
   - `deactivate`

## Run Neo4j in a container

Install Docker and run a Neo4j graph database instance.

```shell
docker run \         
    --restart always \                     
    --publish=7474:7474 \ --publish=7687:7687 --env NEO4J_PLUGINS='["apoc"]' \
    neo4j:5.26.0 
```

## Seed the graph with data

From the Neo4j console, follow the built in guide for a movie graph. `:guide movie-graph`

## Environment Variables

Create a file named `.env` with the contents shown below

```
NEO4J_URI=<address>
NEO4J_USER=<user>
NEO4J_PASSWORD=<password>
```

# Example output

## simple.py

```text
python3 simple.py

Data for Top Gun:
[{'m': {'tagline': 'I feel the need, the need for speed.', 'title': 'Top Gun', 'released': 1986}}]

Graph Schema:
Node properties:
Movie {title: STRING, tagline: STRING, released: INTEGER}
Person {born: INTEGER, name: STRING}
Relationship properties:
ACTED_IN {roles: LIST}
REVIEWED {summary: STRING, rating: INTEGER}
The relationships:
(:Person)-[:ACTED_IN]->(:Movie)
(:Person)-[:DIRECTED]->(:Movie)
(:Person)-[:PRODUCED]->(:Movie)
(:Person)-[:WROTE]->(:Movie)
(:Person)-[:FOLLOWS]->(:Person)
(:Person)-[:REVIEWED]->(:Movie)
```

# Resources

- https://neo4j.com/docs/operations-manual/current/docker/introduction/#docker-image
- https://neo4j.com/docs/operations-manual/current/docker/plugins/