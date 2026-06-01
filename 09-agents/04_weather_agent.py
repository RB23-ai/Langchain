#!/usr/bin/env python
"""
Module 09-04: Weather Agent

A specialised agent that answers weather‑related queries using a weather API.
"""

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
import requests
import os

# ------------------------------------------------------------------
# 1. Real weather tool using OpenWeatherMap (requires API key)
# ------------------------------------------------------------------
@tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a city using OpenWeatherMap API.
    Returns temperature and conditions.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "Weather API key not configured. Set OPENWEATHER_API_KEY."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        resp = requests.get(url, timeout=5)
        data = resp.json()
        if data.get("cod") != 200:
            return f"City not found: {city}"
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        return f"{city}: {temp}°C, {condition}"
    except Exception as e:
        return f"Error fetching weather: {e}"

# ------------------------------------------------------------------
# 2. Fallback tool if API fails (simulated)
# ------------------------------------------------------------------
@tool
def fallback_weather(city: str) -> str:
    """Fallback mock weather when API unavailable."""
    weather = {"paris": "22°C sunny", "london": "15°C cloudy"}
    return weather.get(city.lower(), f"No data for {city}")

# ------------------------------------------------------------------
# 3. Create agent with weather tools
# ------------------------------------------------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
agent = create_agent(llm, tools=[get_weather, fallback_weather],
                     system_prompt="You are a weather expert. Use the weather tool to answer queries.")

if __name__ == "__main__":
    result = agent.invoke({"messages": [("user", "What's the weather like in Paris?")]})
    print(result["messages"][-1].content)