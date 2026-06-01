
"""
FastAPI server for a LangChain chat agent.

Endpoints:
- POST /chat: non‑streaming response
- POST /chat/stream: streaming SSE response
- GET /health: health check
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import asyncio
import json

app = FastAPI(title="LangChain Production API")

# Simple chain (no memory for demo)
prompt = ChatPromptTemplate.from_template("Answer concisely: {question}")
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
chain = prompt | model | StrOutputParser()

class ChatRequest(BaseModel):
    question: str
    session_id: str = "default"

class ChatResponse(BaseModel):
    answer: str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Non‑streaming endpoint."""
    answer = chain.invoke({"question": request.question})
    return ChatResponse(answer=answer)

@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    """Streaming endpoint (SSE)."""
    async def generate():
        async for chunk in chain.astream({"question": request.question}):
            yield f"data: {json.dumps({'token': chunk})}\n\n"
        yield "data: [DONE]\n\n"
    return StreamingResponse(generate(), media_type="text/event-stream")

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)