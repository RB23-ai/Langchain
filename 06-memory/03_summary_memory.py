#!/usr/bin/env python
"""
Module 06-03: ConversationSummaryMemory – LLM‑Generated Summary

Instead of storing raw messages, an LLM periodically compresses the conversation
into a summary. This keeps token usage low even for very long conversations.
"""

from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

def summary_memory_demo():
    print("=" * 60)
    print("1. ConversationSummaryMemory – Compressing History")
    print("=" * 60)

    # LLM will generate summary automatically
    memory = ConversationSummaryMemory(llm=model, return_messages=True)
    chain = ConversationChain(llm=model, memory=memory, verbose=False)

    turns = [
        "I'm planning a trip to Japan.",
        "I want to visit Tokyo and Kyoto.",
        "I have 10 days total.",
        "What's the best time to visit?",
        "I also love sushi.",
    ]

    for user_input in turns:
        response = chain.predict(input=user_input)
        print(f"User: {user_input}")
        print(f"AI: {response[:120]}...")
        print()

    print("📝 Current summary (compressed memory):")
    print(memory.load_memory_variables({})["history"])
    print("\n✅ The summary captures key facts without storing every word.")
    print("   Token usage stays low even after hundreds of turns.\n")

def summary_customization():
    print("=" * 60)
    print("2. Custom Summary Prompt")
    print("=" * 60)

    from langchain.memory import ConversationSummaryMemory
    from langchain_core.prompts import PromptTemplate

    custom_prompt = PromptTemplate.from_template(
        "Summarize this conversation focusing only on travel plans: {summary}"
    )
    memory = ConversationSummaryMemory(
        llm=model,
        prompt=custom_prompt,
        return_messages=True
    )
    memory.save_context({"input": "I want to go to Paris"}, {"output": "Paris is lovely in spring."})
    print("Summary with custom prompt:")
    print(memory.load_memory_variables({})["history"])

if __name__ == "__main__":
    print("\n Module 06-03: ConversationSummaryMemory\n")
    summary_memory_demo()
    summary_customization()