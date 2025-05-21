from modules.prompt_analyzer import looks_like_structured_query
from modules.semantic_matcher import extract_genre_with_llm

"""
Prompt Router

This module handles routing reading challenge prompts to the appropriate matching strategy
based on whether the prompt follows a recognizable pattern.

Supported strategies:
    - "sql": For prompts that match known patterns and can be translated into SQL filters.
    - "genre": For prompts that specifically mention or imply a book genre.
    - "semantic": For abstract or creative prompts that require general interpretation.

Example:
    >>> route_challenge_input("A book with more than 300 pages")
    ("sql", [{"type": "pages_more_than", "text": "more than 300 pages", "value": "300"}])
"""


def route_challenge_input(prompt_text):
    """
    Determine the appropriate processing strategy for a reading challenge prompt.

    Parameters:
        prompt_text (str): The user's input prompt describing a reading challenge.

    Returns:
        tuple: A tuple in the form (route_label, data), where:
            - route_label (str): "sql" for structured prompts, "genre" for genre-based prompts,
              or "semantic" as a fallback.
            - data: A list of extracted filters (for "sql"), a genre string (for "genre"),
              or the original prompt text (for "semantic").
    """
    # First check if it's a structured query with recognizable patterns
    filters = looks_like_structured_query(prompt_text)
    if filters:
        return "sql", filters

    # Next, check if the prompt implies a specific genre
    extracted_genre = extract_genre_with_llm(prompt_text)
    if extracted_genre:
        return "genre", extracted_genre

    # Fall back to semantic matching for abstract prompts
    return "semantic", prompt_text
