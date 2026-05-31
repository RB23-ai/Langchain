# Module 08 – Tool Calling

> **Goal:** Master LangChain’s tool calling system – from simple `@tool` decorators to parallel execution, structured schemas, and human‑in‑the‑loop approval.

## What you'll learn

- `@tool` decorator – the simplest way to turn a function into a tool
- `bind_tools()` – attaching tools to an LLM for agentic decision making
- Parallel tool calls – invoking multiple tools in a single LLM response
- Structured tools – using Pydantic schemas for complex inputs
- Human approval tools – requiring manual confirmation before executing sensitive operations

## Why this matters in production

Tool calling gives LLMs the ability to act – to search the web, run calculations, query databases, or send emails. Without tools, an LLM is a pure text generator. With tools, it becomes an **agent** capable of completing real‑world tasks.

## Files in this module

| File | What it teaches |
|------|------------------|
| `01_tool_decorator.py` | `@tool` – docstring becomes description, type hints become schema |
| `02_bind_tools.py` | `bind_tools()` – attach tools to an LLM, inspect tool calls |
| `03_parallel_tool_calls.py` | Execute multiple tools in parallel from one LLM response |
| `04_structured_tool.py` | Define input schemas with Pydantic for complex validation |
| `05_human_approval_tool.py` | Wrap sensitive tools with human‑in‑the‑loop approval |

## Run it

```bash
python 08-tool-calling/01_tool_decorator.py
python 08-tool-calling/02_bind_tools.py
...