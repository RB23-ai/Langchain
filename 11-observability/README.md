# Module 11 – Observability

> **Goal:** Gain full visibility into your LLM applications – traces, metrics, costs, and custom telemetry.

## Why Observability Matters

LLM applications fail in unpredictable ways: hallucinations, token limit overruns, infinite agent loops, and surprising costs. Without observability, debugging is guesswork. With proper tracing and metrics, you can:

- See exactly which prompt, retrieval, or tool call caused a wrong answer
- Track token usage and cost per user / per session
- Detect regressions before they reach production
- Optimize latency and throughput

## What You'll Learn

| File | What it teaches |
|------|------------------|
| `01_langsmith_tracing.py` | Enable LangSmith to automatically trace every LLM call, tool invocation, and chain step |
| `02_custom_callbacks.py` | Build your own callback handlers for custom logging, metrics, and alerts |
| `03_token_cost_tracking.py` | Track token usage and cost per request using built‑in callbacks |
| `04_opentelemetry.py` | The 1.0+ standard: export traces to OpenTelemetry backends (Jaeger, Datadog, etc.) |

## Setup

```bash
pip install langsmith opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp