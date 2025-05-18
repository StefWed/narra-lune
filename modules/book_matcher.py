from modules.db_connection import get_connection

"""
Book Match Retrieval

This module provides a utility function for querying the database to check if a book
has already been matched to a specific reading challenge prompt.
"""


def find_existing_book_match(prompt_id):
    """
        Retrieve an existing book match for a given reading challenge prompt.

        This function queries the `challenge_books` table to find if a book has already
        been matched to the specified prompt. If a match exists, it returns basic book
        information such as title, author, blurb, genre, and page count.

        Parameters:
            prompt_id (int): The ID of the reading challenge prompt.

        Returns:
            tuple or None: A tuple containing (title, author, blurb, genre, pages) if a match is found,
                           or None if no match exists.
        """

    conn = get_connection()
    cursor = conn.cursor()

    # Step 1: Look for a match in challenge_books
    cursor.execute("""
        SELECT b.title, b.author, b.blurb, b.genre, b.pages
        FROM challenge_books cb
        JOIN books b ON cb.book_id = b.id
        WHERE cb.prompt_id = ?
    """, (prompt_id,))

    result = cursor.fetchone()
    conn.close()

    return result  # Will be None if no match exists