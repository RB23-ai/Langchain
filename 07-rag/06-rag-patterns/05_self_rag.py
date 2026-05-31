#!/usr/bin/env python
"""
RAG Pattern: Self‑RAG (Reflection)

Generate an answer, then reflect on its quality and decide whether to retrieve again.
"""

from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    question: str
    answer: str
    iterations: int

def generate(state: State):
    llm = ChatOpenAI(model="gpt-4o-mini")
    answer = llm.invoke(state["question"]).content
    return {"answer": answer, "iterations": state.get("iterations", 0) + 1}

def reflect(state: State):
    llm = ChatOpenAI(model="gpt-4o-mini")
    reflection = llm.invoke(f"Rate this answer from 1-10: {state['answer']}").content
    return {"reflection": reflection}

def should_continue(state: State):
    # If iterations < 2 and low rating, loop back
    return "generate" if state["iterations"] < 2 and "bad" in state.get("reflection", "").lower() else END

builder = StateGraph(State)
builder.add_node("generate", generate)
builder.add_node("reflect", reflect)
builder.set_entry_point("generate")
builder.add_edge("generate", "reflect")
builder.add_conditional_edges("reflect", should_continue)
graph = builder.compile()
result = graph.invoke({"question": "What is Self‑RAG?"})
print(result["answer"])