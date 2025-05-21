from modules.db_connection import get_connection

"""
Rule-Based Matcher

This module converts structured prompt filters - such as those parsed by `prompt_analyzer` -
into SQL queries to find matching books in the database. It enables fast, interpretable
matching for prompts that follow clear, rule-based patterns.

Supported filter types:
    - "pages_more_than": pages > value
    - "pages_less_than": pages < value
    - "published_before": publishing_date < value
    - "published_in": publishing year == value
    - "title_contains_1" / "title_contains_2": title LIKE %value%
"""


def query_books_by_filters(filters):
    """
    Execute a rule-based SQL query to find a book that matches the given filters.

    Parameters:
        filters (list of dict): A list of dictionaries, each representing a structured filter.
            Each filter must include:
                - 'type' (str): The type of rule (e.g., 'pages_less_than').
                - 'value' (str): The value extracted from the prompt.

    Returns:
        tuple or None: A single matching book as a tuple (title, author, blurb, genre, pages),
        or None if no match is found.
    """
    conditions = []
    params = []

    # Debug: Print the filters we're processing
    print(f"Processing filters: {filters}")

    for f in filters:
        if f["type"] == "pages_more_than":
            conditions.append("pages > ?")
            params.append(int(f["value"]))
        elif f["type"] == "pages_less_than":
            conditions.append("pages < ?")
            params.append(int(f["value"]))
        elif f["type"] == "published_before":
            # Modified for integer pub_date
            conditions.append("pub_date < ?")
            params.append(int(f["value"]))
        elif f["type"] == "published_in":
            # Modified for integer pub_date - exact match on the year
            conditions.append("pub_date = ?")
            params.append(int(f["value"]))
        elif f["type"] in ("title_contains_1", "title_contains_2"):
            conditions.append("LOWER(title) LIKE ?")
            params.append(f"%{f['value'].lower()}%")

    if not conditions:
        return None

    where_clause = " AND ".join(conditions)
    sql = f"""
        SELECT title, author, blurb, genre, pages
        FROM books
        WHERE {where_clause}
        LIMIT 1
    """

    # Debug: Print the SQL and parameters
    print(f"SQL: {sql}")
    print(f"Params: {params}")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    result = cursor.fetchone()
    conn.close()

    # Debug: Print the result
    print(f"Query result: {result}")

    return result
