#!/usr/bin/env python3
from itertools import chain, repeat
from solutions.utils import logger
from aocd import data


def move_head(head, dir):
    x, y = head
    if dir == "R":
        return (x + 1, y)
    if dir == "L":
        return (x - 1, y)
    if dir == "U":
        return (x, y + 1)
    if dir == "D":
        return (x, y - 1)


def step(i):
    if i == 0:
        return 0
    return 1 if i > 0 else -1


def move_knot(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    if abs(dx) <= 1 and abs(dy) <= 1:
        return tail

    return (tail[0] + step(dx), tail[1] + step(dy))


def move_rope(num, moves):
    visited = set()
    knots = [(0, 0)] * num

    for move in moves:
        knots[0] = move_head(knots[0], move)
        for i in range(1, len(knots)):
            knots[i] = move_knot(knots[i - 1], knots[i])
        visited.add(knots[-1])

    return len(visited)


def part1(moves):
    return move_rope(2, moves)


def part2(moves):
    return move_rope(10, moves)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    moves = list(
        chain.from_iterable(
            repeat(line[0], int(line[2:])) for line in data.splitlines()
        )
    )

    ans_1 = part1(moves)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(moves)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (5883, 2367)
TEST_RESULT = (88, 36)
TEST_DATA = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
