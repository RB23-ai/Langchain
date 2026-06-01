"""
Cost Controls – Track token usage, set budgets, and alert on anomalies.

This example demonstrates:
- Using LangSmith cost tracking (automatic)
- Custom callback for per‑user token accounting
- Budget thresholds with alerts
"""

from langchain.callbacks import get_openai_callback
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os

# ------------------------------
# 1. Using LangSmith (automatic)
# ------------------------------
# Set environment variables:
# LANGSMITH_TRACING_V2=true
# LANGSMITH_API_KEY=...
# Then every run appears in LangSmith with token usage and derived cost

# ------------------------------
# 2. Custom token tracking callback
# ------------------------------
class TokenBudgetCallback:
    def __init__(self, user_id: str, budget_usd: float = 1.0):
        self.user_id = user_id
        self.budget_usd = budget_usd
        self.total_tokens = 0
        self.total_cost = 0.0

    def on_llm_end(self, response, **kwargs):
        usage = response.llm_output.get("token_usage", {})
        prompt_tokens = usage.get("prompt_tokens", 0)
        completion_tokens = usage.get("completion_tokens", 0)
        # Approximate cost (adjust per model)
        cost = (prompt_tokens * 0.000001) + (completion_tokens * 0.000002)
        self.total_tokens += prompt_tokens + completion_tokens
        self.total_cost += cost
        if self.total_cost > self.budget_usd:
            print(f"⚠️ User {self.user_id} exceeded budget of ${self.budget_usd}")

# ------------------------------
# 3. Per‑request cost capture
# ------------------------------
with get_openai_callback() as cb:
    model = ChatOpenAI(model="gpt-4o-mini")
    response = model.invoke("Tell me a story")
    print(f"Tokens: {cb.total_tokens}, Cost: ${cb.total_cost:.6f}")

# ------------------------------
# 4. Cost‑aware routing (cheap model for simple queries)
# ------------------------------
def route_by_cost(question: str):
    if len(question) < 20:  # simple question
        model = ChatOpenAI(model="gpt-3.5-turbo")
    else:
        model = ChatOpenAI(model="gpt-4o-mini")
    return model.invoke(question).content