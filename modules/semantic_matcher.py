from dotenv import load_dotenv
import os
import openai

from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam

"""
Semantic Genre Matcher Module

This module provides functionality to analyze reading challenge prompts
using LLMs for genre extraction.
"""


# Load variables from .env
load_dotenv()

# Set up OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)


def extract_genre_with_llm(prompt_text):
    """
    Uses LLM to determine if a reading challenge prompt EXPLICITLY requests a specific book genre.
    Returns a genre string ONLY if the genre is directly mentioned or very clearly implied, else None.

    Args:
        prompt_text (str): The reading challenge prompt text

    Returns:
        str or None: The identified genre or None if no genre was explicitly mentioned
    """

    system_prompt = (
        """
        You are a book genre expert. Your task is to determine if a reading challenge prompt 
        EXPLICITLY requests a book from a specific genre.

        ONLY return a genre if the genre is explicitly mentioned (e.g., "Read a fantasy book", 
        "Read a book in the thriller genre")

        DO NOT return a genre if:
        - The prompt only describes a topic or theme that COULD fit one or multiple genres 
          (e.g., "a book about a cult" could be thriller, horror, non-fiction, memoir, etc.)
        - The prompt describes story elements that appear across multiple genres 
          (e.g., "a book about war" could be historical fiction, memoir, military thriller, etc.)
        - You're making an assumption or educated guess rather than identifying a clear genre indicator

        Common genres include: Fantasy, Science Fiction, Mystery, Murder Mystery, Thriller, 
        Horror, Romance, Historical Fiction, Literary Fiction, Non-Fiction, Biography, Memoir, 
        Self-Help, Young Adult, Children's, Poetry, Drama, Dystopian, Adventure, Western, 
        Crime, Paranormal.

        When in doubt, respond with "None". It's better to return None than to guess incorrectly.
        """
    )

    user_prompt = (
        f'Reading Challenge Prompt: "{prompt_text}"\n\n'
        'Is a specific book genre EXPLICITLY requested?\n'
        'If yes, respond with ONLY the genre name.\n'
        'If no, respond with exactly "None".\n'
        'Remember: topics and themes that could fit multiple genres should return "None".'
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # or "gpt-3.5-turbo"
            messages=[
                ChatCompletionSystemMessageParam(role="system", content=system_prompt),
                ChatCompletionUserMessageParam(role="user", content=user_prompt),
            ],
            temperature=0.1
        )

        genre = response.choices[0].message.content.strip()
        return None if genre.lower() == "none" else genre
    except Exception as e:
        print(f"Error in genre extraction: {e}")
        return None