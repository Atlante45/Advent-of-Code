#!/usr/bin/env python3
from solutions.utils import logger, ocr
from aocd import data


def part1(data):
    res = 0
    x = 1
    t = 0
    for line in data:
        line = line.split()

        t += 1
        if t == 20 or (t - 20) % 40 == 0:
            res += t * x

        if line[0] == "addx":
            t += 1
            if t == 20 or (t - 20) % 40 == 0:
                res += t * x
            x += int(line[1])
    return res


def part2(data):
    res = ""
    x = 1
    t = 0
    for line in data:
        line = line.split()

        if t % 40 == 0:
            res += "\n"
        res += "#" if abs(x - t % 40) <= 1 else "."
        t += 1

        if line[0] == "addx":
            if t % 40 == 0:
                res += "\n"
            res += "#" if abs(x - t % 40) <= 1 else "."
            t += 1

            x += int(line[1])
    return ocr.parse(res.strip())


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (15120, "RKPJBPLA")
TEST_RESULT = (13140, None)
TEST_DATA = """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
