#!/usr/bin/env python
"""
Retriever: MultiQueryRetriever

Generates multiple query variants using an LLM to improve recall.
"""

from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
docs = ["Paris is capital of France", "Tokyo is capital of Japan"]
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(docs, embeddings)

retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(),
    llm=llm
)
results = retriever.get_relevant_documents("French capital")
for r in results:
    print(r.page_content)