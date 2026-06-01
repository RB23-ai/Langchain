
### `12-evaluation/01_langsmith_datasets.py`

```python
#!/usr/bin/env python
"""
LangSmith Datasets – Create, upload, and evaluate against a test set.

This example creates a small dataset and runs a chain against it.
"""

import os
from langsmith import Client
from langsmith.evaluation import evaluate
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Initialize LangSmith client
client = Client()

# 1. Create a dataset (run once)
dataset_name = "My Test Dataset"
try:
    dataset = client.create_dataset(dataset_name, description="Simple Q&A test")
except:
    dataset = client.read_dataset(dataset_name=dataset_name)

# Add examples (questions + reference answers)
examples = [
    ("What is the capital of France?", "Paris"),
    ("What is 2+2?", "4"),
    ("Who wrote Hamlet?", "William Shakespeare"),
]
for q, a in examples:
    client.create_example(
        inputs={"question": q},
        outputs={"answer": a},
        dataset_id=dataset.id,
    )

# 2. Define your chain
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
prompt = ChatPromptTemplate.from_template("Question: {question}\nAnswer:")
chain = prompt | llm

# 3. Define an evaluator (simple exact match)
def exact_match(root_run, example):
    predicted = root_run.outputs["output"].content.strip()
    expected = example.outputs["answer"].strip()
    score = 1 if predicted == expected else 0
    return {"score": score, "key": "exact_match"}

# 4. Run evaluation
results = evaluate(
    chain.invoke,
    data=dataset_name,
    evaluators=[exact_match],
    experiment_prefix="baseline",
)

print(f"Evaluation results: {results}")