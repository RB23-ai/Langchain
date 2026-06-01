#!/usr/bin/env python
"""
06_store_cross_thread.py – Long‑Term Memory Across Threads

Uses LangGraph's Store to remember user preferences across different sessions.
"""

from langgraph.graph import StateGraph, START, END
from langgraph.store import InMemoryStore
from langgraph.checkpoint import MemorySaver
from typing import TypedDict

class State(TypedDict):
    user_id: str
    message: str
    response: str

def remember_node(state: State, store) -> dict:
    user_id = state["user_id"]
    # Get previous preferences (if any)
    prefs = store.get(("user_prefs", user_id), "preferences")
    if not prefs:
        # First time – store something
        store.put(("user_prefs", user_id), "preferences", {"language": "English"})
        return {"response": "Welcome! I've set your language to English."}
    else:
        return {"response": f"Your preferences: {prefs}"}

builder = StateGraph(State)
builder.add_node("remember", remember_node)
builder.add_edge(START, "remember")
builder.add_edge("remember", END)

store = InMemoryStore()
checkpointer = MemorySaver()
graph = builder.compile(store=store, checkpointer=checkpointer)

if __name__ == "__main__":
    config1 = {"configurable": {"thread_id": "thread1", "user_id": "alice"}}
    config2 = {"configurable": {"thread_id": "thread2", "user_id": "alice"}}

    # First session – store preferences
    res1 = graph.invoke({"user_id": "alice", "message": "Hi"}, config1)
    print(res1["response"])

    # Second session – same user, retrieves stored preferences
    res2 = graph.invoke({"user_id": "alice", "message": "What do you know about me?"}, config2)
    print(res2["response"])