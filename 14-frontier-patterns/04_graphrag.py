#!/usr/bin/env python
"""
GraphRAG – Knowledge‑Graph RAG using Neo4j.

Builds a knowledge graph from documents, then retrieves by:
- Vector similarity (text chunks)
- Graph traversal (entities and relationships)
- Community detection (global summaries)
"""

from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI

# Connect to Neo4j (running locally or in cloud)
graph = Neo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="password"
)

# Create GraphRAG QA chain
chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(model="gpt-4o", temperature=0),
    graph=graph,
    verbose=True,
    allow_dangerous_requests=True  # set to True only in controlled environments
)

# Example
# answer = chain.run("Which employees work in the Engineering department?")