#!/usr/bin/env python
"""
Token & Cost Tracking – Use get_openai_callback for precise cost calculation.

Note: For provider‑agnostic cost tracking, consider using LiteLLM or manual calculations.
"""

from langchain.callbacks import get_openai_callback
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
prompt = ChatPromptTemplate.from_template("Explain {concept} in one sentence.")
chain = prompt | model

with get_openai_callback() as cb:
    result = chain.invoke({"concept": "token tracking"})
    print(result.content)
    print("\n" + "=" * 40)
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost:.6f}")
    print("=" * 40)

# You can also collect multiple calls inside the same context:
with get_openai_callback() as cb:
    for concept in ["LLM", "RAG", "Agents"]:
        chain.invoke({"concept": concept})
    print(f"\nTotal cost for 3 calls: ${cb.total_cost:.4f}")