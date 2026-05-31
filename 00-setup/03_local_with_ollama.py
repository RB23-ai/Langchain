
#!/usr/bin/env python
"""
Run a fully local LLM using Ollama – no API key, no internet required after setup.

Prerequisites:
1. Install Ollama from https://ollama.com/
2. Run `ollama serve` in a terminal (keep it running)
3. In another terminal, run `ollama pull llama3.2:3b` (or any other model)

This script will use the local model to answer a simple question.
"""

import subprocess
import sys
import time

def check_ollama_running():
    """Check if Ollama server is running."""
    try:
        subprocess.run(["ollama", "list"], capture_output=True, check=True)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False

def pull_model_if_missing(model_name):
    """Pull the model if not already present."""
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    if model_name not in result.stdout:
        print(f" Model '{model_name}' not found. Pulling now (this may take a few minutes)...")
        subprocess.run(["ollama", "pull", model_name], check=True)
        print(" Model pulled successfully.")

def query_ollama(model_name, prompt):
    """Send a prompt to Ollama and return the response."""
    import requests
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["response"]

def main():
    print("\n Local LLM with Ollama\n")
    
    if not check_ollama_running():
        print(" Ollama is not running. Please start it with: ollama serve")
        print("   Then run this script again.")
        return
    
    model = "llama3.2:3b"
    pull_model_if_missing(model)
    
    prompt = "Explain what a 'local LLM' is in one short sentence."
    print(f" Asking: {prompt}\n")
    
    start = time.time()
    response = query_ollama(model, prompt)
    elapsed = time.time() - start
    
    print(f"Response ({elapsed:.1f} seconds):\n{response}\n")
    print(" Local inference works! You can now use Ollama with any LangChain script.")
    print("   Just set the model string to 'ollama:llama3.2:3b'.")

if __name__ == "__main__":
    main()