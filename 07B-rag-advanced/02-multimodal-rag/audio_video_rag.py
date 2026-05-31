"""
Audio/Video RAG – Transcribe audio/video and add to index.
"""

from langchain_community.document_loaders import YoutubeLoader
import whisper

def transcribe_audio(audio_path: str) -> str:
    """Use Whisper to transcribe audio file."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

def load_youtube_transcript(url: str):
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
    docs = loader.load()
    return docs[0].page_content

if __name__ == "__main__":
    # text = load_youtube_transcript("https://www.youtube.com/watch?v=...")
    # print(text[:500])
    pass