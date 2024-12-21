from solutions.utils.graph import neighbors8


def parse(data):
    return data.splitlines()


def step(grid):
    new_grid = []
    for y, line in enumerate(grid):
        new_line = []
        for x, cell in enumerate(line):
            ns = [grid[ny][nx] for nx, ny in neighbors8(x, y, grid)]
            if cell == ".":
                new_line.append("|" if ns.count("|") >= 3 else ".")
            elif cell == "|":
                new_line.append("#" if ns.count("#") >= 3 else "|")
            else:
                new_line.append("#" if "#" in ns and "|" in ns else ".")
        new_grid.append(new_line)
    return new_grid


def resources(grid):
    return sum(line.count("|") for line in grid) * sum(line.count("#") for line in grid)


def parts(grid):
    p1res = None
    seen = {}
    for s in range(1000000000):
        if s == 10:
            p1res = resources(grid)

        grid = step(grid)
        lines_str = "\n".join("".join(line) for line in grid)
        if lines_str in seen:
            cycle_length = s - seen[lines_str]
            to_go = (1000000000 - s - 1) % cycle_length
            for _ in range(to_go):
                grid = step(grid)
            break
        seen[lines_str] = s

    return p1res, resources(grid)


TEST_DATA = {}
TEST_DATA[
    """\
.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.
""".rstrip()
] = (1147, 0)
