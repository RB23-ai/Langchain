# -*- coding: utf-8 -*-
"""Weather agent implementation"""

from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from typing import Dict, Any
import os

from tools.weather_tool import get_weather_data
from tools.search_tool import get_search_tool


class WeatherAgent:
    """Agent for handling weather-related queries with search capabilities"""
    
    def __init__(self, model_name: str = "gpt-3.5-turbo", temperature: float = 0.7):
        """
        Initialize the Weather Agent.
        
        Args:
            model_name: OpenAI model name
            temperature: Model temperature for creativity
        """
        self.llm = ChatOpenAI(
            model=model_name,
            temperature=temperature,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # Initialize tools
        self.tools = [get_search_tool(), get_weather_data]
        
        # Get ReAct prompt
        self.prompt = hub.pull("hwchase17/react")
        
        # Create agent
        self.agent = create_react_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt
        )
        
        # Create agent executor
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=5
        )
    
    def run(self, query: str) -> Dict[str, Any]:
        """
        Execute the agent with a given query.
        
        Args:
            query: User query string
        
        Returns:
            Agent response dictionary
        """
        try:
            response = self.agent_executor.invoke({"input": query})
            return response
        except Exception as e:
            return {"error": f"Agent execution failed: {str(e)}"}
    
    def get_formatted_response(self, query: str) -> str:
        """
        Get formatted response from the agent.
        
        Args:
            query: User query string
        
        Returns:
            Formatted response string
        """
        response = self.run(query)
        
        if "error" in response:
            return f"Error: {response['error']}"
        
        return response.get("output", "No output generated")