#!/usr/bin/env python
"""
11_multi_agent_swarm.py – Swarm Pattern (Peer‑to‑Peer Handoffs)

Agents can hand off to each other without a central supervisor.
"""

from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional

class State(TypedDict):
    messages: list
    active_agent: Optional[str]

def agent_a(state: State) -> dict:
    # Decide to hand off to agent B
    return {"messages": state["messages"] + ["A → B"], "active_agent": "agent_b"}

def agent_b(state: State) -> dict:
    # Decide to end
    return {"messages": state["messages"] + ["B finished"], "active_agent": None}

builder = StateGraph(State)
builder.add_node("agent_a", agent_a)
builder.add_node("agent_b", agent_b)

builder.set_entry_point("agent_a")
builder.add_conditional_edges("agent_a", lambda s: s["active_agent"] if s["active_agent"] else END)
builder.add_conditional_edges("agent_b", lambda s: s["active_agent"] if s["active_agent"] else END)

graph = builder.compile()

if __name__ == "__main__":
    result = graph.invoke({"messages": [], "active_agent": "agent_a"})
    print(result["messages"])