#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data

import re


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def parsePoints(line):
    x = re.search("^([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)", line)
    return (
        Point(int(x.group(1)), int(x.group(2))),
        Point(int(x.group(3)), int(x.group(4))),
    )


def computeLine(p1, p2, straightLinesOnly):
    vx = p2.x - p1.x
    vy = p2.y - p1.y
    s = max(abs(vx), abs(vy))
    vx /= s
    vy /= s

    if straightLinesOnly and vx != 0 and vy != 0:
        return []

    return [Point(p1.x + i * vx, p1.y + i * vy) for i in range(s + 1)]


def printVents(vents, n, m):
    string = ""
    for y in range(m + 1):
        for x in range(n + 1):
            string += str(vents.get((x, y), "."))
        string += "\n"
    print(string)


def countVents(lines, straightLinesOnly):
    vents = {}

    n = 0
    m = 0

    for line in lines:
        (p1, p2) = parsePoints(line)
        n = max(n, max(p1.x, p2.x))
        m = max(m, max(p1.y, p2.y))

        line = computeLine(p1, p2, straightLinesOnly)
        for p in line:
            numVents = vents.get((p.x, p.y), 0)
            vents[(p.x, p.y)] = numVents + 1

    # printVents(vents, n, m)

    count = 0
    for v in vents.values():
        if v > 1:
            count += 1

    return count


def part1(lines):
    return countVents(lines, True)


def part2(lines):
    return countVents(lines, False)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (4421, 18674)
TEST_RESULT = (5, 12)
TEST_DATA = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
