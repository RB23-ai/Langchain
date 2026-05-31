# Choosing Your LLM Provider

LangChain 1.0 makes provider selection trivial – change one string, and everything still works.  
Here’s how to decide which provider to use while learning.

## Options at a glance

| Provider | Free tier | Speed | Quality | Setup effort |
|----------|-----------|-------|---------|--------------|
| **OpenAI** | No (pay‑as‑you‑go) | Fast | Highest | Low – get API key |
| **Groq** | Yes, generous | Very fast | High | Low – free API key |
| **Ollama** (local) | Yes, unlimited | Depends on your hardware | Good (llama3.2, qwen) | Medium – install Ollama |
| **Anthropic** | Limited free credits | Medium | Highest | Low – API key |
| **Google Gemini** | Yes (rate‑limited) | Fast | High | Low – API key |

## Recommendation for beginners

**Start with Groq** – free, very fast, and the code examples already use it.  
Sign up at [console.groq.com](https://console.groq.com/), get your API key, put it in `.env`.

**If you want zero cloud dependency** → Use Ollama (local). Install from [ollama.com](https://ollama.com/), run `ollama pull llama3.2:3b`, then the code will detect it automatically.

## How to change the provider in code

Every script in this repo uses `init_chat_model("provider:model-name")`.  
To switch, just change that string:

```python
# OpenAI
model = init_chat_model("openai:gpt-4o-mini")

# Groq
model = init_chat_model("groq:llama-3.3-70b-versatile")

# Anthropic
model = init_chat_model("anthropic:claude-3-5-haiku-latest")

# Ollama (local)
model = init_chat_model("ollama:llama3.2:3b")