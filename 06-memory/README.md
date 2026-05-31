# Module 06 – Memory

> **Goal:** Give your LLM application persistent memory – from simple conversation buffers to cross‑session long‑term memory.

## What you'll learn

- `ConversationBufferMemory` – store entire conversation history
- `ConversationBufferWindowMemory` – keep only the last K turns (production favorite)
- `ConversationSummaryMemory` – compress history using an LLM
- `VectorStoreRetrieverMemory` – retrieve relevant past messages via semantic similarity
- `RunnableWithMessageHistory` – modern, session‑aware memory for LCEL chains
- LangGraph's `Checkpointer` + `Store` – the 1.0+ architecture for durable, cross‑thread memory

## Why this matters in production

LLMs are stateless. Without memory, every interaction is a fresh start. Memory enables:
- Multi‑turn conversations (the bot remembers what you just said)
- Personalization (remembers user preferences across sessions)
- Reduced token costs (summarized history instead of raw logs)
- Long‑running agents (state persists across API calls)

## Memory Types at a Glance

| Memory Type | What It Stores | Token Cost | Best For |
|:---|:---|:---|:---|
| `BufferMemory` | Full raw history | High (grows unbounded) | Short debugging sessions |
| `BufferWindowMemory` | Last K messages | Fixed (predictable) | **Production chatbots** ⭐ |
| `SummaryMemory` | LLM‑generated summary | Low (constant) | Long creative conversations |
| `VectorMemory` | Embeddings of past messages | Retrieval cost | Long‑term associative memory |
| `RunnableWithMessageHistory` | Session‑scoped history (any backend) | Varies | Modern LCEL chains |

## Files in this module

| File | What it teaches |
|------|------------------|
| `01_conversation_buffer.py` | Full history storage – simple but unbounded |
| `02_buffer_window.py` | Sliding window – production default |
| `03_summary_memory.py` | LLM summarization for long conversations |
| `04_vector_memory.py` | Semantic search over past messages |
| `05_runnable_with_message_history.py` | Session‑aware memory for LCEL |
| `06_langgraph_memory.md` | LangGraph Checkpointer + Store (the 1.0+ standard) |

## Run it

```bash
python 06-memory/01_conversation_buffer.py
python 06-memory/02_buffer_window.py
python 06-memory/03_summary_memory.py
python 06-memory/04_vector_memory.py
python 06-memory/05_runnable_with_message_history.py