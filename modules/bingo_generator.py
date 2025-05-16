import random


def generate_word_bingo_html(words, fixed_seed=None):

    if fixed_seed is not None:
        random.seed(fixed_seed)

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
