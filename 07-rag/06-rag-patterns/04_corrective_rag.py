#!/usr/bin/env python
"""
RAG Pattern: CRAG (Corrective RAG) with LangGraph

Evaluates retrieved documents; if irrelevant, uses web search fallback.
"""

from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun

class State(TypedDict):
    question: str
    docs: List[str]
    answer: str

def retrieve(state: State):
    # Mock retrieval – replace with real vectorstore
    docs = ["Relevant doc about " + state["question"]]
    return {"docs": docs}

def grade(state: State):
    # LLM grades relevance
    llm = ChatOpenAI(model="gpt-4o-mini")
    grade = llm.invoke(f"Is this relevant to '{state['question']}'? {state['docs'][0]}").content
    return {"grade": grade}

def web_search(state: State):
    search = DuckDuckGoSearchRun()
    result = search.run(state["question"])
    return {"docs": [result], "answer": result}

def generate(state: State):
    llm = ChatOpenAI(model="gpt-4o-mini")
    answer = llm.invoke(f"Answer {state['question']} using {state['docs']}").content
    return {"answer": answer}

def router(state: State):
    return "web_search" if "not relevant" in state.get("grade", "").lower() else "generate"

builder = StateGraph(State)
builder.add_node("retrieve", retrieve)
builder.add_node("grade", grade)
builder.add_node("web_search", web_search)
builder.add_node("generate", generate)
builder.set_entry_point("retrieve")
builder.add_edge("retrieve", "grade")
builder.add_conditional_edges("grade", router, {"web_search": "web_search", "generate": "generate"})
builder.add_edge("web_search", "generate")
builder.add_edge("generate", END)
graph = builder.compile()
result = graph.invoke({"question": "What is CRAG?"})
print(result["answer"])