#!/usr/bin/env python
"""
Retriever: Similarity Search (basic)
"""

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

docs = ["Paris is capital of France", "Tokyo is capital of Japan", "Berlin is capital of Germany"]
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(docs, embeddings)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
results = retriever.get_relevant_documents("What is the capital of France?")
for r in results:
    print(r.page_content)