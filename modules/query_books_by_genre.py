from modules.db_connection import get_connection


def query_books_by_genre(genre):
    """
    Query the database for books matching a specific genre.
    Returns a list of book tuples (title, author, blurb, genre, pages).
    """
    import random
    from modules.db_connection import get_connection

    if not genre:
        return None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Using LIKE with wildcards for more flexible genre matching
        query = """
        SELECT title, author, blurb, genre, pages 
        FROM books 
        WHERE LOWER(genre) LIKE ? 
        ORDER BY RANDOM() 
        LIMIT 3
        """

        cursor.execute(query, (f'%{genre.lower()}%',))
        results = cursor.fetchall()
        conn.close()

        # Return a random book from the results or None if no books found
        return random.choice(results) if results else None

    except Exception as e:
        print(f"Database error when querying by genre: {e}")
        return None