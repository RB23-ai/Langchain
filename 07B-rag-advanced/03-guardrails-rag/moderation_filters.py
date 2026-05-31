"""
Moderation Filters – Use OpenAI's moderation API to block unsafe content.
"""

import openai
from langchain_openai import OpenAI

def moderate_text(text: str) -> bool:
    """Returns True if text is safe, False if flagged."""
    try:
        response = openai.Moderation.create(input=text)
        return not response["results"][0]["flagged"]
    except:
        # Fallback: assume safe if API fails
        return True

def moderate_context(context: str) -> str:
    """Filter unsafe content from context before passing to LLM."""
    # Simple: drop sentences containing flagged terms
    sentences = context.split('.')
    safe_sentences = [s for s in sentences if moderate_text(s)]
    return '. '.join(safe_sentences)