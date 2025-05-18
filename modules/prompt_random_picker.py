import random
from modules.db_connection import get_connection

"""
Random Prompt Selector

This module provides a utility function to randomly select a reading challenge prompt
from the database. Used for page 3 of the app.
"""


def get_random_prompt():
    """
    Retrieve a random reading challenge prompt from the database.

    Returns:
        tuple or (None, None): A tuple (id, text) of the selected prompt,
        or (None, None) if no prompts are found in the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, text FROM prompts")
    prompts = cursor.fetchall()

    conn.close()

    if not prompts:
        return None, None

    return random.choice(prompts)  # returns (id, text)