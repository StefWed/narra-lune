import sqlite3

"""
Database Connection Utility

This module provides a helper function to establish a connection to the ReadingQuest
SQLite database. The database path is fixed and relative to the project structure.
"""


def get_connection():
    """
    Establish a connection to the ReadingQuest SQLite database.

    Returns:
        sqlite3.Connection: A connection object to the SQLite database located at 'data/readingquest.db'.
    """
    db_path = "data/readingquest.db"
    return sqlite3.connect(db_path)