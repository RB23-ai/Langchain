#!/usr/bin/env python
"""
Retriever: MMR (Maximal Marginal Relevance)

Balances relevance and diversity.
Use when results are redundant.
"""

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

docs = ["Cat is an animal.", "Kitten is a young cat.", "Car is a vehicle.", "Cat likes milk."]
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(docs, embeddings)

# MMR retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 2, "fetch_k": 4, "lambda_mult": 0.5}
)
results = retriever.get_relevant_documents("cat")
for r in results:
    print(r.page_content)