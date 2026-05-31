#!/usr/bin/env python
"""
Embeddings: HuggingFace (local, free)

Uses BAAI/bge-small-en-v1.5 – good quality, small footprint.
No API key required.
"""

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
texts = ["Hello world", "LangChain is great"]
vectors = embeddings.embed_documents(texts)
print(f"Dimension: {len(vectors[0])}")
print(f"First few values: {vectors[0][:5]}")