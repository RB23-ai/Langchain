#!/usr/bin/env python
"""
Module 09-05: Code Interpreter Agent

An agent that can execute Python code in a sandboxed environment.
WARNING: Executing arbitrary code is dangerous. This example uses a restricted
execution environment (simulated). In production, use E2B, Riza, or a Docker sandbox.
"""

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
import subprocess
import tempfile

# ------------------------------------------------------------------
# 1. Tool that executes Python code (sandboxed using subprocess)
# ------------------------------------------------------------------
@tool
def execute_python(code: str) -> str:
    """
    Execute Python code and return stdout/stderr.
    Sandboxed using temporary file and limited execution time.
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(code)
        temp_path = f.name

    try:
        result = subprocess.run(
            ["python", temp_path],
            capture_output=True,
            text=True,
            timeout=5,
        )
        output = result.stdout
        if result.stderr:
            output += f"\n[stderr]: {result.stderr}"
        return output if output else "Code executed successfully (no output)."
    except subprocess.TimeoutExpired:
        return "Execution timed out (5 seconds)."
    except Exception as e:
        return f"Error: {e}"
    finally:
        import os
        os.unlink(temp_path)

# ------------------------------------------------------------------
# 2. Create code interpreter agent
# ------------------------------------------------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
agent = create_agent(llm, tools=[execute_python],
                     system_prompt="You are a Python interpreter. Execute the user's code and return the result.")

if __name__ == "__main__":
    queries = [
        "Calculate the sum of numbers from 1 to 100",
        "Print 'Hello, world!'",
        "Write a loop that prints numbers 1 to 5",
    ]
    for q in queries:
        print(f"\nUser: {q}")
        result = agent.invoke({"messages": [("user", q)]})
        print(f"Agent: {result['messages'][-1].content}")