from collections import defaultdict
from itertools import count

CARDS = "23456789TJQKA"
CARDS_ALT = "J23456789TQKA"


def order(hand):
    cards = defaultdict(int)

    score = 0
    for c in hand:
        score = 100 * score + CARDS.index(c)
        cards[c] += 1

    counts = sorted(cards.values())

    if counts[-1] == 5:
        score += 70000000000
    elif counts[-1] == 4:
        score += 60000000000
    elif counts[-1] == 3 and counts[-2] == 2:
        score += 50000000000
    elif counts[-1] == 3:
        score += 40000000000
    elif counts[-1] == 2 and counts[-2] == 2:
        score += 30000000000
    elif counts[-1] == 2:
        score += 20000000000
    else:
        score += 10000000000

    return score


def order_alt(hand):
    cards = defaultdict(int)

    score = 0
    for c in hand:
        score = 100 * score + CARDS_ALT.index(c)
        cards[c] += 1

    j_count = cards["J"]
    del cards["J"]
    counts = sorted(cards.values())

    if j_count == 5 or (counts[-1] + j_count) == 5:
        score += 70000000000
    elif (counts[-1] + j_count) == 4:
        score += 60000000000
    elif (counts[-1] + j_count) == 3 and counts[-2] == 2:
        score += 50000000000
    elif counts[-1] == 3 and (counts[-2] + j_count) == 2:
        score += 50000000000
    elif (counts[-1] + j_count) == 3:
        score += 40000000000
    elif counts[-1] == 2 and (counts[-2] + j_count) == 2:
        score += 30000000000
    elif (counts[-1] + j_count) == 2:
        score += 20000000000
    else:
        score += 10000000000

    return score


def parse(data):
    return data.splitlines()


def part1(lines):
    lines = [line.split() for line in lines]

    hands = sorted(lines, key=lambda v: order(v[0]))

    return sum((i + 1) * int(hand[1]) for i, hand in enumerate(hands))


def part2(lines):
    lines = [line.split() for line in lines]

    hands = sorted(lines, key=lambda v: order_alt(v[0]))

    return sum((i + 1) * int(hand[1]) for i, hand in enumerate(hands))


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
