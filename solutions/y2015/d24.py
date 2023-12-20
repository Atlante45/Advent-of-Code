from itertools import combinations
from math import prod


def solve(gifts, target):
    for i in range(1, len(gifts)):
        qs = []
        for c in combinations(gifts, i):
            if sum(c) == target:
                qs += [prod(c)]
        if qs:
            return min(qs)


def parse(data):
    return [int(line) for line in data.splitlines()]


def part1(gifts):
    return solve(gifts, sum(gifts) // 3)


def part2(gifts):
    return solve(gifts, sum(gifts) // 4)


TEST_DATA = {}
TEST_DATA[
    """\
1
2
3
4
5
7
8
9
10
11
""".rstrip()
] = (99, 44)
