from modules.prompt_analyzer import looks_like_structured_query

"""
Prompt Router

This module handles routing reading challenge prompts to the appropriate matching strategy
based on whether the prompt follows a recognizable, rule-based structure.

Supported strategies:
    - "sql": For prompts that match known patterns and can be translated into SQL filters.
    - "semantic": For abstract or creative prompts that require interpretation by a language model.

Example:
    >>> route_challenge_input("A book with more than 300 pages")
    ("sql", [{"type": "pages_more_than", "text": "more than 300 pages", "value": "300"}])

Dependencies:
    - prompt_analyzer.looks_like_structured_query()
"""


def route_challenge_input(prompt_text):
    """
    Determine the appropriate processing strategy for a reading challenge prompt.

    Parameters:
        prompt_text (str): The user's input prompt describing a reading challenge.

    Returns:
        tuple: A tuple in the form (route_label, data), where:
            - route_label (str): Either "sql" for structured prompts or "semantic" as a fallback.
            - data: A list of extracted filters (for "sql") or the original prompt text (for "semantic").
    """
    filters = looks_like_structured_query(prompt_text)

    if filters:
        return "sql", filters

    # Placeholder for future expansion:
    # elif looks_like_semantic_prompt(prompt_text):
    #     return "semantic", prompt_text

    return "semantic", prompt_text  # fallback
