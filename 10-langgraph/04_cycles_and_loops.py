#!/usr/bin/env python
"""
04_cycles_and_loops.py – Looping Back for Retries

Implements a simple retry loop: if answer is "bad", try again.
"""

from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    attempt: int
    finished: bool
    result: str

def attempt_node(state: State) -> dict:
    attempt = state.get("attempt", 0) + 1
    # Simulate: first two attempts fail, third succeeds
    if attempt < 3:
        return {"attempt": attempt, "finished": False, "result": f"Attempt {attempt} failed"}
    else:
        return {"attempt": attempt, "finished": True, "result": "Success!"}

def should_continue(state: State) -> bool:
    return not state["finished"]

builder = StateGraph(State)
builder.add_node("attempt", attempt_node)
builder.set_entry_point("attempt")
builder.add_conditional_edges("attempt", should_continue, {True: "attempt", False: END})

graph = builder.compile()

if __name__ == "__main__":
    result = graph.invoke({"attempt": 0, "finished": False})
    print(result["result"])