"""
Long Context Caching – Reduce latency and cost by caching retrieval results.

Caches results of similarity searches for repeated or similar queries.
Uses LRU eviction and TTL (time‑to‑live). Can be extended to use Redis in production.
"""

import hashlib
from datetime import datetime, timedelta
from typing import List, Optional
from langchain.schema import Document

class LRUCache:
    """Simple in‑memory LRU cache with TTL support."""
    def __init__(self, capacity: int = 100, ttl_seconds: int = 3600):
        self.capacity = capacity
        self.ttl = timedelta(seconds=ttl_seconds)
        self.cache = {}
        self.timestamps = {}

    def _hash_key(self, key: str) -> str:
        """Use MD5 to normalize long query strings."""
        return hashlib.md5(key.encode()).hexdigest()

    def get(self, query: str) -> Optional[List[Document]]:
        h = self._hash_key(query)
        if h in self.cache:
            if datetime.now() - self.timestamps[h] < self.ttl:
                return self.cache[h]
            else:
                # Expired
                del self.cache[h]
                del self.timestamps[h]
        return None

    def set(self, query: str, docs: List[Document]):
        h = self._hash_key(query)
        if len(self.cache) >= self.capacity:
            # Evict the oldest entry
            oldest_key = min(self.timestamps, key=self.timestamps.get)
            del self.cache[oldest_key]
            del self.timestamps[oldest_key]
        self.cache[h] = docs
        self.timestamps[h] = datetime.now()

class CachedVectorStore:
    """
    Wrapper around a vector store that caches retrieval results.
    """
    def __init__(self, vectorstore, cache: LRUCache = None):
        self.vectorstore = vectorstore
        self.cache = cache or LRUCache()

    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        # Check cache first
        cached = self.cache.get(query)
        if cached is not None:
            print(f"[Cache hit] Returning cached results for query: {query[:50]}...")
            return cached
        # Cache miss – perform actual search
        docs = self.vectorstore.similarity_search(query, k=k)
        self.cache.set(query, docs)
        print(f"[Cache miss] Stored results for query: {query[:50]}...")
        return docs

# Example usage
if __name__ == "__main__":
    from langchain_openai import OpenAIEmbeddings
    from langchain_community.vectorstores import FAISS

    embeddings = OpenAIEmbeddings()
    texts = ["Doc1: LangChain is awesome.", "Doc2: Caching saves money.", "Doc3: Advanced RAG techniques."]
    vectorstore = FAISS.from_texts(texts, embeddings)

    cached_retriever = CachedVectorStore(vectorstore, cache=LRUCache(capacity=2, ttl_seconds=300))

    # First call – cache miss
    docs1 = cached_retriever.similarity_search("LangChain")
    # Second call with same query – cache hit
    docs2 = cached_retriever.similarity_search("LangChain")

    print("Number of retrieved docs:", len(docs2))
    print("Page content:", docs2[0].page_content)