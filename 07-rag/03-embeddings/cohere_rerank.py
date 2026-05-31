#!/usr/bin/env python
"""
Reranking: Cohere (cross-encoder)

Cohere's rerank API reorders documents by relevance.
Use after initial retrieval to improve precision.
"""

from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CohereRerank
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Dummy documents (replace with real ones)
docs = ["Paris is the capital of France.", "Tokyo is in Japan.", "Berlin is in Germany."]
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

compressor = CohereRerank(top_n=2)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retriever
)

results = compression_retriever.get_relevant_documents("What is the capital of France?")
for r in results:
    print(r.page_content)