from queue import PriorityQueue
from typing import Counter

from more_itertools import pairwise
from solutions.utils.graph import dijkstra, neighbors4


def parse(data):
    return data.splitlines()


def find_start(lines, v="S"):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == v:
                return i, j
    return None


def djik(start, neighbors):
    starts = [start]
    frontier = PriorityQueue()
    came_from = {}
    cost_so_far = {}

    for start in starts:
        frontier.put(start, 0)
        came_from[start] = None
        cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        for next in neighbors(current):
            new_cost = cost_so_far[current] + 1

            if next in cost_so_far and cost_so_far[next] == new_cost:
                return new_cost, [next, current], came_from

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put(next, new_cost)
                came_from[next] = current

    return -1


def part1(lines):
    start = find_start(lines)

    def next(p):
        ns = []
        i, j = p
        fro = lines[i][j]
        for a, b in neighbors4(i, j, lines):
            to = lines[a][b]
            # print(fro, to, a, b)
            if (
                a == i - 1
                and (fro == "L" or fro == "J" or fro == "|" or fro == "S")
                and (to == "F" or to == "7" or to == "|")
            ):
                ns += [(a, b)]
            if (
                a == i + 1
                and (to == "L" or to == "J" or to == "|")
                and (fro == "F" or fro == "7" or fro == "|" or fro == "S")
            ):
                ns += [(a, b)]
            if (
                b == j - 1
                and (fro == "7" or fro == "J" or fro == "-" or fro == "S")
                and (to == "F" or to == "L" or to == "-")
            ):
                ns += [(a, b)]
            if (
                b == j + 1
                and (to == "7" or to == "J" or to == "-")
                and (fro == "F" or fro == "L" or fro == "-" or fro == "S")
            ):
                ns += [(a, b)]
        # print(p, ns)
        return ns

    # print(start)
    # print(next(start))

    res, _, _ = djik(start, next)
    return res


def propagate(lines, i, j, v):
    ps = [(i, j)]

    while len(ps) > 0:
        i, j = ps.pop()
        lines[i][j] = v
        for a, b in neighbors4(i, j, lines):
            if lines[a][b] == ".":
                ps.append((a, b))


def part2(lines):
    start = find_start(lines)

    def next(p):
        ns = []
        i, j = p
        fro = lines[i][j]
        for a, b in neighbors4(i, j, lines):
            to = lines[a][b]
            # print(fro, to, a, b)
            if (
                a == i - 1
                and (fro == "L" or fro == "J" or fro == "|" or fro == "S")
                and (to == "F" or to == "7" or to == "|")
            ):
                ns += [(a, b)]
            if (
                a == i + 1
                and (to == "L" or to == "J" or to == "|")
                and (fro == "F" or fro == "7" or fro == "|" or fro == "S")
            ):
                ns += [(a, b)]
            if (
                b == j - 1
                and (fro == "7" or fro == "J" or fro == "-" or fro == "S")
                and (to == "F" or to == "L" or to == "-")
            ):
                ns += [(a, b)]
            if (
                b == j + 1
                and (to == "7" or to == "J" or to == "-")
                and (fro == "F" or fro == "L" or fro == "-" or fro == "S")
            ):
                ns += [(a, b)]
        # print(p, ns)
        return ns

    # print(start)
    # print(next(start))

    _, fros, came_from = djik(start, next)

    lines = [list(line) for line in lines]
    # print("\n".join(["".join(l) for l in lines]))

    path = fros
    a, b = fros
    while a is not None:
        a = came_from[a]
        path.append(a)
    while b is not None:
        b = came_from[b]
        path.append(b)

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] in ["J", "L", "7", "F", "|", "-"] and (i, j) not in path:
                lines[i][j] = "."

    # start = find_start(lines, ".")
    # areas = []
    # while start is not None:
    #     areas.append(propagate(lines, *start, "I"))
    #     start = find_start(lines, ".")
    # print(areas)

    # print("\n".join(["".join(l) for l in lines]))

    new_lines = []
    for line in lines:
        new_line = [line[0]]
        for a, b in pairwise(line):
            new_line += [
                "-" if a in ["F", "L", "-", "S"] and b in ["7", "J", "-", "S"] else ".",
                b,
            ]
        new_lines.append(new_line)

    lines = new_lines

    # print("\n")
    # print("\n".join(["".join(l) for l in lines]))

    new_lines = [lines[0]]
    for a, b in pairwise(lines):
        new_line = []
        for i in range(len(lines[0])):
            new_line.append(
                "|"
                if a[i] in ["F", "7", "|", "S"] and b[i] in ["L", "J", "|", "S"]
                else "."
            )
        new_lines += [new_line, b]

    lines = new_lines

    # print("\n")
    # print("\n".join(["".join(l) for l in lines]))

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (
                i == 0 or j == 0 or i == len(lines) - 1 or j == len(lines[0]) - 1
            ) and lines[i][j] == ".":
                propagate(lines, i, j, "O")

    # print("\n".join(["".join(l) for l in lines]))

    res = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if i % 2 == 0 and j % 2 == 0 and lines[i][j] == ".":
                res += 1
    return res


TEST_DATA = {}
TEST_DATA[
    """\
.....
.S-7.
.|.|.
.L-J.
.....
""".rstrip()
] = (4, None)
TEST_DATA[
    """\
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".rstrip()
] = (8, None)
TEST_DATA[
    """\
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""".rstrip()
] = (None, 4)
TEST_DATA[
    """\
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""".rstrip()
] = (None, 8)
TEST_DATA[
    """\
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""".rstrip()
] = (None, 10)
