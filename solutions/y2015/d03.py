#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data


from collections import defaultdict


def move(coords, m):
    x, y = coords
    if m == "^":
        y += 1
    elif m == "v":
        y -= 1
    elif m == ">":
        x += 1
    elif m == "<":
        x -= 1
    return x, y


def part1(input):
    visits = defaultdict(int)
    coords = (0, 0)
    visits[coords] = 1
    for m in input[0].strip():
        coords = move(coords, m)
        visits[coords] += 1

    return len(visits)


def part2(input):
    visits = defaultdict(int)
    coords = [(0, 0), (0, 0)]
    visits[0, 0] = 1
    for i, m in enumerate(input[0].strip()):
        coords[i % 2] = move(coords[i % 2], m)
        visits[coords[i % 2]] += 1

    return len(visits)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (2081, 2341)
TEST_RESULT = (4, 3)
TEST_DATA = """\
^>v<
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
