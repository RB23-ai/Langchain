#!/usr/bin/env python
"""
Custom Callbacks – Build your own logging, metrics, or alerting.

This example implements a simple callback that prints events and counts tokens.
"""

from langchain_core.callbacks import BaseCallbackHandler
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from typing import Dict, Any, List

class MyCustomHandler(BaseCallbackHandler):
    """Prints events and accumulates token usage."""

    def __init__(self):
        self.total_tokens = 0
        self.step_count = 0

    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs) -> None:
        self.step_count += 1
        print(f"[Step {self.step_count}] LLM call started")

    def on_llm_end(self, response, **kwargs) -> None:
        # Extract token usage if available
        try:
            usage = response.llm_output.get("token_usage", {})
            tokens = usage.get("total_tokens", 0)
            self.total_tokens += tokens
            print(f"[Step {self.step_count}] LLM ended – tokens this call: {tokens}, total: {self.total_tokens}")
        except:
            pass

    def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs) -> None:
        print(f"Chain started with inputs: {inputs}")

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs) -> None:
        print(f"Chain ended with output: {outputs[:100]}...")

# Usage
handler = MyCustomHandler()
model = ChatOpenAI(model="gpt-4o-mini", callbacks=[handler])
prompt = ChatPromptTemplate.from_template("What is {topic}?")
chain = prompt | model

result = chain.invoke({"topic": "LangChain callbacks"})
print("\nFinal answer:", result.content)
print(f"\n📊 Total tokens across all calls: {handler.total_tokens}")