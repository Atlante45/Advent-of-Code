import math


def parse(data):
    return data.splitlines()


def part1(input):
    res = 0
    for line in input:
        w, h, d = [int(v) for v in line.strip().split("x")]
        sides = sorted([w * h, w * d, h * d])
        res += sum([2 * a for a in sides]) + sides[0]

    return res


def part2(input):
    res = 0
    for line in input:
        edges = sorted([int(v) for v in line.strip().split("x")])
        res += 2 * edges[0] + 2 * edges[1] + math.prod(edges)

    return res


TEST_DATA = {}
TEST_DATA[
    """\
2x3x4
""".rstrip()
] = (58, 34)
TEST_DATA[
    """\
1x1x10
""".rstrip()
] = (43, 14)
