# LangServe vs. Custom FastAPI: When to Use What

LangServe was designed to quickly turn any LangChain runnable into a REST API. It automatically generates endpoints (`/invoke`, `/batch`, `/stream`) and OpenAPI docs.

## When LangServe works well

- Prototyping or internal tools
- You only need basic invoke/batch/stream
- You don't need custom authentication, rate limiting, or middleware

## When you should build a custom FastAPI app

- You need fine‑grained control over endpoints (e.g., `/chat`, `/feedback`)
- You need to inject middleware (rate limiting, CORS, logging)
- You need session management or user authentication
- You want to combine multiple chains/agents in one API
- You want to optimize memory usage (LangServe loads everything eagerly)

## Alternative: FastAPI + manual runnable invocation

The `01_serving_with_fastapi/` folder shows exactly this pattern. You keep full control and add exactly what you need.

## Recommendation

For production, start with a custom FastAPI app. It's more lines of code but far more flexible. LangServe is best for demos or when you need zero‑code API exposure.