"""
Image Embeddings – Use CLIP to embed images and text into the same space.
"""

from sentence_transformers import SentenceTransformer
from PIL import Image
import torch

# Load CLIP model (supports both image and text)
model = SentenceTransformer('clip-ViT-B-32')

def embed_image(image: Image.Image):
    """Get embedding vector for an image."""
    return model.encode(image)

def embed_text(text: str):
    """Get embedding vector for text."""
    return model.encode(text)

def similarity(image_vec, text_vec):
    """Compute cosine similarity between image and text."""
    from sklearn.metrics.pairwise import cosine_similarity
    return cosine_similarity([image_vec], [text_vec])[0][0]

if __name__ == "__main__":
    # Example: image = Image.open("cat.jpg")
    # img_emb = embed_image(image)
    # txt_emb = embed_text("a cat")
    # print(similarity(img_emb, txt_emb))
    pass