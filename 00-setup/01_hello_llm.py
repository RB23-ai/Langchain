
"""
Hello, LangChain – the minimal working example.

This script:
1. Loads environment variables from .env
2. Initializes a chat model using LangChain's unified init_chat_model
3. Invokes the model with a simple prompt
4. Prints the response

If you see a friendly greeting, your setup works!
"""

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load API keys from .env file
load_dotenv()

def main():
    print("\n LangChain Setup Check\n")
    
    # Determine which provider to use (first available wins)
    # You can change the order or comment out providers you don't have
    if os.getenv("OPENAI_API_KEY"):
        model_id = "openai:gpt-4o-mini"
        print(" Using OpenAI (gpt-4o-mini)")
    elif os.getenv("GROQ_API_KEY"):
        model_id = "groq:llama-3.3-70b-versatile"
        print(" Using Groq (llama-3.3-70b)")
    elif os.getenv("ANTHROPIC_API_KEY"):
        model_id = "anthropic:claude-3-5-haiku-latest"
        print(" Using Anthropic (Claude 3.5 Haiku)")
    else:
        # Fallback to local Ollama if installed and running
        try:
            model_id = "ollama:llama3.2:3b"
            print(" Using Ollama (local, llama3.2)")
        except Exception:
            print(" No API key found and Ollama not available.")
            print("   Please set OPENAI_API_KEY, GROQ_API_KEY, or run 'ollama serve'.")
            return
    
    # Initialize the model
    model = init_chat_model(model_id, temperature=0.7)
    
    # Invoke with a simple test prompt
    response = model.invoke("Say 'Hello, world! I am running LangChain.' in exactly that sentence, nothing else.")
    
    print("\n Model response:\n")
    print(response.content)
    print("\n Setup successful! You are ready for Module 01.\n")

if __name__ == "__main__":
    main()