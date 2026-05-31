#!/usr/bin/env python
"""
Document Loader: GitHub

Clones a GitHub repository and loads all relevant files.
"""

from langchain_community.document_loaders import GitLoader

loader = GitLoader(
    clone_url="https://github.com/langchain-ai/langchain",
    repo_path="./langchain_repo",
    branch="master",
)
documents = loader.load()
print(f"Loaded {len(documents)} files")