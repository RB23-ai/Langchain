#!/usr/bin/env python
"""
Server‑Sent Events (SSE) streaming with FastAPI and async LangChain.
"""

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import asyncio
import json

app = FastAPI()

prompt = ChatPromptTemplate.from_template("Write a short poem about {topic}")
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.9)
chain = prompt | model | StrOutputParser()

class PoemRequest(BaseModel):
    topic: str

@app.post("/poem/stream")
async def stream_poem(request: PoemRequest):
    async def generate():
        async for chunk in chain.astream({"topic": request.topic}):
            yield f"data: {json.dumps({'text': chunk})}\n\n"
        yield "data: [DONE]\n\n"
    return StreamingResponse(generate(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)