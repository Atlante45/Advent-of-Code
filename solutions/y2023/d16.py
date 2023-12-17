from collections import defaultdict, deque


DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ITEM = {
    ".": [[0], [1], [2], [3]],
    "/": [[1], [0], [3], [2]],
    "\\": [[3], [2], [1], [0]],
    "|": [[0], [0, 2], [2], [0, 2]],
    "-": [[3, 1], [1], [3, 1], [3]],
}


def valid(grid, i, j):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])


def parse(data):
    return [list(line) for line in data.splitlines()]


def solve(grid, i, j, d):
    history = defaultdict(list)

    frontier = deque()
    frontier.append((i, j, d))
    while len(frontier) > 0:
        i, j, d = frontier.pop()
        if not valid(grid, i, j) or ((i, j) in history and d in history[(i, j)]):
            continue
        history[(i, j)].append(d)

        frontier.extend(
            [(i + DIR[dir][0], j + DIR[dir][1], dir) for dir in ITEM[grid[i][j]][d]]
        )

    return len(history)


def part1(grid):
    return solve(grid, 0, 0, 1)


def part2(grid):
    res = 0
    for i in range(len(grid)):
        res = max(res, solve(grid, i, 0, 1))
        res = max(res, solve(grid, i, len(grid[0]) - 1, 3))

    for i in range(len(grid[0])):
        res = max(res, solve(grid, 0, i, 2))
        res = max(res, solve(grid, len(grid) - 1, i, 0))
    return res


TEST_DATA = {}
TEST_DATA[
    """\
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
""".rstrip()
] = (46, 51)
