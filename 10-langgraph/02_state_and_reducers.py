#!/usr/bin/env python
"""
02_state_and_reducers.py – Typed State and Reducers

Shows how to use reducers (e.g., add_messages) to merge state updates.
"""

from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from typing import TypedDict, Annotated

class State(TypedDict):
    messages: Annotated[list, add_messages]  # appends, not overwrites
    count: int

def node_a(state: State) -> dict:
    return {"messages": [("ai", "Hello from node A")], "count": state.get("count", 0) + 1}

def node_b(state: State) -> dict:
    return {"messages": [("ai", "Hello from node B")], "count": state.get("count", 0) + 1}

builder = StateGraph(State)
builder.add_node("a", node_a)
builder.add_node("b", node_b)
builder.set_entry_point("a")
builder.add_edge("a", "b")
builder.add_edge("b", END)

graph = builder.compile()

if __name__ == "__main__":
    initial = {"messages": [], "count": 0}
    result = graph.invoke(initial)
    print("Messages:", result["messages"])
    print("Count:", result["count"])