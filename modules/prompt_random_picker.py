
import random
from modules.db_connection import get_connection


def get_random_prompt():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, text FROM prompts")
    prompts = cursor.fetchall()

    conn.close()

    if not prompts:
        return None, None

    return random.choice(prompts)  # returns (id, text)