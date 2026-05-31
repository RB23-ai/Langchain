#!/usr/bin/env python
"""
Document Loader: Notion

Loads Markdown files exported from Notion.
"""

from langchain_community.document_loaders import NotionDirectoryLoader

loader = NotionDirectoryLoader("notion_export/")
documents = loader.load()
print(f"Loaded {len(documents)} pages")