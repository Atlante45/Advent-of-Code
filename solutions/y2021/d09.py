#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data


def findNeighbors(heighmap, i, j):
    neighbors = []
    height = len(heighmap)
    width = len(heighmap[0])
    if i > 0:
        neighbors.append((i - 1, j))
    if i < height - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < width - 1:
        neighbors.append((i, j + 1))

    return neighbors


def findLowestPoints(heighmap):
    lowestPoints = []
    height = len(heighmap)
    width = len(heighmap[0])
    for i in range(height):
        for j in range(width):
            lowest = True
            for (i1, j1) in findNeighbors(heighmap, i, j):
                if heighmap[i][j] >= heighmap[i1][j1]:
                    lowest = False
                    break
            if lowest:
                lowestPoints += [(i, j)]

    return lowestPoints


def computeBasin(heighmap, i, j):
    res = 1
    heighmap[i][j] = 9
    for (i1, j1) in findNeighbors(heighmap, i, j):
        if heighmap[i1][j1] != 9:
            res += computeBasin(heighmap, i1, j1)

    return res


def part1(heighmap):
    res = 0

    for (i, j) in findLowestPoints(heighmap):
        res += 1 + heighmap[i][j]

    return res


def part2(heighmap):
    basins = []

    for (i, j) in findLowestPoints(heighmap):
        basins.append(computeBasin(heighmap, i, j))

    basins = sorted(basins)
    return basins[-3] * basins[-2] * basins[-1]


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    heighmap = []
    for line in data.splitlines():
        heighmap.append([int(v) for v in line.strip()])

    ans_1 = part1(heighmap)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(heighmap)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (514, 1103130)
TEST_RESULT = (15, 1134)
TEST_DATA = """\
2199943210
3987894921
9856789892
8767896789
9899965678
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
