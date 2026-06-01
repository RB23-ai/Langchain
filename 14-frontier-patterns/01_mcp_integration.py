#!/usr/bin/env python
"""
MCP Integration – Model Context Protocol (introduced by Anthropic).

MCP is the emerging standard for connecting LLMs to external tools and data sources.
LangChain 1.0+ provides first‑class MCP client support via langchain-mcp-adapters.
"""

import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

async def mcp_agent():
    # Connect to one or more MCP servers
    client = MultiServerMCPClient({
        "math_server": {
            "command": "python",
            "args": ["math_server.py"],  # your MCP server script
            "transport": "stdio"
        },
        "weather_server": {
            "url": "http://localhost:8000/mcp",
            "transport": "sse"
        }
    })

    # Discover and load tools from all servers
    tools = await client.get_tools()
    llm = ChatOpenAI(model="gpt-4o-mini")
    agent = create_agent(llm, tools)
    return agent

# Example MCP server (math_server.py) would expose tools like `add`, `multiply`