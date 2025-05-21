import random
from modules.db_connection import get_connection


def get_random_book():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT title, author, blurb, genre, pages FROM books WHERE blurb IS NOT NULL")
    books = cursor.fetchall()

    if books:
        return random.choice(books)
    else:
        return None