#!/usr/bin/env python
"""
Pairwise Evaluators – Compare two model outputs to decide which is better.

Common use: A/B testing prompts, models, or retrieval strategies.
"""

from langsmith.evaluation import evaluate
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Two different prompts
prompt_a = ChatPromptTemplate.from_template("Answer concisely: {q}")
prompt_b = ChatPromptTemplate.from_template("Answer in detail, with examples: {q}")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def run_model_a(inputs):
    return (prompt_a | llm).invoke(inputs["question"]).content

def run_model_b(inputs):
    return (prompt_b | llm).invoke(inputs["question"]).content

# Dataset of questions
questions = ["What is RAG?", "Explain quantum computing simply."]

# Use LangSmith's pairwise evaluator (requires `LangSmithClient`)
from langsmith import Client
client = Client()
dataset = client.create_dataset("pairwise_test", data=[{"question": q} for q in questions])

# Evaluate
eval_results = evaluate(
    run_model_a,
    data=dataset.id,
    evaluators=[lambda a, b: {"score": 1, "comment": "Placeholder"}],
)
print(eval_results)