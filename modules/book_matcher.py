from modules.db_connection import get_connection


def find_existing_book_match(prompt_id):
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