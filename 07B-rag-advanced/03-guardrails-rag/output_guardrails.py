"""
Output Guardrails – Filter LLM outputs for toxicity, hallucinations, PII.
"""

import re
from langchain_openai import ChatOpenAI

def contains_profanity(text: str) -> bool:
    """Simple profanity detection (list-based)."""
    profane_words = ["badword1", "badword2"]  # Replace with real list
    return any(word in text.lower() for word in profane_words)

def detect_hallucination(question: str, answer: str, context: str) -> bool:
    """Check if answer contradicts context."""
    prompt = f"Does the answer contain any statement not supported by the context? Answer yes/no.\nContext: {context}\nAnswer: {answer}"
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    response = llm.invoke(prompt).content.strip().lower()
    return "yes" in response

def output_guardrail(question: str, answer: str, context: str) -> bool:
    """Returns True if output is safe, False if should be blocked."""
    if contains_profanity(answer):
        print("Blocked: profanity")
        return False
    if detect_hallucination(question, answer, context):
        print("Blocked: hallucination")
        return False
    return True