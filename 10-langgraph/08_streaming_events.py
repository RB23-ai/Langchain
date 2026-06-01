#!/usr/bin/env python
"""
08_streaming_events.py – Streaming Graph Execution Events

Streams node start/end events, token chunks, and final outputs.
"""

import asyncio
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import HumanMessage, AIMessage

async def slow_node(state: MessagesState) -> dict:
    await asyncio.sleep(0.5)
    return {"messages": [AIMessage(content="Processed")]}

builder = StateGraph(MessagesState)
builder.add_node("process", slow_node)
builder.add_edge(START, "process")
builder.add_edge("process", END)

graph = builder.compile()

async def main():
    async for event in graph.astream_events(
        {"messages": [HumanMessage(content="Hello")]},
        version="v2"
    ):
        kind = event["event"]
        if kind == "on_chain_start":
            print(f"Starting: {event['name']}")
        elif kind == "on_chain_end":
            print(f"Finished: {event['name']}")
        elif kind == "on_chain_stream":
            print(f"Stream chunk: {event['data']['chunk']}")

if __name__ == "__main__":
    asyncio.run(main())