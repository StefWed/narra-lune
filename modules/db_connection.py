import sqlite3
import os


def get_connection():
    db_path = "data/readingquest.db"
    print("Using database at:", os.path.abspath(db_path))
    return sqlite3.connect(db_path)