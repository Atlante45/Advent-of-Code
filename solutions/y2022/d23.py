from collections import Counter
from itertools import count


def n8(i, j):
    return [
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
        (i - 1, j - 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i + 1, j + 1),
    ]


def n3(i, j, d):
    match d:
        case 0:
            return [
                (i - 1, j - 1),
                (i, j - 1),
                (i + 1, j - 1),
            ]
        case 1:
            return [
                (i - 1, j + 1),
                (i, j + 1),
                (i + 1, j + 1),
            ]
        case 2:
            return [
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
            ]
        case 3:
            return [
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1),
            ]


def dir(i, j, d):
    match d:
        case 0:
            return (i, j - 1)
        case 1:
            return (i, j + 1)
        case 2:
            return (i - 1, j)
        case 3:
            return (i + 1, j)


def parse(data: str):
    elves = set()
    for y, row in enumerate(data.splitlines()):
        for x, tile in enumerate(row):
            if tile == "#":
                elves.add((x, y))

    return elves


def plan(elves, round):
    moves = {}
    for (x, y) in elves:
        if not any(n for n in n8(x, y) if n in elves):
            continue
        for i in range(4):
            d = (round + i) % 4
            if not any(n for n in n3(x, y, d) if n in elves):
                moves[(x, y)] = dir(x, y, d)
                break
    return moves


def move(elves, moves):
    dest = dict(Counter(moves.values()))
    for fro, to in moves.items():
        if dest[to] > 1:
            continue
        elves.remove(fro)
        elves.add(to)


def part1(elves: set):
    for i in range(10):
        moves = plan(elves, i)
        move(elves, moves)

    xs, ys = zip(*elves)
    area = (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)
    return area - len(elves)


def part2(elves):
    for i in count():
        moves = plan(elves, i)
        if not moves:
            break
        move(elves, moves)

    return i + 1


TEST_DATA = {}
TEST_DATA[
    """\
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
""".rstrip()
] = (110, 20)
