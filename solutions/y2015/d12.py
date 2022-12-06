#!/usr/bin/env python3
import json
from solutions.utils import logger
from aocd import data


def recurse(val, filter):
    res = 0
    if isinstance(val, dict):
        for k, v in val.items():
            if filter and v == "red":
                return 0
            res += recurse(k, filter) + recurse(v, filter)

    if isinstance(val, list):
        for v in val:
            res += recurse(v, filter)

    if isinstance(val, int):
        res += val

    return res


def part1(data):
    return recurse(data, False)


def part2(data):
    return recurse(data, True)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = json.loads(data)

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (None, None)
TEST_RESULT = (None, None)
TEST_DATA = """\
{"a":[-1,13]}
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
