#!/usr/bin/env python
"""
Text Splitter: SemanticChunker

Splits based on embedding similarity. Chunks where semantic shift is high.
Requires an embedding model.
"""

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

text = """The quick brown fox jumps over the lazy dog.
This is a completely different topic.
Then we return to the fox again. It is still quick."""

splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=95
)
chunks = splitter.split_text(text)
print(f"Number of semantic chunks: {len(chunks)}")