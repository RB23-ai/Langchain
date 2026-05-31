"""
Citation Grounding – Force LLM to provide citations for each claim.
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List
from langchain_openai import ChatOpenAI

class Citation(BaseModel):
    text: str = Field(description="The quoted or paraphrased claim")
    source: str = Field(description="Document identifier or chunk ID")

class AnswerWithCitations(BaseModel):
    answer: str = Field(description="Final answer summarizing the citations")
    citations: List[Citation] = Field(description="List of citations supporting the answer")

parser = PydanticOutputParser(pydantic_object=AnswerWithCitations)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Always cite your sources. {format_instructions}"),
    ("human", "Context: {context}\nQuestion: {question}")
])

def get_grounded_answer(question: str, context: str):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    chain = prompt.partial(format_instructions=parser.get_format_instructions()) | llm | parser
    return chain.invoke({"question": question, "context": context})

if __name__ == "__main__":
    result = get_grounded_answer("What is RAG?", "RAG stands for Retrieval-Augmented Generation.")
    print(result.answer)
    for c in result.citations:
        print(f"  - {c.text} (source: {c.source})")