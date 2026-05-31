#!/usr/bin/env python
"""
Document Loader: YouTube

Extracts transcript from a YouTube video.
"""

from langchain_community.document_loaders import YoutubeLoader

url = "https://youtu.be/7xTGNNLPyMI?si=MocYDors-GG2T-rQ"
loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
documents = loader.load()
print(f"Title: {documents[0].metadata['title']}")
print(f"Transcript length: {len(documents[0].page_content)} chars")