#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data

import hashlib
from itertools import count


def find(input, prefix, start):
    for i in count(start):
        secret = input + str(i)
        if hashlib.md5(secret.encode()).hexdigest().startswith(prefix):
            return i


def part1(input, start):
    return find(input, "00000", start)


def part2(input, start):
    return find(input, "000000", start)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.strip()

    ans_1 = part1(data, 1)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data, ans_1)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (254575, 1038736)
TEST_RESULT = (609043, 6742839)
TEST_DATA = """\
abcdef
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
