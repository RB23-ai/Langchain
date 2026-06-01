#!/usr/bin/env python
"""
Module 09-06: SQL Agent

An agent that can query a SQLite database using natural language.
Uses a predefined database (e.g., Chinook sample DB or a simple one).
"""

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
import sqlite3

# ------------------------------------------------------------------
# 1. Create a sample SQLite database
# ------------------------------------------------------------------
def create_sample_db():
    conn = sqlite3.connect("sample.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER, name TEXT, department TEXT, salary INTEGER)")
    cursor.execute("DELETE FROM employees")
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", [
        (1, "Alice", "Engineering", 90000),
        (2, "Bob", "Sales", 75000),
        (3, "Charlie", "Engineering", 85000),
    ])
    conn.commit()
    conn.close()

create_sample_db()

# ------------------------------------------------------------------
# 2. Tool that executes SQL queries
# ------------------------------------------------------------------
@tool
def run_sql(query: str) -> str:
    """Execute a SQL SELECT query on the employees database and return results."""
    try:
        conn = sqlite3.connect("sample.db")
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        if not rows:
            return "No results."
        return "\n".join(str(row) for row in rows)
    except Exception as e:
        return f"SQL error: {e}"

# ------------------------------------------------------------------
# 3. Create SQL agent
# ------------------------------------------------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
agent = create_agent(llm, tools=[run_sql],
                     system_prompt="You are a SQL expert. Convert natural language to SQL and run queries.")

if __name__ == "__main__":
    queries = [
        "Show all employees.",
        "List employees in Engineering.",
        "What is the average salary?",
    ]
    for q in queries:
        print(f"\nUser: {q}")
        result = agent.invoke({"messages": [("user", q)]})
        print(f"Agent: {result['messages'][-1].content}")