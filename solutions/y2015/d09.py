#!/usr/bin/env python3
from itertools import pairwise, permutations

from solutions.utils import logger
from aocd import data

import re

REGEX = r"^(\w+) to (\w+) = (\d+)$"


def cost(links, path):
    return sum(links[link] for link in pairwise(path))


def compute(links, locations, func):
    return func(cost(links, perm) for perm in permutations(locations))


def part1(links, locations):
    return compute(links, locations, min)


def part2(links, locations):
    return compute(links, locations, max)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    groups = [re.match(REGEX, line).groups() for line in data.splitlines()]

    locations = set()
    links = {}
    for a, b, d in groups:
        locations.add(a)
        locations.add(b)
        links[(a, b)] = links[(b, a)] = int(d)

    ans_1 = part1(links, locations)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(links, locations)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (141, 736)
TEST_RESULT = (605, 982)
TEST_DATA = """\
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
