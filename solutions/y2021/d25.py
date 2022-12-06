#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data

import copy


def part1(input):
    res = 0
    while True:
        moved = False
        new_input = copy.deepcopy(input)
        for i in range(len(input)):
            for j in range(len(input[0])):
                j2 = (j + 1) % len(input[0])
                if input[i][j] == ">" and input[i][j2] == ".":
                    new_input[i][j] = "."
                    new_input[i][j2] = ">"
                    moved = True

        input = new_input
        new_input = copy.deepcopy(input)

        for i in range(len(input)):
            for j in range(len(input[0])):
                i2 = (i + 1) % len(input)
                if input[i][j] == "v" and input[i2][j] == ".":
                    new_input[i][j] = "."
                    new_input[i2][j] = "v"
                    moved = True
        input = new_input

        res += 1
        if not moved:
            break

    return res


def part2(input):
    pass


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = [list(line) for line in data.splitlines()]

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (419, None)
TEST_RESULT = (58, None)
TEST_DATA = """\
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
