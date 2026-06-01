#!/usr/bin/env python
"""
03_conditional_edges.py – Branching Based on State

Routes to different nodes depending on a condition.
"""

from langgraph.graph import StateGraph, END
from typing import TypedDict, Literal

class State(TypedDict):
    user_input: str
    route: str

def node_math(state: State) -> dict:
    return {"route": "math", "user_input": state["user_input"]}

def node_history(state: State) -> dict:
    return {"route": "history", "user_input": state["user_input"]}

def router(state: State) -> Literal["math_node", "history_node"]:
    if "math" in state["user_input"].lower():
        return "math_node"
    else:
        return "history_node"

builder = StateGraph(State)
builder.add_node("math_node", node_math)
builder.add_node("history_node", node_history)
builder.set_entry_point("math_node")  # temporary, will be overridden by conditional edge
builder.add_conditional_edges("__start__", router, {
    "math_node": "math_node",
    "history_node": "history_node"
})
builder.add_edge("math_node", END)
builder.add_edge("history_node", END)

graph = builder.compile()

if __name__ == "__main__":
    for inp in ["What is 2+2?", "Who was Napoleon?"]:
        res = graph.invoke({"user_input": inp})
        print(f"Input: {inp} → Route: {res['route']}")