#!/usr/bin/env python
"""
Module 08-03: Parallel Tool Calls

Modern LLMs (GPT-4o, Claude 3.5, Gemini) can request multiple tool calls in a single response.
LangChain's ToolNode executes them in parallel, improving performance.
"""

from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import ToolNode
import time

# ------------------------------------------------------------
# 1. Define tools with simulated delays to demonstrate parallelism
# ------------------------------------------------------------
@tool
def slow_add(a: int, b: int) -> str:
    """Add two numbers (simulated slow operation)."""
    time.sleep(1)  # Simulate network/processing delay
    return str(a + b)

@tool
def slow_multiply(a: int, b: int) -> str:
    """Multiply two numbers (simulated slow)."""
    time.sleep(1)
    return str(a * b)

@tool
def get_time() -> str:
    """Get current timestamp."""
    from datetime import datetime
    return datetime.now().isoformat()

tools = [slow_add, slow_multiply, get_time]

# ------------------------------------------------------------
# 2. Bind tools to LLM
# ------------------------------------------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm_with_tools = llm.bind_tools(tools)
tool_node = ToolNode(tools)

# ------------------------------------------------------------
# 3. Simulate a query that triggers parallel tool calls
# ------------------------------------------------------------
def parallel_demo():
    print("=" * 60)
    print("Parallel Tool Calls Demo")
    print("=" * 60)

    user_input = "Calculate 5 + 3, then multiply 4 * 7, and also give me the current time."
    print(f"User: {user_input}\n")

    # First, get the LLM's tool call request
    response = llm_with_tools.invoke([HumanMessage(content=user_input)])

    if response.tool_calls:
        print(f"LLM requested {len(response.tool_calls)} tool calls:")
        for tc in response.tool_calls:
            print(f"  - {tc['name']}({tc['args']})")

        # Execute them in parallel via ToolNode
        print("\nExecuting tool calls in parallel...")
        start = time.time()
        result = tool_node.invoke({"messages": [response]})
        elapsed = time.time() - start

        # Extract results
        for msg in result["messages"]:
            if isinstance(msg, ToolMessage):
                print(f"  {msg.name} → {msg.content}")

        print(f"\n⏱️  Total execution time: {elapsed:.2f}s")
        print("   (Sequential would take ~3s, parallel ~1s)\n")
    else:
        print("No tool calls requested.")

# ------------------------------------------------------------
# 4. Run demo
# ------------------------------------------------------------
if __name__ == "__main__":
    parallel_demo()