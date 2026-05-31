#!/usr/bin/env python
"""
Module 06-02: ConversationBufferWindowMemory – Sliding Window

Keeps only the last K conversation turns. Token usage is predictable and bounded.
This is the **production default** for most chatbots.
"""

from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

def window_memory_demo():
    print("=" * 60)
    print("1. BufferWindowMemory – Keep Last 3 Turns")
    print("=" * 60)

    # k=3 means keep last 3 exchanges (6 messages: 3 human + 3 AI)
    memory = ConversationBufferWindowMemory(k=3, return_messages=True)
    chain = ConversationChain(llm=model, memory=memory, verbose=False)

    turns = [
        "My name is Alice.",
        "I live in Paris.",
        "I work as a data scientist.",
        "What's my name?",
        "Where do I live?",
        "What do I do for work?",
        "What was my first message?"  # This will be forgotten because window=3
    ]

    for i, user_input in enumerate(turns, 1):
        response = chain.predict(input=user_input)
        print(f"Turn {i}: User: {user_input}")
        print(f"      AI: {response[:100]}...")
        print()

    print("📊 After 7 turns, only the last 3 exchanges remain in memory.")
    print("   The first message ('My name is Alice') is gone.\n")

def memory_visualization():
    print("=" * 60)
    print("2. Visualizing the Sliding Window")
    print("=" * 60)

    memory = ConversationBufferWindowMemory(k=2)
    memory.save_context({"input": "A"}, {"output": "1"})
    memory.save_context({"input": "B"}, {"output": "2"})
    memory.save_context({"input": "C"}, {"output": "3"})

    history = memory.load_memory_variables({})["history"]
    print("After adding A1, B2, C3 (k=2):")
    print(history)
    print("\n→ 'A1' has been evicted. Only B2 and C3 remain.")

if __name__ == "__main__":
    print("\n Module 06-02: ConversationBufferWindowMemory\n")
    window_memory_demo()
    memory_visualization()