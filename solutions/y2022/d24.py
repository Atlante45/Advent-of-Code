from collections import defaultdict

from solutions.utils.graph import neighbors4


def parse(data):
    lines = data.splitlines()
    blizzards = defaultdict(list)
    for j, row in enumerate(lines[1:-1]):
        for i, v in enumerate(row[1:-1]):
            match v:
                case "<":
                    blizzards[None, j] += [(i, -1)]
                case ">":
                    blizzards[None, j] += [(i, 1)]
                case "^":
                    blizzards[i, None] += [(j, -1)]
                case "v":
                    blizzards[i, None] += [(j, 1)]
    return blizzards, (len(lines[0]) - 2, len(lines) - 2)


def step(blizzards, size, positions, goal, t):
    if goal in positions:
        return t + 1

    board = set()
    for (x, y), l in blizzards.items():
        match x, y:
            case None, _:
                board.update([((v + (t + 1) * d) % size[0], y) for v, d in l])
            case _, None:
                board.update([(x, (v + (t + 1) * d) % size[1]) for v, d in l])

    new_positions = set()
    for pos in positions:
        for p in [pos] + neighbors4(pos[0], pos[1], size[0], size[1]):
            if p not in board:
                new_positions.add(p)

    return step(blizzards, size, new_positions, goal, t + 1)


def part1(blizzards, size):
    return step(blizzards, size, set([(0, -1)]), (size[0] - 1, size[1] - 1), 0)


def part2(blizzards, size):
    t1 = step(blizzards, size, set([(0, -1)]), (size[0] - 1, size[1] - 1), 0)
    t2 = step(blizzards, size, set([(size[0] - 1, size[1])]), (0, 0), t1)
    return step(blizzards, size, set([(0, -1)]), (size[0] - 1, size[1] - 1), t2)


TEST_DATA = {}
TEST_DATA[
    """\
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
""".rstrip()
] = (18, 54)
