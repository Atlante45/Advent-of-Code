#!/usr/bin/env python3
import numpy as np
from solutions.utils import logger
from aocd import data

import re

REGEX = r"^\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"


def gen(sum, depth):
    for i in range(sum + 1):
        if depth > 2:
            for j in gen(sum - i, depth - 1):
                yield [i] + j
        else:
            yield [i, sum - i]


def parse_data(data):
    matrix = []
    cals = []
    for line in data:
        vals = list(map(int, re.search(REGEX, line).groups()))
        matrix.append(vals[:-1])
        cals.append(vals[-1])
    matrix = np.rot90(np.array(matrix), axes=(1, 0))
    cals.reverse()

    return matrix, cals


def compute_score(matrix, cals, vec):
    vec = np.array(vec)
    tcal = np.sum(np.matmul(cals, vec))
    vec = np.matmul(matrix, vec)
    if all(map(lambda i: i >= 0, vec)):
        return np.prod(vec), tcal

    return None, None


def parts(data):
    matrix, cals = parse_data(data)

    maximum = 0
    maximum_cals = 0
    for vec in gen(100, len(data)):
        score, tcal = compute_score(matrix, cals, vec)
        if not score:
            continue

        maximum = max(maximum, score)
        if tcal == 500:
            maximum_cals = max(maximum_cals, score)

    return maximum, maximum_cals


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1, ans_2 = parts(data)
    logger.debug_part(0, ans_1, result, debug)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (13882464, 11171160)
TEST_RESULT = (62842880, 57600000)
TEST_DATA = """\
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
