#!/usr/bin/env python
"""
Deep Agents – Agents with planning, virtual filesystems, and sub‑agent spawning.

Deep Agents (popularised by LangChain's `deepagents` library) can:
- Write and read files (virtual filesystem)
- Plan tasks step by step
- Spawn sub‑agents for subtasks
"""

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

@tool
def write_file(path: str, content: str) -> str:
    """Write content to a virtual file."""
    # In production, use an in‑memory store or temp directory
    return f"Written to {path}"

@tool
def read_file(path: str) -> str:
    """Read content from a virtual file."""
    return f"Content of {path}"

@tool
def spawn_sub_agent(task: str) -> str:
    """Spawn a sub‑agent to handle a subtask."""
    # In real implementation, this would create a new agent instance
    return f"Sub‑agent completed: {task}"

llm = ChatOpenAI(model="gpt-4o")
agent = create_agent(
    llm,
    tools=[write_file, read_file, spawn_sub_agent],
    system_prompt="You are a deep agent. You can read/write files and spawn sub‑agents."
)

# Example usage (simplified)
# result = agent.invoke({"messages": [("user", "Plan a 5‑step research project")]})