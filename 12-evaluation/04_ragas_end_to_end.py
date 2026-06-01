#!/usr/bin/env python
"""
RAGAS – Compute RAG‑specific metrics: faithfulness, answer relevancy, context precision, context recall.
Requires a dataset with `question`, `answer`, `contexts`, `ground_truth`.
"""

from datasets import Dataset
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
from ragas import evaluate

# Example dataset (replace with your RAG outputs)
data = {
    "question": ["What is RAG?", "What is LangChain?"],
    "answer": ["RAG is Retrieval-Augmented Generation.", "LangChain is an LLM framework."],
    "contexts": [
        ["RAG stands for Retrieval-Augmented Generation, a technique to ground LLMs."],
        ["LangChain is a framework for developing LLM applications."],
    ],
    "ground_truth": [
        "RAG is Retrieval-Augmented Generation.",
        "LangChain is a framework for building LLM apps.",
    ],
}
dataset = Dataset.from_dict(data)

# Run evaluation
results = evaluate(
    dataset,
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
)
print(results)