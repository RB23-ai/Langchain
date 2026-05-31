"""
Chroma Vector Store – Local, persistent.
"""

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

docs = ["Doc1 content", "Doc2 content"]
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(docs, embeddings, persist_directory="./chroma_db")
vectorstore.persist()

query = "Doc1"
results = vectorstore.similarity_search(query, k=1)
print(results[0].page_content)