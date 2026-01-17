# LangChain Projects Collection

A comprehensive collection of LangChain implementations showcasing AI agents, RAG systems, vector databases, and more. This repository serves as a learning resource and reference for building LLM-powered applications.

##  Project Structure

```
Langchain/
├── Agent_langchain/          # AI Agents with tools and reasoning
│   ├── agents/              # Agent implementations
│   ├── tools/               # Custom tools for agents
│   ├── config/              # Configuration files
│   ├── utils/               # Utility functions
│   ├── main.py              # Main application entry point
│   ├── .env                 # Environment variables (template)
│   └── requirements.txt     # Python dependencies
│
├── RAG/                     #  Retrieval-Augmented Generation
│   ├── Vector/              # Vector database implementations
│   │   ├── 1.Chroma_DB_demo.ipynb
│   │   ├── 2.Pinecone_demo.ipynb
│   │   └── 3.Weaviate_demo.ipynb
│   ├── langchain_retrievers.py
│   └── langchain-text-splitters/  # Text splitting utilities
│
└── README.md               # This file
```

##  Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Weatherstack API key (optional, for weather agent)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/RB23-ai/Langchain.git
cd Langchain
```

2. **Set up the Weather Agent project**
```bash
cd Agent_langchain
pip install -r requirements.txt
```

3. **Configure environment variables**
```bash
# Create .env file from template
cp .env.example .env
# Edit .env with your API keys
```

4. **Run the Weather Agent**
```bash
python main.py
```

##  Project Configuration

### Environment Setup
Create a `.env` file in `Agent_langchain/` with:

```
# Required
OPENAI_API_KEY=your-openai-api-key-here

# Optional (for weather functionality)
WEATHERSTACK_API_KEY=your-weatherstack-api-key

# Optional (for RAG notebooks)
PINECONE_API_KEY=your-pinecone-api-key
WEAVIATE_API_KEY=your-weaviate-api-key
```

##  Detailed Usage

###  Running the Weather Agent

The Weather Agent demonstrates the ReAct (Reasoning + Acting) pattern:

```python
from agents.weather_agent import WeatherAgent

# Initialize agent
agent = WeatherAgent(model_name="gpt-3.5-turbo", temperature=0.7)

# Run queries
response = agent.get_formatted_response(
    "Find the capital of Madhya Pradesh, then find its current weather condition"
)
print(response)
```

**Example Queries:**
- "What's the weather like in Tokyo?"
- "Find the population of Paris and then check its weather"
- "Compare the weather between New York and London"

###  Exploring RAG Systems

The RAG directory contains Jupyter notebooks demonstrating different vector databases:

```bash
# Open ChromaDB tutorial
jupyter notebook RAG/Vector/1.Chroma_DB_demo.ipynb

# Open Pinecone tutorial  
jupyter notebook RAG/Vector/2.Pinecone_demo.ipynb

# Open Weaviate tutorial
jupyter notebook RAG/Vector/3.Weaviate_demo.ipynb
```

##  Features

### Agent Systems
- **Weather Agent**: ReAct-based agent with search and weather tools
- **Tool Integration**: DuckDuckGo search + Weatherstack API
- **Modular Architecture**: Clean separation of agents, tools, and configuration

### RAG Implementations
- **Multiple Vector Databases**: ChromaDB, Pinecone, Weaviate
- **Retrieval Systems**: Document retrieval and text splitting
- **Jupyter Notebooks**: Step-by-step tutorials with examples

### Technical Highlights
- **ReAct Agent Pattern**: Reasoning + Acting framework
- **Environment-Based Configuration**: Secure API key management
- **Production-Ready Structure**: Modular, extensible codebase

##  Use Cases

### Educational
- Learn LangChain agent patterns
- Understand RAG implementations
- Explore different vector databases
- Study production-ready project structure

### Practical Applications
- **Intelligent Assistants**: Build AI agents with specific tools
- **Knowledge Bases**: Create RAG systems for document retrieval
- **Research**: Experiment with different LLM architectures
- **Prototyping**: Quick-start templates for LangChain projects

##  Testing

Run the agent with sample queries:

```bash
# Interactive mode
cd Agent_langchain
python main.py

# Direct query
python -c "from agents.weather_agent import WeatherAgent; agent = WeatherAgent(); print(agent.get_formatted_response('Weather in London'))"
```

##  Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow existing code structure and patterns
- Add appropriate documentation
- Include example usage
- Update README if adding new features
- **Never commit API keys or secrets**

##  Security Notice

**Important**: This repository uses environment variables for API keys. Never commit actual API keys to version control.

If you accidentally commit an API key:
1. Rotate the key immediately
2. Remove it from git history
3. Update the `.env` file

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Contact

Project Maintainer: [Ruchika Bahatt](https://github.com/RB23-ai)

Project Link: [https://github.com/RB23-ai/Langchain](https://github.com/RB23-ai/Langchain)

---

## 📚 Learning Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [Vector Databases Explained](https://www.pinecone.io/learn/vector-database/)
- [RAG Tutorials](https://www.langchain.com/langchain-retrieval-augmented-generation)
