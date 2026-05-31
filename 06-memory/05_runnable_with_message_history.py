#!/usr/bin/env python
"""
Module 06-05: RunnableWithMessageHistory – Modern Session Memory for LCEL

This is the recommended way to add conversation memory to LCEL chains in LangChain 1.0+.
It works with any message history backend (in‑memory, Redis, Postgres, etc.).
"""

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Simple in‑memory store for sessions
store = {}

def get_session_history(session_id: str):
    """Return a message history object for the given session ID."""
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def basic_runnable_with_history():
    print("=" * 60)
    print("1. RunnableWithMessageHistory – Per‑Session Memory")
    print("=" * 60)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("placeholder", "{history}"),  # history will be injected here
        ("human", "{input}")
    ])

    chain = prompt | model | StrOutputParser()

    # Wrap with history
    chain_with_history = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )

    # Session A
    config_a = {"configurable": {"session_id": "user_alice"}}
    response1 = chain_with_history.invoke({"input": "My name is Alice."}, config=config_a)
    print(f"Session A (Alice): {response1}")

    response2 = chain_with_history.invoke({"input": "What's my name?"}, config=config_a)
    print(f"Session A (Alice): {response2}")

    # Session B – different user, separate history
    config_b = {"configurable": {"session_id": "user_bob"}}
    response3 = chain_with_history.invoke({"input": "My name is Bob."}, config=config_b)
    print(f"Session B (Bob): {response3}")

    response4 = chain_with_history.invoke({"input": "What's my name?"}, config=config_b)
    print(f"Session B (Bob): {response4}\n")

def persistence_example():
    print("=" * 60)
    print("2. Multiple Turns in Same Session")
    print("=" * 60)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You remember previous questions."),
        ("placeholder", "{history}"),
        ("human", "{input}")
    ])

    chain = prompt | model | StrOutputParser()
    chain_with_history = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )

    session_id = "test_user"
    config = {"configurable": {"session_id": session_id}}

    questions = [
        "I love hiking.",
        "What do I enjoy doing?",
        "I also like swimming.",
        "What are my hobbies?"
    ]

    for q in questions:
        response = chain_with_history.invoke({"input": q}, config=config)
        print(f"Q: {q}\nA: {response}\n")

if __name__ == "__main__":
    print("\n Module 06-05: RunnableWithMessageHistory\n")
    basic_runnable_with_history()
    persistence_example()