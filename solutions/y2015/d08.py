#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data

import re

REGEX = r"(\\\\|\\\"|\\x[0-9A-Fa-f]{2})"


def part1(data):
    file_chars = sum(len(line) for line in data.splitlines())
    data = re.sub(REGEX, ".", data)
    disk_chars = sum(len(line) - 2 for line in data.splitlines())

    return file_chars - disk_chars


def part2(data):
    file_chars = sum(len(line) for line in data.splitlines())
    expanded_chars = sum(
        len(line) + line.count('"') + line.count("\\") + 2 for line in data.splitlines()
    )
    return expanded_chars - file_chars


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (1371, 2117)
TEST_RESULT = (12, 19)
TEST_DATA = """\
""
"abc"
"aaa\\"aaa"
"\\x27"
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
