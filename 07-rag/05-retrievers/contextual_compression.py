#!/usr/bin/env python
"""
Retriever: ContextualCompressionRetriever

Uses an LLM to extract only the relevant parts of each retrieved document.
"""

from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
compressor = LLMChainExtractor.from_llm(llm)
docs = ["Paris is the capital of France. It has many attractions."]
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(docs, embeddings)
retriever = vectorstore.as_retriever()
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retriever
)
results = compression_retriever.get_relevant_documents("What is the capital of France?")
for r in results:
    print(r.page_content)