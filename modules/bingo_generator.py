import random

def generate_bingo_card():
    # Bingo uses columns B-I-N-G-O with ranges:
    # B: 1–15, I: 16–30, N: 31–45, G: 46–60, O: 61–75
    card = []
    ranges = {
        'B': list(range(1, 16)),
        'I': list(range(16, 31)),
        'N': list(range(31, 46)),
        'G': list(range(46, 61)),
        'O': list(range(61, 76)),
    }

    for col in 'BINGO':
        card.append(random.sample(ranges[col], 5))

    # Replace center with "JOKER"
    card[2][2] = "JOKER"

    # Transpose to row-wise format
    bingo_card = [list(row) for row in zip(*card)]
    return bingo_card

bingo = generate_bingo_card()
for row in bingo:
    print(row)