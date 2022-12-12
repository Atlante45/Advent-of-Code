#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data

from solutions.utils.graph import dijkstra, neighbors4


def parse(data):
    start = end = None

    heightmap = []
    for r, line in enumerate(data):
        row = []
        for c, p in enumerate(line):
            match p:
                case "S":
                    row.append(0)
                    start = (r, c)
                case "E":
                    row.append(25)
                    end = (r, c)
                case _:
                    row.append(ord(p) - ord("a"))
        heightmap.append(row)
    return start, end, heightmap


def part1(data):
    start, end, heightmap = parse(data)

    def neighbors(n):
        i, j = n
        return [
            (x, y)
            for (x, y) in neighbors4(i, j, heightmap)
            if heightmap[x][y] <= heightmap[i][j] + 1
        ]

    _, cost_so_far = dijkstra(start, neighbors)
    return cost_so_far[end]


def part2(data):
    _, end, heightmap = parse(data)

    def neighbors(n):
        i, j = n
        return [
            (x, y)
            for (x, y) in neighbors4(i, j, heightmap)
            if heightmap[x][y] <= heightmap[i][j] + 1
        ]

    starts = []
    for i, r in enumerate(heightmap):
        for j, c in enumerate(r):
            if heightmap[i][j] == 0:
                starts.append((i, j))

    _, cost_so_far = dijkstra(starts, neighbors)
    return cost_so_far[end]


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (484, 478)
TEST_RESULT = (31, 29)
TEST_DATA = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
