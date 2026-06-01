# Module 13 – Production

> **Goal:** Deploy, scale, secure, and monitor your LangChain applications in production.

## What you'll learn

- Serving chains/agents with FastAPI (custom, no LangServe)
- Rate limiting and caching (Redis, in‑memory)
- Retries and fallbacks for resilience
- Server‑Sent Events (SSE) streaming for chat UI
- Security: prompt injection, PII, secrets management
- Cost controls (token budgets, model fallbacks)
- Docker deployment with docker‑compose

## Files in this module

| File | What it teaches |
|------|------------------|
| `01_serving_with_fastapi/` | FastAPI app with `/chat` endpoint |
| `02_langserve_alternative.md` | Why you might not need LangServe |
| `03_rate_limiting_caching.py` | Token bucket + Redis caching |
| `04_retry_and_fallbacks.py` | Tenacity retries, provider fallback |
| `05_streaming_sse.py` | Async streaming via SSE |
| `06_security_prompt_injection.md` | Defending against prompt injection |
| `07_cost_controls.py` | Token counting and spend limits |
| `08_docker_deployment/` | Dockerfile + docker‑compose.yml |

## Run it

```bash
cd 01_serving_with_fastapi
pip install fastapi uvicorn
python main.py