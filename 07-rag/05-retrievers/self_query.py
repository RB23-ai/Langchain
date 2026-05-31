#!/usr/bin/env python
"""
Retriever: SelfQueryRetriever

Extracts metadata filters from natural language queries.
"""

from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

metadata_field_info = [
    AttributeInfo(name="source", description="Document source", type="string"),
    AttributeInfo(name="year", description="Publication year", type="integer"),
]
document_content_description = "Technical documentation"
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(
    ["Doc1 2023", "Doc2 2024"],
    embeddings,
    metadatas=[{"source": "a.pdf", "year": 2023}, {"source": "b.pdf", "year": 2024}]
)
retriever = SelfQueryRetriever.from_llm(
    llm,
    vectorstore,
    document_content_description,
    metadata_field_info,
    verbose=True
)
results = retriever.get_relevant_documents("Documents from 2024")
print(len(results))