# Module 09 – Agents

> **Goal:** Build intelligent agents that can autonomously decide which tools to use, in what order, to accomplish user goals.

## What you'll learn

- The **ReAct** (Reasoning + Acting) pattern – foundation of modern agents
- `create_agent` – LangChain 1.0's high‑level agent constructor (runs on LangGraph)
- Custom tools – giving agents the ability to act
- Specialized agents: weather, code interpreter, SQL, pandas

## Why this matters in production

Agents move beyond fixed‑path chains. They can adapt, search for missing information, and solve multi‑step problems. This is essential for real‑world assistants, research tools, and automation.

## Files in this module

| File | What it teaches |
|------|------------------|
| `01_react_pattern.md` | Explanation of Thought → Action → Observation loop |
| `02_create_agent.py` | Basic agent using `create_agent` |
| `03_custom_tools_agent.py` | Agent with multiple custom tools |
| `04_weather_agent.py` | Agent specialised for weather queries |
| `05_code_interpreter_agent.py` | Agent that executes Python code |
| `06_sql_agent.py` | Agent that queries databases via SQL |
| `07_pandas_agent.py` | Agent that analyses pandas DataFrames |

## Run it

```bash
python 09-agents/02_create_agent.py
python 09-agents/03_custom_tools_agent.py
...