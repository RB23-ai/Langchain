#!/usr/bin/env python
"""
Retriever: ParentDocumentRetriever

Embed small child chunks but return larger parent chunks for context.
"""

from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

parent_splitter = RecursiveCharacterTextSplitter(chunk_size=2000)
child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)
embeddings = OpenAIEmbeddings()
vectorstore = Chroma(embedding_function=embeddings)
docstore = InMemoryStore()

retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=docstore,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)
# Add documents
retriever.add_documents([{"page_content": "Long document..."}])