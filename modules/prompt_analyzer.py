import re

"""
Prompt Analyzer

This module provides simple, rule-based parsing tools for analyzing reading challenge prompts.
It detects whether a prompt contains structured patterns that can be interpreted as SQL-style filters,
enabling fast and interpretable book matching without requiring a language model or vector search.

Supported pattern types include:
    - Page count comparisons (e.g., "more than 300 pages")
    - Publication year filters (e.g., "published before 1990")
    - Title keyword searches (e.g., "title contains the word 'space'")

Example:
    >>> looks_like_structured_query("A book with less than 250 pages")
    [{'type': 'pages_less_than', 'text': 'less than 250 pages', 'value': '250'}]
"""


def looks_like_structured_query(text):
    """
    Analyze a prompt for rule-based patterns related to pages, publication year, or title keywords.

    Parameters:
        text (str): The prompt text to analyze.

    Returns:
        List[dict]: A list of detected pattern matches. Each dictionary contains:
            - 'type': A string identifier for the type of pattern (e.g., 'pages_less_than').
            - 'text': The matched text fragment.
            - 'value': The extracted numeric or keyword value from the match.

    Supported patterns:
        - "more than <N> pages"
        - "less than <N> pages"
        - "published before <YEAR>"
        - "published in <YEAR>"
        - "title contains/includes 'WORD'"
    """
    patterns = {
        "pages_more_than": r"\bmore than (\d+) pages\b",
        "pages_less_than": r"\bless than (\d+) pages\b",
        "published_before": r"\bpublished before (\d{4})\b",
        "published_in": r"\bpublished in(?: the year)? (\d{4})\b",
        "title_contains_1": r"(?:the\s)?word ['\"](\w+)['\"] (?:can be found|is|appears)? (?:in|in the)? title",
        "title_contains_2": r"title (?:has|contains|includes) (?:the word )?['\"](\w+)['\"]"
    }

    matches = []

    for label, pattern in patterns.items():
        match = re.search(pattern, text.lower())
        if match:
            matches.append({
                "type": label,
                "text": match.group(0),
                "value": match.group(1)
            })

    return matches
