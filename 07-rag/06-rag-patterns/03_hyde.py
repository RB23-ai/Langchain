#!/usr/bin/env python
"""
RAG Pattern: HyDE (Hypothetical Document Embeddings)

Generate a hypothetical answer, then retrieve documents similar to that answer.
"""

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

docs = ["LangChain is a framework.", "HyDE improves RAG."]
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(docs, embeddings)

llm = ChatOpenAI(model="gpt-4o-mini")
hypothetical = llm.invoke("Answer: What is HyDE?").content
print(f"Hypothetical answer: {hypothetical}")
results = vectorstore.similarity_search(hypothetical, k=1)
print(f"Retrieved: {results[0].page_content}")