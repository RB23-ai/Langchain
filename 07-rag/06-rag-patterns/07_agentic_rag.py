#!/usr/bin/env python
"""
RAG Pattern: Agentic RAG

Agent decides when and how to retrieve, possibly multiple times.
Uses LangGraph with tool-calling.
"""

from langgraph.graph import StateGraph, END
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from typing import TypedDict, List

@tool
def search(query: str) -> str:
    """Search knowledge base."""
    return f"Result for {query}: [simulated]"

class State(TypedDict):
    messages: List
    answer: str

def agent(state: State):
    llm = ChatOpenAI(model="gpt-4o-mini").bind_tools([search])
    response = llm.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}

def tools(state: State):
    # Execute tool calls
    return {"messages": state["messages"]}

def should_continue(state: State):
    last = state["messages"][-1]
    return "tools" if hasattr(last, "tool_calls") and last.tool_calls else END

builder = StateGraph(State)
builder.add_node("agent", agent)
builder.add_node("tools", tools)
builder.set_entry_point("agent")
builder.add_conditional_edges("agent", should_continue)
builder.add_edge("tools", "agent")
graph = builder.compile()

result = graph.invoke({"messages": [("user", "What is RAG?")]})
print(result["messages"][-1].content)