from collections import defaultdict
from itertools import count
from math import ceil, sqrt


def parse(data):
    return int(data.strip())


def coords(index):
    sqrt_index = sqrt(index)
    radius = ceil((sqrt_index - 1) / 2)
    offset = index - max(0, 2 * (radius - 1) + 1) ** 2
    a = offset % max(1, 2 * radius)
    b = offset // max(1, 2 * radius)
    x, y = radius, a - radius
    if b % 4 in [1, 3]:
        x, y = -y, x
    if b % 4 in [2, 3]:
        x, y = -x, -y
    return x, y


def part1(index):
    return sum(abs(c) for c in coords(index))


def part2(index):
    grid = defaultdict(int)
    for v in count(1):
        i, j = coords(v)
        cells = [
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1),
            (i - 1, j - 1),
            (i - 1, j + 1),
            (i + 1, j - 1),
            (i + 1, j + 1),
        ]
        grid[i, j] = max(1, sum(grid[x, y] for x, y in cells))

        if grid[i, j] > index:
            return grid[i, j]


TEST_DATA = {}
TEST_DATA[
    """\
1
""".rstrip()
] = (0, None)
TEST_DATA[
    """\
12
""".rstrip()
] = (3, None)
TEST_DATA[
    """\
23
""".rstrip()
] = (2, None)
TEST_DATA[
    """\
1024
""".rstrip()
] = (31, None)
