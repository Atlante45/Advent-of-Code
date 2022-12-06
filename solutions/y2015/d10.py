#!/usr/bin/env python3
from itertools import groupby
from solutions.utils import logger
from aocd import data


def look_and_say(seq):
    return "".join(str(len(list(g))) + k for k, g in groupby(seq))


def part1(data):
    for _ in range(40):
        data = look_and_say(data)

    return len(data), data


def part2(data):
    for _ in range(10):
        data = look_and_say(data)

    return len(data)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.strip()

    ans_1, data = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (None, None)
TEST_RESULT = (None, None)
TEST_DATA = """\

""".rstrip()

if __name__ == "__main__":
    # solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
