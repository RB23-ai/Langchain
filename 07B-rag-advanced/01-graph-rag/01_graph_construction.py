"""
Graph RAG – Build a knowledge graph from documents using LLM.
Extracts entities and relationships to create a graph structure.
"""

import networkx as nx
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import json

def extract_entities_relations(text: str) -> dict:
    """Use LLM to extract entities and relations."""
    prompt = PromptTemplate.from_template("""
    Extract entities and relationships from the following text.
    Return as JSON: {"entities": [{"name": "...", "type": "..."}], "relations": [{"from": "...", "to": "...", "relation": "..."}]}
    Text: {text}
    """)
    chain = prompt | ChatOpenAI(model="gpt-4o-mini", temperature=0)
    result = chain.invoke({"text": text})
    return json.loads(result.content)

def build_graph(documents):
    """Build NetworkX graph from document chunks."""
    G = nx.Graph()
    for doc in documents:
        extracted = extract_entities_relations(doc.page_content)
        for ent in extracted.get("entities", []):
            G.add_node(ent["name"], type=ent.get("type", "unknown"))
        for rel in extracted.get("relations", []):
            G.add_edge(rel["from"], rel["to"], relation=rel["relation"])
    return G

if __name__ == "__main__":
    sample_docs = [{"page_content": "Alice works at OpenAI. Bob is a researcher at Google."}]
    # Convert to Document objects if needed
    # graph = build_graph(sample_docs)
    # print(f"Nodes: {graph.nodes()}, Edges: {graph.edges()}")