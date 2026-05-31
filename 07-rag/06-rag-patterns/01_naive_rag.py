#!/usr/bin/env python
"""
RAG Pattern: Naive RAG

Basic retrieve → generate.
"""

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

docs = ["LangChain is a framework for LLM apps.", "RAG improves accuracy."]
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(docs, embeddings)
retriever = vectorstore.as_retriever()

prompt = ChatPromptTemplate.from_template("Context: {context}\nQuestion: {question}\nAnswer:")
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | ChatOpenAI(model="gpt-4o-mini")
    | StrOutputParser()
)
print(chain.invoke("What is LangChain?"))