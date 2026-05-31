#!/usr/bin/env python
"""
Text Splitter: Code Splitter

Uses RecursiveCharacterTextSplitter with language-specific separators.
Respects function and class boundaries.
"""

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    Language
)

python_code = """
def hello():
    print("Hello, world!")

class Greeting:
    def __init__(self, name):
        self.name = name

    def say(self):
        return f"Hello {self.name}"
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=20
)
chunks = splitter.split_text(python_code)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i}:\n{chunk}\n")