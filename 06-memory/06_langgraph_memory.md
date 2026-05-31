# LangGraph Memory – Checkpointer and Store (The 1.0+ Way)

Since LangChain 1.0, all agent runtimes are built on LangGraph. LangGraph provides two distinct memory mechanisms:

## 1. Checkpointer – Short‑Term / Within‑Thread Memory

**What it does:** Saves the full graph state after every node execution. This includes messages, current node, pending edges, and any variables.

**Use cases:** Multi‑turn conversations, resumable workflows, fault tolerance.

**How it works:** A checkpointer is attached at compile time. Every time the graph executes, state is automatically persisted to a backend (in‑memory, SQLite, PostgreSQL). You resume a conversation by providing the same `thread_id`.

```python
from langgraph.graph import StateGraph, MessagesState
from langgraph.checkpoint import MemorySaver

builder = StateGraph(MessagesState)
# ... add nodes and edges ...
checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "user_123"}}
# First invocation
graph.invoke({"messages": [("user", "Hi")]}, config)
# Second invocation – remembers previous state
graph.invoke({"messages": [("user", "What was my first message?")]}, config)