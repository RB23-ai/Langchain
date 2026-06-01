#!/usr/bin/env python
"""
07_human_in_the_loop.py – Interrupt and Resume

Pauses before a sensitive node, waits for human input, then resumes.
"""

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint import MemorySaver
from langgraph.types import interrupt
from typing import TypedDict

class State(TypedDict):
    action: str
    approved: bool

def propose_action(state: State) -> dict:
    return {"action": "Send email to ceo@company.com"}

def request_approval(state: State) -> dict:
    # interrupt() pauses the graph and returns the human's input when resumed
    human_input = interrupt({"action": state["action"], "message": "Approve? (yes/no)"})
    approved = human_input.strip().lower() == "yes"
    return {"approved": approved}

def execute(state: State) -> dict:
    if state["approved"]:
        print("Executing action:", state["action"])
    else:
        print("Action rejected.")
    return {}

builder = StateGraph(State)
builder.add_node("propose", propose_action)
builder.add_node("approve", request_approval)
builder.add_node("execute", execute)
builder.add_edge(START, "propose")
builder.add_edge("propose", "approve")
builder.add_edge("approve", "execute")
builder.add_edge("execute", END)

checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer, interrupt_before=["approve"])

if __name__ == "__main__":
    config = {"configurable": {"thread_id": "session1"}}

    # Start – will stop before "approve"
    print("Starting graph...")
    for event in graph.stream({"action": ""}, config):
        print(event)

    # Get current state
    state = graph.get_state(config)
    print("Paused before node:", state.next)

    # Simulate human approval
    print("\nHuman approves...")
    graph.update_state(config, {"approved": True}, as_node="approve")

    # Resume
    print("Resuming...")
    for event in graph.stream(None, config):
        print(event)