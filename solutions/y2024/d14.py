from itertools import count
from math import prod
import re

R1 = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")


def parse(data):
    return [tuple(map(int, R1.match(line).groups())) for line in data.splitlines()]


def part1(robots):
    res = [0, 0, 0, 0]

    for px, py, vx, vy in robots:
        px = (px + 100 * vx) % 101
        py = (py + 100 * vy) % 103

        if px == 50:
            continue
        if py == 51:
            continue

        i = 0
        if px > 50:
            i += 1

        if py > 51:
            i += 2
        res[i] += 1

    return prod(res)


def part2(robots):
    for x in count(1):
        grid = set()
        for px, py, vx, vy in robots:
            px = (px + x * vx) % 101
            py = (py + x * vy) % 103

            if (px, py) in grid:
                break
            grid.add((px, py))

        if len(grid) == len(robots):
            return x


TEST_DATA = {}
TEST_DATA[
    """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".rstrip()
] = (None, None)
