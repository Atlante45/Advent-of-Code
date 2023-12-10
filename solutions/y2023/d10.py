from solutions.utils.graph import dijkstra, neighbors4

LEFT = "S7J-"
RIGHT = "SFL-"
UP = "SLJ|"
DOWN = "SF7|"


def find_start(grid, neighbors):
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "S":
                si, sj = i, j

    ns = [(i - si, j - sj) for i, j in neighbors((si, sj))]
    if (-1, 0) in ns and (1, 0) in ns:
        grid[si][sj] = "|"
    elif (-1, 0) in ns and (0, -1) in ns:
        grid[si][sj] = "J"
    elif (-1, 0) in ns and (0, 1) in ns:
        grid[si][sj] = "L"
    elif (1, 0) in ns and (0, -1) in ns:
        grid[si][sj] = "7"
    elif (1, 0) in ns and (0, 1) in ns:
        grid[si][sj] = "F"
    elif (0, -1) in ns and (0, 1) in ns:
        grid[si][sj] = "-"

    return (si, sj)


def parse(data):
    grid = [list(line) for line in data.splitlines()]

    def neighbors(p):
        ns = []
        i, j = p
        fro = grid[i][j]
        for a, b in neighbors4(i, j, grid):
            to = grid[a][b]
            if a == i - 1 and fro in UP and to in DOWN:
                ns += [(a, b)]
            elif a == i + 1 and fro in DOWN and to in UP:
                ns += [(a, b)]
            elif b == j - 1 and fro in LEFT and to in RIGHT:
                ns += [(a, b)]
            elif b == j + 1 and fro in RIGHT and to in LEFT:
                ns += [(a, b)]
        return ns

    start = find_start(grid, neighbors)

    _, cost_so_far = dijkstra(start, neighbors)
    return grid, cost_so_far


def part1(_, cost_so_far):
    return len(cost_so_far.keys()) // 2


def part2(grid, cost_so_far):
    loop = cost_so_far.keys()

    res = 0
    for i, row in enumerate(grid):
        inside = False
        for j, c in enumerate(row):
            if inside and (i, j) not in loop:
                res += 1
            elif c in UP and (i, j) in loop:
                inside = not inside
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
