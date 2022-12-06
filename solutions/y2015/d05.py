#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data

VOWELS = "aeiou"
BAD = ["ab", "cd", "pq", "xy"]


def part1(input):
    res = 0

    for line in input:
        if sum([c in VOWELS for c in line]) < 3:
            continue
        if any([k in line for k in BAD]):
            continue
        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                res += 1
                break

    return res


def part2(input):
    res = 0
    for line in input:
        cond1, cond2 = False, False
        for i in range(len(line) - 2):
            cond1 = cond1 or line[i : i + 2] in line[i + 2 :]
            cond2 = cond2 or line[i] == line[i + 2]
            if cond1 and cond2:
                res += 1
                break

    return res


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (238, 69)
TEST_RESULT = (2, 0)
TEST_DATA = """\
turn on 1,10 through 5,15
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
