"""
Pinecone – Managed cloud vector DB.
Requires PINECONE_API_KEY and PINECONE_ENVIRONMENT.
"""

from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = PineconeVectorStore.from_texts(
    ["Doc1", "Doc2"],
    embeddings,
    index_name="my-index"
)