from itertools import cycle
from math import lcm
import re


def parse(data):
    lines = data.splitlines()
    lr, nodes = lines[0], lines[2:]
    nodes = [re.findall(r"\w{3}", line) for line in nodes]
    return [0 if c == "L" else 1 for c in lr.strip()], {a: [b, c] for a, b, c in nodes}


def solve(start, moves, nodes, win):
    for step, move in enumerate(cycle(moves), 1):
        start = nodes[start][move]
        if win(start):
            return step


def part1(moves, nodes):
    return solve("AAA", moves, nodes, lambda n: n == "ZZZ")


def part2(moves, nodes):
    starts = [node for node in nodes.keys() if node[-1] == "A"]
    return lcm(*[solve(s, moves, nodes, lambda n: n[-1] == "Z") for s in starts])


TEST_DATA = {}
TEST_DATA[
    """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".rstrip()
] = (6, None)
TEST_DATA[
    """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".rstrip()
] = (None, 6)
