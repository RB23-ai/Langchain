# -*- coding: utf-8 -*-
"""Main entry point for the LangChain Weather Agent"""

import os
from dotenv import load_dotenv
from agents.weather_agent import WeatherAgent


def load_environment():
    """Load environment variables from .env file"""
    # Try to load from current directory
    if os.path.exists(".env"):
        load_dotenv()
        print("✓ Environment variables loaded from .env file")
    else:
        print("⚠ .env file not found. Using system environment variables.")
    
    # Check for required environment variables
    required_vars = ["OPENAI_API_KEY"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f" Missing required environment variables: {', '.join(missing_vars)}")
        print("Please set them in your .env file or system environment.")
        exit(1)


def main():
    """Main function to run the weather agent"""
    # Load environment variables
    load_environment()
    
    print("=" * 50)
    print("  LangChain Weather Agent")
    print("=" * 50)
    
    # Initialize the agent
    print("\nInitializing Weather Agent")
    agent = WeatherAgent()
    print("Agent initialized")
    
    # Example queries
    example_queries = [
        "Find the capital of Madhya Pradesh, then find its current weather condition",
        "What's the weather like in Tokyo?",
        "Find the population of Paris and then check its weather",
        "Compare the weather between New York and London"
    ]
    
    while True:
        print("\n" + "=" * 50)
        print("\nExample queries you can try:")
        for i, query in enumerate(example_queries, 1):
            print(f"{i}. {query}")
        
        print("\nEnter your query (or 'quit' to exit):")
        user_query = input("> ").strip()
        
        if user_query.lower() in ['quit', 'exit', 'q']:
            print("\nBye")
            break
        
        if not user_query:
            continue
        
        print(f"\n Processing: '{user_query}'")
        print("-" * 30)
        
        # Get response from agent
        response = agent.get_formatted_response(user_query)
        
        print("\n Response:")
        print("-" * 30)
        print(response)
        print("-" * 30)


if __name__ == "__main__":
    main()