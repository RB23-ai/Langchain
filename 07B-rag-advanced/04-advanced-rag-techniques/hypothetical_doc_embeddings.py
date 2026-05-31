"""
HyDE – Hypothetical Document Embeddings

Idea: generate a hypothetical answer to the user's query first, then use its embedding
to retrieve real documents. This bridges the semantic gap between query phrasing and
document language.

Steps:
1. LLM generates a hypothetical (possibly fictional) answer.
2. Embed that hypothetical answer.
3. Retrieve real documents similar to the hypothetical answer.
4. Optionally, generate the final answer using those retrieved documents.
"""

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from typing import List

def generate_hypothetical_answer(query: str, llm) -> str:
    """Generate a hypothetical answer that could plausibly answer the query."""
    prompt = f"Write a detailed, factual‑sounding hypothetical answer to the following question:\n{query}"
    return llm.invoke(prompt).content

def hyde_retrieve(query: str, vectorstore, llm, k: int = 5) -> List[Document]:
    """Retrieve documents using HyDE."""
    hypothetical = generate_hypothetical_answer(query, llm)
    print(f"[HyDE] Hypothetical answer:\n{hypothetical[:200]}...\n")
    docs = vectorstore.similarity_search(hypothetical, k=k)
    return docs

def hyde_rag(query: str, vectorstore, llm, k: int = 5) -> str:
    """Full HyDE pipeline: retrieve then generate final answer."""
    retrieved = hyde_retrieve(query, vectorstore, llm, k)
    context = "\n\n".join([doc.page_content for doc in retrieved])
    final_prompt = f"Answer the question based on the context below.\nContext:\n{context}\nQuestion: {query}\nAnswer:"
    return llm.invoke(final_prompt).content

if __name__ == "__main__":
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    embeddings = OpenAIEmbeddings()
    corpus = [
        "RAG stands for Retrieval-Augmented Generation. It improves LLM accuracy by grounding responses in external knowledge.",
        "Hypothetical Document Embeddings (HyDE) generate a fake document before searching.",
        "Reciprocal Rank Fusion combines multiple retrieval result sets.",
        "Self-RAG uses reflection tokens to decide when to retrieve."
    ]
    vectorstore = FAISS.from_texts(corpus, embeddings)

    question = "What is HyDE and how does it work?"
    answer = hyde_rag(question, vectorstore, llm)
    print(f"\nFinal answer:\n{answer}")