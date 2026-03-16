import random

"""
Bingo Card Generator

This module provides utility functions for generating an HTML representation of a 5x5 word bingo card.
Each bingo card is filled with reading prompts from a provided list, with a "JOKER" placed in the center cell.
"""


def generate_word_bingo_html(prompts):
    """
        Generate an HTML table representing a 5x5 bingo card filled with randomly distributed prompts.

        The function selects 24 unique challenges at random from the input list and inserts a "JOKER" word
        in the center of the 5x5 grid (i.e., the 13th cell). The resulting bingo card is styled using inline CSS.

        Parameters:
            prompts (list of str): A list containing at least 24 unique reading challenges to populate the bingo card.

        Returns:
            str: An HTML string rendering the bingo card as a table.

        Raises:
            AssertionError: If the input list contains fewer than 24 challenges.
        """

    assert len(prompts) >= 24, "Need at least 24 unique words"
    selected = random.sample(prompts, 24)
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


def generate_fixed_bingo_html(prompts):
    """
    Generate an HTML bingo card from a fixed list of 25 reading challenges.
    The 13th element (index 12) should be the JOKER.
    """

    assert len(prompts) == 25, "Need exactly 25 words for a fixed bingo card"

    html = "<table style='border-collapse: collapse; width: 100%; text-align: center;'>"

    for i in range(5):
        html += "<tr>"
        for j in range(5):
            word = prompts[i * 5 + j]

            bg_color = "#dcd6f7" if word == "JOKER" else "#f5f5fd"

            html += (
                f"<td style='border: 1px solid #888; padding: 20px; font-size: 16px; "
                f"background-color: {bg_color}; color: #222; text-align: center;'>"
                f"{word}</td>"
            )

        html += "</tr>"

    html += "</table>"
    return html