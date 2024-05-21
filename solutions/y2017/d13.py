from itertools import count


def parse(data):
    return [list(map(int, line.split(": "))) for line in data.splitlines()]


def part1(scanners):
    res = 0
    for depth, range in scanners:
        if depth % (2 * range - 2) == 0:
            res += depth * range
    return res


def part2(scanners):
    for i in count():
        if all((depth + i) % (2 * range - 2) for depth, range in scanners):
            return i


TEST_DATA = {}
TEST_DATA[
    """\
0: 3
1: 2
4: 4
6: 4
""".rstrip()
] = (24, None)
