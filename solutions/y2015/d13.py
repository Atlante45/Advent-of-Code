from collections import defaultdict
from itertools import permutations

from more_itertools import pairwise


import re

REGEX = r"^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)."


def parse_data(data):
    nodes = set()
    edges = defaultdict(int)
    for line in data:
        a, sign, units, b = re.search(REGEX, line).groups()
        nodes.add(a)
        edges[(a, b)] = (-1 if sign == "lose" else 1) * int(units)

    return nodes, edges


def happiness(edges, perm):
    total = sum(edges[(a, b)] + edges[(b, a)] for a, b in pairwise(perm))
    return total + edges[(perm[0], perm[-1])] + edges[(perm[-1], perm[0])]


def parse(data):
    return data.splitlines()


def part1(data):
    nodes, edges = parse_data(data)
    return max(happiness(edges, perm) for perm in permutations(nodes))


def part2(data):
    nodes, edges = parse_data(data)
    nodes.add("Me!")
    return max(happiness(edges, perm) for perm in permutations(nodes))


TEST_DATA = {}
TEST_DATA[
    """\
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
""".rstrip()
] = (330, 286)
