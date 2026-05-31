# Module 00 – Setup

> **Goal:** Get your environment ready, install dependencies, and run your first LLM call in under 5 minutes.

This is the only module that doesn’t teach a LangChain concept – it makes sure everything works so you can focus on learning.

## What you will do

- Set up Python virtual environment
- Install required packages
- Configure API keys (or use a free local alternative)
- Run `01_hello_llm.py` to verify everything works

## Prerequisites

- Python 3.10 or higher
- Internet connection (for downloading packages and API calls – offline alternative provided)
- A code editor (VS Code, PyCharm, etc.)

## Files in this module

| File | Purpose |
|------|---------|
| `01_hello_llm.py` | Sanity check – invokes an LLM and prints a response |
| `02_pick_a_provider.md` | Guide to choosing between OpenAI, Groq, Anthropic, and local Ollama |
| `03_local_with_ollama.py` | Run a fully local, free LLM using Ollama (no API key required) |

## Quick start

From the repo root:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt -r requirements-providers.txt
cp .env.example .env
# Edit .env and add at least one API key
python 00-setup/01_hello_llm.py