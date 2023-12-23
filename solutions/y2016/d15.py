from itertools import count
import re


REGEX = r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)."


def parse(data):
    discs = []
    for line in data.splitlines():
        disc, positions, position = map(int, re.match(REGEX, line).groups())
        discs.append(((position + disc) % positions, positions))
    return discs


def solve(discs):
    for i in count():
        if all((position + i) % positions == 0 for position, positions in discs):
            return i


def part1(discs):
    return solve(discs)


def part2(discs):
    discs.append((len(discs) + 1, 11))
    return solve(discs)


TEST_DATA = {}
TEST_DATA[
    """\
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
""".rstrip()
] = (5, None)
