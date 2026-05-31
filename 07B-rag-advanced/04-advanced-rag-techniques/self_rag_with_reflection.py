"""
Self‑RAG with Reflection – Iterative retrieval and self‑critique

Implements a simple version of Self‑RAG where the LLM:
1. Decides whether retrieval is needed for the query.
2. Retrieves documents.
3. Generates an answer.
4. Critiques its own answer (faithfulness, usefulness).
5. If the critique fails, it either retrieves again (with a refined query) or retries generation.

Uses LangGraph for stateful, conditional loops.
"""

from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

class GraphState(TypedDict):
    question: str
    generation: str
    documents: List[Document]
    critique: str
    iteration: int
    needs_retrieval: bool

def decide_retrieval(state: GraphState):
    """LLM decides if retrieval is needed."""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    prompt = f"Does the following question require external knowledge (yes/no)?\nQuestion: {state['question']}"
    response = llm.invoke(prompt).content.strip().lower()
    needs = "yes" in response
    return {"needs_retrieval": needs, "iteration": state.get("iteration", 0) + 1}

def retrieve(state: GraphState):
    """Retrieve relevant documents from vector store."""
    docs = vectorstore.similarity_search(state["question"], k=4)
    return {"documents": docs}

def generate(state: GraphState):
    """Generate answer using retrieved documents (or directly if no retrieval)."""
    llm = ChatOpenAI(model="gpt-4o-mini")
    if state.get("documents"):
        context = "\n\n".join([d.page_content for d in state["documents"]])
        prompt = f"Answer the question using only the context.\nContext: {context}\nQuestion: {state['question']}\nAnswer:"
    else:
        prompt = f"Answer the question: {state['question']}"
    answer = llm.invoke(prompt).content
    return {"generation": answer}

def critique(state: GraphState):
    """LLM critiques the generated answer for faithfulness and usefulness."""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    context = "\n\n".join([d.page_content for d in state.get("documents", [])])
    prompt = f"""Evaluate the answer.
Context: {context}
Question: {state['question']}
Answer: {state['generation']}
Output JSON: {{"faithful": true/false, "useful": true/false}}"""
    critique_text = llm.invoke(prompt).content
    return {"critique": critique_text}

def route_after_critique(state: GraphState):
    """Decide whether to retry retrieval or generation, or finish."""
    if "false" in state["critique"].lower() and state["iteration"] < 3:
        # Retry retrieval with refined query
        return "retrieve"
    else:
        return END

builder = StateGraph(GraphState)
builder.add_node("decide_retrieval", decide_retrieval)
builder.add_node("retrieve", retrieve)
builder.add_node("generate", generate)
builder.add_node("critique", critique)

builder.set_entry_point("decide_retrieval")
builder.add_conditional_edges(
    "decide_retrieval",
    lambda s: "retrieve" if s["needs_retrieval"] else "generate"
)
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", "critique")
builder.add_conditional_edges("critique", route_after_critique)

graph = builder.compile()

if __name__ == "__main__":
    from langchain_openai import OpenAIEmbeddings
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(
        ["Self-RAG uses self‑reflection tokens.", "It improves factuality and reduces hallucinations."],
        embeddings
    )

    result = graph.invoke({"question": "What is Self‑RAG?", "iteration": 0})
    print("Final answer:", result["generation"])