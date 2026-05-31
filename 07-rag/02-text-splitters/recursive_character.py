#!/usr/bin/env python
"""
Text Splitter: RecursiveCharacterTextSplitter

Splits text by trying separators in order: ["\n\n", "\n", " ", ""]
Best for general text.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Paragraph one. Here is some text.

Paragraph two. More content here.

Paragraph three. Final paragraph."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10,
    separators=["\n\n", "\n", " ", ""]
)
chunks = splitter.split_text(text)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {chunk}")