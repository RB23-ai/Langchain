#!/usr/bin/env python
"""
OpenTelemetry Integration – Export traces to OTLP backends (Jaeger, Datadog, etc.).

This is the 1.0+ standard for vendor‑agnostic observability.
"""

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# ------------------------------------------------------------------
# 1. Setup OpenTelemetry
# ------------------------------------------------------------------
provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())  # print to console
provider.add_span_processor(processor)

# If you have an OTLP endpoint (e.g., Jaeger, Datadog), uncomment:
# otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
# provider.add_span_processor(BatchSpanProcessor(otlp_exporter))

trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# ------------------------------------------------------------------
# 2. Use LangChain with manual spans
# ------------------------------------------------------------------
@tracer.start_as_current_span("my-rag-chain")
def my_chain(question: str) -> str:
    model = ChatOpenAI(model="gpt-4o-mini")
    prompt = ChatPromptTemplate.from_template("Answer: {q}")
    chain = prompt | model
    return chain.invoke({"q": question}).content

if __name__ == "__main__":
    answer = my_chain("What is OpenTelemetry?")
    print(f"Answer: {answer}")
    print("\n✅ Traces exported to console. Install Jaeger to visualize.")