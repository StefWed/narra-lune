"""
Semantic Blurb Matcher

This module uses LLM reasoning to determine if a book's blurb satisfies a reading challenge prompt.
It queries a small set of books and uses the OpenAI API to evaluate each match.
"""

import os
import openai
from dotenv import load_dotenv
from modules.db_connection import get_connection

# Load environment variables
load_dotenv()

# Set up OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)


def query_books_by_llm(prompt_text, top_n=5):
    """
    Check which books match the given challenge prompt using LLM reasoning.

    Args:
        prompt_text (str): The reading challenge prompt
        top_n (int): Number of candidate books to evaluate

    Returns:
        tuple: (title, author, blurb, genre, pages) if a match is found, None otherwise
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Get top N candidate books (random selection for diversity)
    cursor.execute("""
        SELECT id, title, author, blurb, genre, pages 
        FROM books 
        WHERE blurb IS NOT NULL AND blurb != '' 
        ORDER BY RANDOM() 
        LIMIT ?
        """, (top_n,))
    books = cursor.fetchall()
    conn.close()

    if not books:
        return None

    for book_id, title, author, blurb, genre, pages in books:
        user_query = f"""
        Reading Challenge Prompt: "{prompt_text}"
        Book Title: "{title}" by {author}
        Blurb: "{blurb}"

        Question: Does this book fulfill the reading challenge prompt?
        Answer with ONLY "Yes" or "No" first, followed by a brief explanation (max 2 sentences).
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o",  # Using the gpt-4o model or you can use gpt-3.5-turbo
                messages=[{"role": "user", "content": user_query}],
                temperature=0.3
            )

            answer = response.choices[0].message.content.strip().lower()

            # If the response starts with "yes", consider it a match
            if answer.startswith("yes"):
                print(f"Match found: {title} - {answer}")
                return (title, author, blurb, genre, pages)

        except Exception as e:
            print(f"LLM error for book {title}: {e}")
            continue

    return None  # No match found