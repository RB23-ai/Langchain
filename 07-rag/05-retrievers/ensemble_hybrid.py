#!/usr/bin/env python
"""
Retriever: EnsembleRetriever (Hybrid)

Combines BM25 (keyword) and dense (embedding) retrieval.
"""

from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

docs = ["The cat sat on the mat.", "The dog ran in the park.", "Cat and dog are pets."]
bm25_retriever = BM25Retriever.from_texts(docs, k=2)
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(docs, embeddings)
dense_retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

ensemble = EnsembleRetriever(
    retrievers=[bm25_retriever, dense_retriever],
    weights=[0.4, 0.6]
)
results = ensemble.get_relevant_documents("cat")
for r in results:
    print(r.page_content)