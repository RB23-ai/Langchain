#!/usr/bin/env python
"""
RAG Pattern: Query Rewriting

Rewrite the user query before retrieval to improve recall.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

rewrite_prompt = PromptTemplate.from_template("Rewrite this question to be more specific: {question}")
rewriter = rewrite_prompt | ChatOpenAI(model="gpt-4o-mini") | StrOutputParser()

original_q = "What is it?"
rewritten = rewriter.invoke({"question": original_q})
print(f"Original: {original_q}\nRewritten: {rewritten}")
# Then use rewritten for retrieval...