#!/usr/bin/env python
"""
RAG Pattern: Adaptive RAG

Router decides retrieval strategy based on query complexity.
"""

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

def router(query: str) -> str:
    prompt = f"Classify query complexity: simple, medium, or complex:\n{query}"
    return llm.invoke(prompt).content.strip().lower()

def retrieve_simple(query):
    return f"Simple answer for {query}"
def retrieve_medium(query):
    return f"Detailed answer with examples for {query}"
def retrieve_complex(query):
    return f"Multi-step analysis for {query}"

query = "Explain quantum entanglement"
level = router(query)
if level == "simple":
    print(retrieve_simple(query))
elif level == "medium":
    print(retrieve_medium(query))
else:
    print(retrieve_complex(query))