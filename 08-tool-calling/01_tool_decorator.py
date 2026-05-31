
---

## `08-tool-calling/01_tool_decorator.py`

```python
#!/usr/bin/env python
"""
Module 08-01: The @tool Decorator

The simplest way to create a tool. The decorator reads:
- The function name → becomes the tool name
- The docstring → becomes the tool description (the LLM reads this!)
- Type hints → become the input schema (Pydantic model)
"""

from langchain.tools import tool
from langchain_openai import ChatOpenAI

# ------------------------------------------------------------
# 1. Basic tool – a simple calculation
# ------------------------------------------------------------
@tool
def add_numbers(a: int, b: int) -> str:
    """Add two integers and return the result."""
    return str(a + b)

# ------------------------------------------------------------
# 2. Tool without arguments – returns current time
# ------------------------------------------------------------
@tool
def get_current_time() -> str:
    """Return the current date and time in ISO format."""
    from datetime import datetime
    return datetime.now().isoformat()

# ------------------------------------------------------------
# 3. Tool with more complex logic – weather (simulated)
# ------------------------------------------------------------
@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    # In production, call a real weather API.
    weather_data = {
        "Paris": "22°C, sunny",
        "London": "15°C, cloudy",
        "Tokyo": "28°C, humid"
    }
    return weather_data.get(city, f"Weather data for {city} not available")

# ------------------------------------------------------------
# 4. Inspecting a tool's properties
# ------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("Tool inspection")
    print("=" * 60)

    print(f"Tool name: {add_numbers.name}")
    print(f"Description: {add_numbers.description}")
    print(f"Arguments schema: {add_numbers.args}")
    print()

    # Test the tools directly
    print("Testing add_numbers(5, 3):", add_numbers.invoke({"a": 5, "b": 3}))
    print("Current time:", get_current_time.invoke({}))
    print("Weather in Paris:", get_weather.invoke({"city": "Paris"}))

    # --------------------------------------------------------
    # 5. What the LLM sees – we'll simulate binding
    # --------------------------------------------------------
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    tools = [add_numbers, get_current_time, get_weather]
    llm_with_tools = llm.bind_tools(tools)

    # The LLM can now decide to call these tools. This is shown in next examples.
    print("\n✅ Tools defined. They are ready to be bound to an LLM.")