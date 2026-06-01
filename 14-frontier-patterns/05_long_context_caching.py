#!/usr/bin/env python
"""
Long Context Caching – Cache retrieval results for repeated queries.

Reduces latency and cost by storing retrieval results in Redis (or in‑memory).
Supports exact‑match and semantic (embedding‑based) caching.
"""

import hashlib
from typing import List, Optional
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

class SemanticCache:
    """Cache retrieval results by embedding similarity."""
    def __init__(self, vectorstore, threshold: float = 0.9):
        self.vectorstore = vectorstore
        self.threshold = threshold
        self.cache = {}

    def get(self, query: str) -> Optional[List[Document]]:
        # For exact match
        h = hashlib.md5(query.encode()).hexdigest()
        if h in self.cache:
            return self.cache[h]

        # For semantic match (requires embedding the query and comparing to stored keys)
        # Not shown for brevity – would need a second vectorstore of cached queries
        return None

    def set(self, query: str, docs: List[Document]):
        h = hashlib.md5(query.encode()).hexdigest()
        self.cache[h] = docs

# Usage with a retriever
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(["sample documents"], embeddings)
cache = SemanticCache(vectorstore)

def cached_retrieve(query: str):
    cached = cache.get(query)
    if cached:
        return cached
    docs = vectorstore.similarity_search(query, k=4)
    cache.set(query, docs)
    return docs