#!/usr/bin/env python3
from collections import defaultdict
from itertools import permutations

from more_itertools import pairwise
from solutions.utils import logger
from aocd import data

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


def part1(data):
    nodes, edges = parse_data(data)
    return max(happiness(edges, perm) for perm in permutations(nodes))


def part2(data):
    nodes, edges = parse_data(data)
    nodes.add("Me!")
    return max(happiness(edges, perm) for perm in permutations(nodes))


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (664, 640)
TEST_RESULT = (330, 286)
TEST_DATA = """\
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

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
