#!/usr/bin/env python3
from curses.ascii import isalpha

from solutions.utils import logger
from aocd import data

import re


def move_crates(crates, moves, move_func):
    stacks = filter(lambda s: s[-1] != " ", zip(*crates))
    stacks = list(map(lambda s: list(reversed(list(filter(isalpha, s)))), stacks))

    for move in moves:
        groups = re.search(r"^move (\d+) from (\d+) to (\d+)", move).groups()
        count, from_s, to_s = list(map(int, groups))

        stacks[to_s - 1] += move_func(stacks[from_s - 1][-count:])
        stacks[from_s - 1] = stacks[from_s - 1][:-count]

    return "".join(list(map(lambda s: s.pop(), stacks)))


def part1(crates, moves):
    return move_crates(crates, moves, reversed)


def part2(crates, moves):
    return move_crates(crates, moves, lambda s: s)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()
    mid = data.index("")
    crates = data[:mid]
    moves = data[mid + 1 :]

    ans_1 = part1(crates, moves)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(crates, moves)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = ("RLFNRTNFB", "MHQTLJRLB")
TEST_RESULT = ("CMZ", "MCD")
TEST_DATA = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
