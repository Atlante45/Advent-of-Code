#!/usr/bin/env python3
from itertools import chain, product
import time
from more_itertools import first, split_after
from math import prod

from solutions.utils import logger
from aocd import data


def outward(i, n, func):
    return [map(func, reversed(range(i))), map(func, range(i + 1, n))]


def is_visible(trees, a, b):
    ranges = chain(
        outward(a, len(trees), lambda i: trees[i][b]),
        outward(b, len(trees[a]), lambda j: trees[a][j]),
    )
    return any(map(lambda range: max(range) < trees[a][b], ranges))


def score(trees, a, b):
    ranges = chain(
        outward(a, len(trees), lambda i: trees[i][b]),
        outward(b, len(trees[a]), lambda j: trees[a][j]),
    )
    return prod(
        len(first(split_after(range, lambda x: x >= trees[a][b]))) for range in ranges
    )


def part1(data):
    trees = list(list(map(int, list(line))) for line in data)
    indices = product(range(1, len(data) - 1), range(1, len(data[0]) - 1))

    res = 2 * len(trees) + 2 * len(trees[0]) - 4
    res += sum(is_visible(trees, i, j) for i, j in indices)
    return res

def part2(data):
    trees = list(list(map(int, list(line))) for line in data)
    indices = product(range(1, len(data) - 1), range(1, len(data[0]) - 1))
    return max(score(trees, i, j) for i, j in indices)



def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (1849, 201600)
TEST_RESULT = (21, 8)
TEST_DATA = """\
30373
25512
65332
33549
35390
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
