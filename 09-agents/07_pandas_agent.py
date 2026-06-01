#!/usr/bin/env python
"""
Module 09-07: Pandas Agent

An agent that can analyse pandas DataFrames using natural language.
It uses the `create_pandas_dataframe_agent` from LangChain (legacy) or a custom tool.
We'll implement a custom tool that runs pandas operations via `eval`.
WARNING: Executing arbitrary code is risky – this is for demonstration.
"""

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
import pandas as pd

# ------------------------------------------------------------------
# 1. Create a sample DataFrame
# ------------------------------------------------------------------
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 60000, 70000, 55000],
    "department": ["Engineering", "Sales", "Engineering", "Marketing"]
})

# ------------------------------------------------------------------
# 2. Tool that runs pandas code (sandboxed eval – dangerous, use with caution)
# ------------------------------------------------------------------
@tool
def query_dataframe(code: str) -> str:
    """
    Execute a Python expression that operates on the DataFrame 'df'.
    Returns the string representation of the result.
    Example: "df[df['age'] > 28]['name'].tolist()"
    """
    try:
        # Evaluate in a restricted namespace (still risky)
        result = eval(code, {"df": df, "pd": pd})
        return str(result)
    except Exception as e:
        return f"Error: {e}"

# ------------------------------------------------------------------
# 3. Create pandas agent
# ------------------------------------------------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
agent = create_agent(llm, tools=[query_dataframe],
                     system_prompt="You help analyse a DataFrame 'df' with columns: name, age, salary, department. Write pandas code to answer questions.")

if __name__ == "__main__":
    queries = [
        "What is the average salary?",
        "Who are the employees older than 30?",
        "List names of engineers.",
    ]
    for q in queries:
        print(f"\nUser: {q}")
        result = agent.invoke({"messages": [("user", q)]})
        print(f"Agent: {result['messages'][-1].content}")