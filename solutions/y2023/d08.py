import math
import re


def parse(data):
    lines = data.splitlines()
    lr, nodes = lines[0], lines[2:]
    nodes = [re.findall(r"\w{3}", line) for line in nodes]
    return [0 if c == "L" else 1 for c in lr.strip()], {a: [b, c] for a, b, c in nodes}


def part1(lr, nodes):
    start = "AAA"
    steps = 0
    while True:
        for m in lr:
            start = nodes[start][m]
            steps += 1
        if start == "ZZZ":
            return steps


def part2(lr, nodes):
    starts = [node for node in nodes.keys() if node[-1] == "A"]
    loops = []

    for start in starts:
        current = start
        steps = 0
        while True:
            for m in lr:
                current = nodes[current][m]
                steps += 1
            if current[-1] == "Z":
                loops += [steps]
                break

    return math.lcm(*loops)


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
