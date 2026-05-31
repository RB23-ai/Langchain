#!/usr/bin/env python
"""
Document Loader: Web

Uses WebBaseLoader to scrape static web pages.
"""

from langchain_community.document_loaders import WebBaseLoader

url = "https://dev.to/ruchika_bhat_876f8530fa3b/the-thinking-machines-how-ai-learned-to-reason-step-by-step-7eg"
loader = WebBaseLoader(url)
documents = loader.load()
print(f"Loaded {len(documents)} documents")
print(documents[0].page_content[:500])