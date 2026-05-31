#!/usr/bin/env python
"""
Embeddings: OpenAI

Uses OpenAI's text-embedding-3-small model.
Requires OPENAI_API_KEY.
"""

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
texts = ["Hello world", "LangChain is great", "Embeddings are vectors"]
vectors = embeddings.embed_documents(texts)
query_vec = embeddings.embed_query("What is LangChain?")
print(f"Dimension: {len(vectors[0])}")
print(f"Similarity (doc0 vs query): {sum(a*b for a,b in zip(vectors[0], query_vec)):.4f}")