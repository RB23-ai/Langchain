"""
Hybrid Text‑Graph RAG – Combine dense text retrieval with graph traversal.
Retrieve text chunks, then expand via graph edges.
"""

from langchain.retrievers import EnsembleRetriever
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

class HybridTextGraphRetriever:
    def __init__(self, text_retriever, graph, max_graph_expansions=2):
        self.text_retriever = text_retriever
        self.graph = graph
        self.max_expansions = max_graph_expansions

    def expand_via_graph(self, seed_entities):
        """From seed entities, traverse graph to get related entities."""
        expanded = set(seed_entities)
        for _ in range(self.max_expansions):
            new_nodes = set()
            for node in expanded:
                new_nodes.update(self.graph.neighbors(node))
            expanded.update(new_nodes)
        return expanded

    def retrieve(self, query):
        # Step 1: text retrieval
        text_docs = self.text_retriever.get_relevant_documents(query)
        # Extract entity mentions from text (simplified)
        # In real: use NER or LLM
        entities = [doc.metadata.get("entity", "") for doc in text_docs if "entity" in doc.metadata]
        # Step 2: graph expansion
        expanded_entities = self.expand_via_graph(entities)
        # Fetch graph context for these entities
        graph_context = [f"Entity: {e}" for e in expanded_entities]
        return text_docs + [Document(page_content=ctx) for ctx in graph_context]

# Example usage
# embeddings = OpenAIEmbeddings()
# vectorstore = FAISS.from_texts(["Apple is a company", "Apple makes iPhones"], embeddings)
# text_retriever = vectorstore.as_retriever()
# hybrid = HybridTextGraphRetriever(text_retriever, graph)
# docs = hybrid.retrieve("Tell me about Apple")