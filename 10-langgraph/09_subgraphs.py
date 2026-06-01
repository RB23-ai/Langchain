#!/usr/bin/env python
"""
09_subgraphs.py – Nesting Graphs

A subgraph is a compiled graph used as a node in a parent graph.
"""

from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import HumanMessage, AIMessage

# Subgraph: simple greeting
def greet_node(state: MessagesState) -> dict:
    return {"messages": [AIMessage(content="Hello from subgraph!")]}

sub_builder = StateGraph(MessagesState)
sub_builder.add_node("greet", greet_node)
sub_builder.add_edge(START, "greet")
sub_builder.add_edge("greet", END)
subgraph = sub_builder.compile()

# Parent graph that calls subgraph
def parent_node(state: MessagesState) -> dict:
    # Invoke subgraph
    sub_result = subgraph.invoke({"messages": state["messages"]})
    return {"messages": sub_result["messages"]}

parent_builder = StateGraph(MessagesState)
parent_builder.add_node("sub", parent_node)
parent_builder.add_edge(START, "sub")
parent_builder.add_edge("sub", END)

parent_graph = parent_builder.compile()

if __name__ == "__main__":
    result = parent_graph.invoke({"messages": [HumanMessage(content="Hi")]})
    print(result["messages"][-1].content)