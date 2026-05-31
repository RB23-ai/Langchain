"""
Module 06-01: ConversationBufferMemory – Full History

Stores every message exchanged. Simple but token usage grows with each turn.
Use only for short debugging or when you are certain conversations will be short.
"""

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

def buffer_memory_demo():
    print("=" * 60)
    print("1. ConversationBufferMemory – Full History")
    print("=" * 60)

    memory = ConversationBufferMemory()
    chain = ConversationChain(llm=model, memory=memory, verbose=True)

    print("\nTurn 1:")
    response1 = chain.predict(input="Hi, my name is Alice.")
    print(f"AI: {response1}")

    print("\nTurn 2:")
    response2 = chain.predict(input="What's my name?")
    print(f"AI: {response2}")

    print("\nMemory contents (raw):")
    print(memory.load_memory_variables({}))

    print("\n⚠️  Caution: BufferMemory grows without bound.")
    print("   After 100 turns, token usage may exceed context limits.\n")

def inspect_memory():
    print("=" * 60)
    print("2. Inspecting Memory Buffer")
    print("=" * 60)

    memory = ConversationBufferMemory(return_messages=True)
    memory.save_context({"input": "Hello"}, {"output": "Hi there!"})
    memory.save_context({"input": "How are you?"}, {"output": "I'm good, thanks!"})

    variables = memory.load_memory_variables({})
    print("Messages stored:")
    for msg in variables["history"]:
        print(f"  {msg.type}: {msg.content}")

if __name__ == "__main__":
    print("\n Module 06-01: ConversationBufferMemory\n")
    buffer_memory_demo()
    inspect_memory()