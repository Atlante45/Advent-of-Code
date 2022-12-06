#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data


def part1(input):
    return max(input)


def part2(input):
    return sum(sorted(input)[-3:])


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = [sum(map(int, chunk.splitlines())) for chunk in data.split("\n\n")]

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (72511, 212117)
TEST_RESULT = (24000, 45000)
TEST_DATA = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
