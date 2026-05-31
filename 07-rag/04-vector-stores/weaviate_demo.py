"""
Weaviate – Self-hosted or cloud, supports hybrid search.
"""

from langchain_weaviate import WeaviateVectorStore
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = WeaviateVectorStore.from_texts(
    ["Doc1", "Doc2"],
    embeddings,
    weaviate_url="http://localhost:8080"
)