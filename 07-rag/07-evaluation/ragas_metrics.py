#!/usr/bin/env python
"""
Evaluation: RAGAS Metrics

Measures faithfulness, answer relevance, context precision, context recall.
Requires dataset with questions, answers, contexts.
"""

from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
from datasets import Dataset

data = {
    "question": ["What is RAG?"],
    "answer": ["RAG stands for Retrieval-Augmented Generation."],
    "contexts": [["Retrieval-Augmented Generation (RAG) is a technique."]],
    "ground_truth": ["RAG is Retrieval-Augmented Generation."]
}
dataset = Dataset.from_dict(data)
result = evaluate(dataset, metrics=[faithfulness, answer_relevancy, context_precision, context_recall])
print(result)