#!/usr/bin/env python
"""
Text Splitter: MarkdownHeaderTextSplitter

Splits markdown documents based on heading levels.
Preserves hierarchical structure.
"""

from langchain_text_splitters import MarkdownHeaderTextSplitter

markdown = """
# Title
Content under title.

## Section 1
Content of section 1.

### Subsection 1.1
Detailed content.

## Section 2
Another section.
"""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
splits = splitter.split_text(markdown)
for split in splits:
    print(f"Metadata: {split.metadata}")
    print(f"Content: {split.page_content[:100]}...\n")