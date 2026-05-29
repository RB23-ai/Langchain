# -*- coding: utf-8 -*-
"""Weather tool for fetching weather data"""

import requests
from langchain_core.tools import tool
from typing import Dict, Any
import os


@tool
def get_weather_data(city: str) -> Dict[str, Any]:
    """
    Fetches the current weather data for a given city using Weatherstack API.
    
    Args:
        city: Name of the city
    
    Returns:
        Dictionary containing weather data
    """
    api_key = os.getenv("WEATHERSTACK_API_KEY")
    if not api_key:
        raise ValueError("WEATHERSTACK_API_KEY not found in environment variables")
    
    url = f'https://api.weatherstack.com/current?access_key={api_key}&query={city}'
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch weather data: {str(e)}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}


def format_weather_response(weather_data: Dict[str, Any]) -> str:
    """
    Formats weather data into a readable string.
    
    Args:
        weather_data: Raw weather data from API
    
    Returns:
        Formatted weather information string
    """
    if "error" in weather_data:
        return f"Error: {weather_data['error']}"
    
    if "current" not in weather_data:
        return "No current weather data available"
    
    current = weather_data["current"]
    location = weather_data.get("location", {})
    
    return f"""
Weather in {location.get('name', 'Unknown location')}:
- Temperature: {current.get('temperature', 'N/A')}°C
- Feels like: {current.get('feelslike', 'N/A')}°C
- Weather: {current.get('weather_descriptions', ['N/A'])[0]}
- Humidity: {current.get('humidity', 'N/A')}%
- Wind Speed: {current.get('wind_speed', 'N/A')} km/h
- Wind Direction: {current.get('wind_dir', 'N/A')}
- Pressure: {current.get('pressure', 'N/A')} mb
- Visibility: {current.get('visibility', 'N/A')} km
"""