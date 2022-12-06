#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data


def part1(input):
    x = 0
    z = 0

    for line in input:
        line = line.split()

        direction = line[0]
        length = int(line[1])
        if direction == "forward":
            x += length
        elif direction == "up":
            z -= length
        elif direction == "down":
            z += length

    return x * z


def part2(input):
    aim = 0
    x = 0
    z = 0

    for line in input:
        line = line.split()

        direction = line[0]
        length = int(line[1])
        if direction == "forward":
            x += length
            z += aim * length
        elif direction == "up":
            aim -= length
        elif direction == "down":
            aim += length

    return x * z


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (1815044, 1739283308)
TEST_RESULT = (150, 900)
TEST_DATA = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
