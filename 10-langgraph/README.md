# Module 10 – LangGraph

> **Goal:** Build stateful, cyclical, human‑in‑the‑loop AI agents using LangGraph – the engine that powers LangChain 1.0 agents.

## Why LangGraph?

LCEL (pipe) is great for linear chains. But when you need:
- Loops (retry on failure, iterate until condition)
- Human approval (pause, wait for input, resume)
- Persistent memory across invocations (checkpoints)
- Multi‑agent collaboration (supervisor + workers)

…you need LangGraph. It models workflows as state machines.

## Files in this module

| File | What it teaches |
|------|------------------|
| `01_first_stategraph.py` | Minimal StateGraph with one node |
| `02_state_and_reducers.py` | Typed state, reducers (add_messages) |
| `03_conditional_edges.py` | Branching with `add_conditional_edges` |
| `04_cycles_and_loops.py` | Looping back to previous nodes |
| `05_checkpointer_memory.py` | Within‑thread persistence (MemorySaver) |
| `06_store_cross_thread.py` | Long‑term memory across threads (Store) |
| `07_human_in_the_loop.py` | Interrupt before/after, resume execution |
| `08_streaming_events.py` | Streaming graph execution events |
| `09_subgraphs.py` | Nesting compiled graphs as nodes |
| `10_multi_agent_supervisor.py` | Supervisor pattern for multi‑agent systems |
| `11_multi_agent_swarm.py` | Peer‑to‑peer agent handoffs |
| `12_durable_execution.py` | Postgres checkpointer for production |

## Run it

```bash
python 10-langgraph/01_first_stategraph.py
...