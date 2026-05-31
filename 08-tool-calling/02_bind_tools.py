#!/usr/bin/env python
"""
Module 08-02: bind_tools() – Attaching Tools to an LLM

Once tools are defined, we use .bind_tools() to attach them to an LLM.
The LLM then decides, based on the user input, which tool (if any) to call.
"""

from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# ------------------------------------------------------------
# 1. Define tools (reused from previous example)
# ------------------------------------------------------------
@tool
def add_numbers(a: int, b: int) -> str:
    """Add two integers."""
    return str(a + b)

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    weather = {"Paris": "22°C sunny", "London": "15°C cloudy"}
    return weather.get(city, "Unknown city")

# ------------------------------------------------------------
# 2. Bind tools to LLM
# ------------------------------------------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [add_numbers, get_weather]
llm_with_tools = llm.bind_tools(tools)

# ------------------------------------------------------------
# 3. Invoke and inspect tool calls
# ------------------------------------------------------------
def show_tool_call(user_input: str):
    print(f"\nUser: {user_input}")
    response = llm_with_tools.invoke([HumanMessage(content=user_input)])

    if hasattr(response, "tool_calls") and response.tool_calls:
        for tc in response.tool_calls:
            print(f"  🔧 Tool call: {tc['name']}({tc['args']})")
    else:
        print(f"  💬 Direct answer: {response.content[:100]}...")

if __name__ == "__main__":
    print("=" * 60)
    print("bind_tools() – LLM decides when to call tools")
    print("=" * 60)

    show_tool_call("What is 15 + 27?")
    show_tool_call("What's the weather like in Paris?")
    show_tool_call("Tell me a joke.")

    # --------------------------------------------------------
    # 4. Important: ToolNode for automatic execution
    # --------------------------------------------------------
    print("\n" + "=" * 60)
    print("ToolNode – Executing tool calls automatically")
    print("=" * 60)

    from langgraph.prebuilt import ToolNode

    tool_node = ToolNode(tools)
    # Simulate an AIMessage with tool_calls
    from langchain_core.messages import AIMessage, ToolMessage

    fake_ai_message = AIMessage(
        content="",
        tool_calls=[{"name": "add_numbers", "args": {"a": 8, "b": 3}, "id": "call_1"}]
    )
    result = tool_node.invoke({"messages": [fake_ai_message]})
    print("ToolNode execution result:", result["messages"][-1].content)