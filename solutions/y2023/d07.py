from collections import defaultdict


def order(hand):
    CARDS = "23456789TJQKA"
    cards = defaultdict(int)

    cards_strength = 0
    for c in hand:
        cards_strength = 100 * cards_strength + CARDS.index(c)
        cards[c] += 1

    counts = sorted(cards.values(), reverse=True) + [0]

    hand_strength = 10 * counts[0] + counts[1]

    return hand_strength * pow(100, len(hand)) + cards_strength


def order_alt(hand):
    CARDS = "J23456789TQKA"
    cards = defaultdict(int)

    cards_strength = 0
    for c in hand:
        cards_strength = 100 * cards_strength + CARDS.index(c)
        cards[c] += 1

    j_count = cards["J"]
    del cards["J"]
    counts = sorted(cards.values(), reverse=True) + [0, 0]

    hand_strength = 10 * (counts[0] + j_count) + counts[1]

    return hand_strength * pow(100, len(hand)) + cards_strength


def parse(data):
    return [line.split() for line in data.splitlines()]


def solve(lines, ordering):
    hands = sorted(lines, key=lambda v: ordering(v[0]))
    return sum((i + 1) * int(hand[1]) for i, hand in enumerate(hands))


def part1(lines):
    return solve(lines, order)


def part2(lines):
    return solve(lines, order_alt)


TEST_DATA = {}
TEST_DATA[
    """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".rstrip()
] = (6440, 5905)
