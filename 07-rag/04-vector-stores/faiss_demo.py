"""
FAISS – In-memory, fast.
"""

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

docs = ["Apple Inc.", "Microsoft Corp.", "Google LLC"]
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(docs, embeddings)
query = "tech company"
results = vectorstore.similarity_search(query, k=2)
for r in results:
    print(r.page_content)