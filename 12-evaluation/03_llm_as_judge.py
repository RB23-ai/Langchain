#!/usr/bin/env python
"""
LLM as Judge – Use a powerful LLM (GPT-4, Claude) to score answers.

Metrics: correctness, helpfulness, safety, conciseness.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json

judge_llm = ChatOpenAI(model="gpt-4o", temperature=0)  # Use a strong model

# Scoring rubric
scoring_prompt = PromptTemplate.from_template("""
You are an expert evaluator. Score the following answer on a scale of 1-5 for CORRECTNESS.

Question: {question}
Reference answer: {reference}
Candidate answer: {candidate}

Output ONLY a JSON object: {{"score": <1-5>, "reason": "<brief explanation>"}}
""")

judge_chain = scoring_prompt | judge_llm | StrOutputParser()

def evaluate_answer(question: str, reference: str, candidate: str) -> dict:
    result = judge_chain.invoke({
        "question": question,
        "reference": reference,
        "candidate": candidate,
    })
    return json.loads(result)

if __name__ == "__main__":
    question = "What is the capital of France?"
    reference = "Paris"
    candidate = "The capital city of France is Paris."

    score = evaluate_answer(question, reference, candidate)
    print(f"Score: {score['score']} – {score['reason']}")