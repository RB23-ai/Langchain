#!/usr/bin/env python
"""
Rate limiting and caching using Redis (or in‑memory fallback).

Implements:
- Token bucket rate limiter per user
- Caching of LLM responses for identical queries
"""

import hashlib
import time
from functools import wraps
from typing import Dict, Optional
import redis
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ------------------------------------------------------------
# In‑memory cache (fallback if Redis not available)
# ------------------------------------------------------------
class MemoryCache:
    def __init__(self, ttl_seconds=3600):
        self.cache = {}
        self.ttl = ttl_seconds
        self.timestamps = {}

    def get(self, key):
        if key in self.cache:
            if time.time() - self.timestamps[key] < self.ttl:
                return self.cache[key]
            else:
                del self.cache[key]
                del self.timestamps[key]
        return None

    def set(self, key, value):
        self.cache[key] = value
        self.timestamps[key] = time.time()

# ------------------------------------------------------------
# Token bucket rate limiter
# ------------------------------------------------------------
class TokenBucket:
    def __init__(self, rate: float, capacity: int):
        self.rate = rate          # tokens per second
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill = time.time()

    def consume(self, tokens: int = 1) -> bool:
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
        self.last_refill = now
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

# Global rate limiters per user
rate_limiters: Dict[str, TokenBucket] = {}

def get_rate_limiter(user_id: str) -> TokenBucket:
    if user_id not in rate_limiters:
        rate_limiters[user_id] = TokenBucket(rate=2.0, capacity=5)  # 2 req/sec, burst 5
    return rate_limiters[user_id]

# ------------------------------------------------------------
# Cached LLM chain
# ------------------------------------------------------------
def get_cache_key(prompt_template: str, inputs: dict) -> str:
    content = prompt_template + str(sorted(inputs.items()))
    return hashlib.md5(content.encode()).hexdigest()

cache = MemoryCache(ttl_seconds=300)  # 5 minutes

def cached_chain(user_id: str, question: str) -> str:
    # Rate limiting
    limiter = get_rate_limiter(user_id)
    if not limiter.consume():
        raise Exception("Rate limit exceeded. Please wait.")

    # Cache lookup
    key = get_cache_key("Answer concisely: {question}", {"question": question})
    cached = cache.get(key)
    if cached:
        return f"[CACHED] {cached}"

    # Real LLM call
    prompt = ChatPromptTemplate.from_template("Answer concisely: {question}")
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    chain = prompt | model | StrOutputParser()
    answer = chain.invoke({"question": question})
    cache.set(key, answer)
    return answer

if __name__ == "__main__":
    for i in range(7):
        try:
            res = cached_chain("user123", "What is LangChain?")
            print(res)
        except Exception as e:
            print(e)