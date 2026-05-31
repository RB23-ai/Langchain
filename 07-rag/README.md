# Module 07 – RAG (Retrieval-Augmented Generation)

> **Goal:** Master RAG from basic document ingestion to advanced patterns like CRAG, Self‑RAG, and Agentic RAG.

## What you'll learn

- Document Loaders (PDF, web, YouTube, Notion, GitHub)
- Text Splitters (Recursive, Token, Semantic, Code, Markdown)
- Embeddings (OpenAI, HuggingFace, Cohere reranking)
- Vector Stores (Chroma, FAISS, Pinecone, Weaviate)
- Retrievers (Similarity, MMR, MultiQuery, Self‑Query, Parent, Ensemble, Contextual Compression)
- RAG Patterns (Naive, Query Rewriting, HyDE, CRAG, Self‑RAG, Adaptive, Agentic)
- Evaluation (RAGAS metrics, LangSmith)

## Subdirectories

| Directory | Topic |
|:---|:---|
| `01-document-loaders/` | Load from PDF, web, YouTube, Notion, GitHub |
| `02-text-splitters/` | Chunking strategies |
| `03-embeddings/` | Embedding models (OpenAI, HF local) |
| `04-vector-stores/` | Chroma, FAISS, Pinecone, Weaviate (Jupyter notebooks) |
| `05-retrievers/` | Retrieval strategies |
| `06-rag-patterns/` | Naive → Query Rewriting → HyDE → CRAG → Self‑RAG → Agentic |
| `07-evaluation/` | RAGAS metrics, LangSmith traces |

## Interview Questions

1. **What is the RAG pipeline?** Load → Split → Embed → Store (offline). Retrieve → Generate (online).
2. **Why is chunk overlap important?** Prevents information loss at chunk boundaries.
3. **What's the difference between `load()` and `lazy_load()`?** `load()` returns all docs (memory heavy); `lazy_load()` returns a generator (memory efficient).
4. **When would you use `SemanticChunker`?** For prose where you want topically coherent chunks.
5. **Why use the same embedding model for indexing and querying?** Different models produce incompatible vector spaces.
6. **What is MMR?** Balances relevance and diversity – prevents redundant results.
7. **What is hybrid retrieval?** Combines BM25 (keyword) and dense (semantic) retrieval.
8. **What is HyDE?** Generate a hypothetical answer, then retrieve documents similar to that answer.
9. **What is CRAG?** Evaluates retrieved docs; if low confidence, fall back to web search.
10. **What are the four RAGAS metrics?** Faithfulness, answer relevancy, context precision, context recall.

## Run it

```bash
# Example
python 07-rag/01-document-loaders/pdf_loader.py