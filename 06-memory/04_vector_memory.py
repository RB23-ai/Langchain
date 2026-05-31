#!/usr/bin/env python
"""
Module 06-04: VectorStoreRetrieverMemory – Semantic Search Over History

Stores past messages as embeddings. At query time, retrieves the most semantically
similar past exchanges. Perfect for long‑term memory across many turns.
"""

from langchain.memory import VectorStoreRetrieverMemory
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

def vector_memory_demo():
    print("=" * 60)
    print("1. VectorStoreRetrieverMemory – Semantic Memory")
    print("=" * 60)

    # Create vector store
    embedding = OpenAIEmbeddings()
    vectorstore = Chroma(collection_name="memory", embedding_function=embedding)

    # Wrap as retriever memory
    memory = VectorStoreRetrieverMemory(
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_messages=True
    )

    # Save some facts
    memory.save_context({"input": "My favorite color is blue"}, {"output": "Noted."})
    memory.save_context({"input": "I have a dog named Max"}, {"output": "Cute!"})
    memory.save_context({"input": "I work as a software engineer"}, {"output": "Interesting."})

    # Query memory
    query = "What pet do I have?"
    relevant = memory.load_memory_variables({"input": query})["history"]
    print(f"Query: '{query}'")
    print(f"Retrieved memories: {relevant}\n")

    # Second query
    query2 = "What is my job?"
    relevant2 = memory.load_memory_variables({"input": query2})["history"]
    print(f"Query: '{query2}'")
    print(f"Retrieved memories: {relevant2}\n")

def memory_in_chain():
    print("=" * 60)
    print("2. Using Vector Memory in a ConversationChain")
    print("=" * 60)

    embedding = OpenAIEmbeddings()
    vectorstore = Chroma(collection_name="chain_memory", embedding_function=embedding)
    memory = VectorStoreRetrieverMemory(
        retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
        return_messages=False  # plain string for older chains
    )

    # Save a fact
    memory.save_context({"input": "My birthday is July 4th"}, {"output": "Happy birthday in advance!"})

    chain = ConversationChain(llm=model, memory=memory, verbose=False)
    response = chain.predict(input="When is my birthday?")
    print(f"AI response: {response}\n")

if __name__ == "__main__":
    print("\nModule 06-04: VectorStoreRetrieverMemory\n")
    vector_memory_demo()
    memory_in_chain()