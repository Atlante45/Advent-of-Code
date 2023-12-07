CARD_ORDER = "_23456789TJQKA"


def order(hand):
    hand, _ = hand
    cards = {card: hand.count(card) for card in hand if card != "_"}
    counts = sorted(cards.values(), reverse=True) + [0, 0]
    counts[0] += hand.count("_")
    return (counts[0], counts[1]) + tuple(CARD_ORDER.index(c) for c in hand)


def solve(hands):
    return sum(i * bid for i, [_, bid] in enumerate(sorted(hands, key=order), 1))


def parse(data):
    lines = [line.split() for line in data.splitlines()]
    return [(hand, int(bid)) for hand, bid in lines]


def part1(hands):
    return solve(hands)


def part2(hands):
    hands = [(hand.replace("J", "_"), bid) for (hand, bid) in hands]
    return solve(hands)


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
