#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data

import math


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


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (1606483, 3842356)
TEST_RESULT = (58, 34)
TEST_DATA = """\
^>v<
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
