import random

"""
Bingo Card Generator

This module provides a utility function for generating an HTML representation of a 5x5 word bingo card.
Each bingo card is filled with random words from a provided list, with a "JOKER" placed in the center cell.
"""


def generate_word_bingo_html(words):
    """
        Generate an HTML table representing a 5x5 bingo card filled with random words.

        The function selects 24 unique words at random from the input list and inserts a "JOKER" word
        in the center of the 5x5 grid (i.e., the 13th cell). The resulting bingo card is styled using inline CSS.

        Parameters:
            words (list of str): A list containing at least 24 unique words to populate the bingo card.

        Returns:
            str: An HTML string rendering the bingo card as a table.

        Raises:
            AssertionError: If the input list contains fewer than 24 words.
        """

    assert len(words) >= 24, "Need at least 24 unique words"
    selected = random.sample(words, 24)
    selected.insert(12, "JOKER")  # Center position in 5x5 grid

    html = "<table style='border-collapse: collapse; width: 100%; text-align: center;'>"
    for i in range(5):
        html += "<tr>"
        for j in range(5):
            word = selected[i*5 + j]

            bg_color = "#dcd6f7" if word == "JOKER" else "#f5f5fd"
            html += (
                f"<td style='border: 1px solid #888; padding: 20px; font-size: 16px; "
                f"background-color: {bg_color}; color: #222; text-align: center;'>"
                f"{word}</td>"
            )
        html += "</tr>"
    html += "</table>"
    return html
