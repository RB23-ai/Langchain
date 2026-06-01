#!/usr/bin/env python
"""
Module 09-03: Custom Tools Agent

An agent equipped with multiple custom tools: calculator, weather, and word length.
"""

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

# ------------------------------------------------------------------
# 1. Custom tools
# ------------------------------------------------------------------
@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    # Mock weather data – replace with real API
    weather = {"paris": "22°C sunny", "london": "15°C cloudy", "tokyo": "28°C humid"}
    return weather.get(city.lower(), f"No weather data for {city}")

@tool
def word_length(word: str) -> str:
    """Return the number of characters in a word."""
    return str(len(word))

# ------------------------------------------------------------------
# 2. Create agent with all tools
# ------------------------------------------------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [calculator, get_weather, word_length]
agent = create_agent(llm, tools=tools, system_prompt="You are a helpful assistant with tools for math, weather, and word length.")

# ------------------------------------------------------------------
# 3. Test the agent
# ------------------------------------------------------------------
if __name__ == "__main__":
    queries = [
        "What is 25 * 4 + 10?",
        "What's the weather in Paris?",
        "How many letters are in 'supercalifragilisticexpialidocious'?"
    ]
    for q in queries:
        print(f"\nUser: {q}")
        result = agent.invoke({"messages": [("user", q)]})
        print(f"Agent: {result['messages'][-1].content}")