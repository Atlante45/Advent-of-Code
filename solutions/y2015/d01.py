#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data


def part1(input):
    return sum([1 if c == "(" else -1 for c in input])


def part2(input):
    floor = 0
    for i, c in enumerate(input):
        floor += 1 if c == "(" else -1
        if floor == -1:
            return i + 1


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.strip()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (138, 1771)
TEST_RESULT = (-1, 5)
TEST_DATA = """\
()())
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
