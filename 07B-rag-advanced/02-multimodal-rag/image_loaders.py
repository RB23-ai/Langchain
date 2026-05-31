"""
Image Loaders – Load images from local paths or URLs.
"""

from langchain.document_loaders import ImageCaptionLoader
from PIL import Image
import requests

def load_image_from_path(path: str):
    """Load image as PIL Image."""
    return Image.open(path)

def load_image_from_url(url: str):
    """Download image from URL."""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    return Image.open(response.raw)

# Using LangChain's ImageCaptionLoader (requires BLIP or similar)
def image_caption_loader(image_paths):
    loader = ImageCaptionLoader(paths=image_paths)
    documents = loader.load()
    return documents

if __name__ == "__main__":
    # Example: load and get caption
    # docs = image_caption_loader(["path/to/image.jpg"])
    # print(docs[0].page_content)
    pass