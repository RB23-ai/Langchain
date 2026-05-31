#!/usr/bin/env python
"""
Evaluation: LangSmith

Create dataset, run evaluators, and trace RAG pipeline.
"""

import os
from langsmith import Client, traceable
from langsmith.evaluation import evaluate

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your_key"
client = Client()

@traceable
def rag_pipeline(question: str) -> str:
    # Your RAG chain here
    return f"Answer to {question}"

def accuracy_evaluator(run, example):
    return {"score": 1 if run.outputs["output"] == example.outputs["answer"] else 0}

# Run evaluation
results = evaluate(
    rag_pipeline,
    data="my_rag_dataset",
    evaluators=[accuracy_evaluator],
    experiment_prefix="rag-test"
)
print(results)