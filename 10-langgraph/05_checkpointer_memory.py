#!/usr/bin/env python
"""
05_checkpointer_memory.py – Within‑Thread Persistence

Uses MemorySaver to remember state across invocations of the same thread.
"""

from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint import MemorySaver
from langchain_core.messages import HumanMessage, AIMessage

def chatbot(state: MessagesState) -> dict:
    # Simple echo bot
    last_human = state["messages"][-1].content
    return {"messages": [AIMessage(content=f"You said: {last_human}")]}

builder = StateGraph(MessagesState)
builder.add_node("chatbot", chatbot)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)

if __name__ == "__main__":
    config = {"configurable": {"thread_id": "user123"}}

    # First turn
    result1 = graph.invoke({"messages": [HumanMessage(content="Hi, I'm Alice")]}, config)
    print(result1["messages"][-1].content)

    # Second turn – remembers previous messages (state is persisted)
    result2 = graph.invoke({"messages": [HumanMessage(content="What's my name?")]}, config)
    print(result2["messages"][-1].content)