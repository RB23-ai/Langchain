#!/usr/bin/env python
"""
Text Splitter: TokenTextSplitter

Splits by tokens (e.g., for OpenAI models). Uses tiktoken.
"""

from langchain_text_splitters import TokenTextSplitter

text = "This is a long document. " * 100
splitter = TokenTextSplitter(chunk_size=50, chunk_overlap=10)
chunks = splitter.split_text(text)
print(f"Split into {len(chunks)} token-aligned chunks")