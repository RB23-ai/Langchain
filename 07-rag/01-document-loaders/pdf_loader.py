
"""
Document Loader: PDF

Uses PyPDFLoader to extract text from PDF files.
"""

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")
documents = loader.load()
print(f"Loaded {len(documents)} pages")
for doc in documents[:2]:
    print(f"Page {doc.metadata['page']}: {doc.page_content[:200]}...")