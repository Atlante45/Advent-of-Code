#!/usr/bin/env python3
import re

from solutions.utils import logger
from aocd import data


def parse_line(line):
    a, b, c, d = list(map(int, re.search(r"^(\d+)-(\d+),(\d+)-(\d+)", line).groups()))
    return [(a, b), (c, d)]


def contained(sections):
    s1, s2 = sections
    low = max(s1[0], s2[0])
    high = min(s1[1], s2[1])
    return (low, high) == s1 or (low, high) == s2


def overlap(sections):
    s1, s2 = sections
    low = max(s1[0], s2[0])
    high = min(s1[1], s2[1])
    return low <= high


def compute(sections, func):
    return len(list(filter(func, sections)))


def part1(input):
    return compute(input, contained)


def part2(input):
    return compute(input, overlap)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = [parse_line(line) for line in data.splitlines()]

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (466, 865)
TEST_RESULT = (2, 4)
TEST_DATA = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
