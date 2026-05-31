# Module 07B – Advanced RAG Techniques

> **Goal:** Master state‑of‑the‑art RAG patterns: Graph RAG, Multimodal RAG, Guardrails, and advanced retrieval methods.

## What you'll learn

- **Graph RAG** – Build knowledge graphs from documents, hybrid text‑graph retrieval
- **Multimodal RAG** – Process images, tables, audio, video alongside text
- **Guardrails** – Input/output filtering, citation grounding, safety moderation
- **Advanced Techniques** – RAG Fusion, HyDE, Self‑RAG with reflection, Agentic RAG tools, long context caching

## Structure

| Subdirectory | Content |
|:---|:---|
| `01-graph-rag/` | Graph construction (entities/relations), stores, retrievers, Microsoft Graph RAG, hybrid text‑graph |
| `02-multimodal-rag/` | Image loaders, CLIP embeddings, table processing, audio/video, unified retriever |
| `03-guardrails-rag/` | Input guardrails (PII, prompt injection), output guardrails, citation grounding, moderation, safety eval |
| `04-advanced-rag-techniques/` | RAG Fusion, HyDE, Self‑RAG with reflection, Agentic RAG tools, long context caching |

## Run it

```bash
python 01-graph-rag/graph_construction.py
python 02-multimodal-rag/image_loaders.py
...