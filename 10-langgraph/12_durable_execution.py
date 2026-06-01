#!/usr/bin/env python
"""
12_durable_execution.py – Production Checkpointer with SQLite

Uses SqliteSaver to persist state across restarts.
"""

from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_core.messages import HumanMessage, AIMessage
import time

def process(state: MessagesState) -> dict:
    # Simulate a long operation
    time.sleep(1)
    return {"messages": [AIMessage(content="Processed after long work")]}

builder = StateGraph(MessagesState)
builder.add_node("process", process)
builder.add_edge(START, "process")
builder.add_edge("process", END)

with SqliteSaver.from_conn_string("durable.db") as checkpointer:
    graph = builder.compile(checkpointer=checkpointer)

    config = {"configurable": {"thread_id": "job-1"}}
    # First run – will process
    result = graph.invoke({"messages": [HumanMessage(content="Start")]}, config)
    print(result["messages"][-1].content)

    # Even if the program restarts, we can resume:
    # state = graph.get_state(config)
    # print(state.values)