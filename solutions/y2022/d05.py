from curses.ascii import isalpha
from itertools import zip_longest
import re


def move_crates(crates, moves, move_func):
    stacks = filter(lambda s: s[-1] != " ", zip_longest(*crates, fillvalue=" "))
    stacks = list(map(lambda s: list(reversed(list(filter(isalpha, s)))), stacks))

    for move in moves:
        groups = re.search(r"^move (\d+) from (\d+) to (\d+)", move).groups()
        count, from_s, to_s = list(map(int, groups))

        stacks[to_s - 1] += move_func(stacks[from_s - 1][-count:])
        stacks[from_s - 1] = stacks[from_s - 1][:-count]

    return "".join(list(map(lambda s: s.pop(), stacks)))


def parse(data):
    data = data.splitlines()
    mid = data.index("")
    return data[:mid], data[mid + 1 :]


def part1(crates, moves):
    return move_crates(crates, moves, reversed)


def part2(crates, moves):
    return move_crates(crates, moves, lambda s: s)


TEST_DATA = {}
TEST_DATA[
    """\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".rstrip()
] = ("CMZ", "MCD")
