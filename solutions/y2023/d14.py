def cycle(grid):
    width = len(grid[0])
    height = len(grid)

    for j in range(width):
        p = 0
        for i in range(height):
            if grid[i][j] == "#":
                p = i + 1
            elif grid[i][j] == "O":
                grid[i][j] = "."
                grid[p][j] = "O"
                p += 1

    for i in range(height):
        p = 0
        for j in range(width):
            if grid[i][j] == "#":
                p = j + 1
            elif grid[i][j] == "O":
                grid[i][j] = "."
                grid[i][p] = "O"
                p += 1

    for j in range(width):
        p = height - 1
        for i in reversed(range(height)):
            if grid[i][j] == "#":
                p = i - 1
            elif grid[i][j] == "O":
                grid[i][j] = "."
                grid[p][j] = "O"
                p -= 1

    for i in range(height):
        p = width - 1
        for j in reversed(range(width)):
            if grid[i][j] == "#":
                p = j - 1
            elif grid[i][j] == "O":
                grid[i][j] = "."
                grid[i][p] = "O"
                p -= 1


def serialize(grid):
    return "".join("".join(line) for line in grid)


def weight(grid):
    height = len(grid)
    return sum(height - i for i in range(height) for c in grid[i] if c == "O")


def parse(data):
    return [list(line) for line in data.splitlines()]


def part1(grid):
    width = len(grid[0])
    height = len(grid)

    for j in range(width):
        p = 0
        for i in range(height):
            if grid[i][j] == "#":
                p = i + 1
            elif grid[i][j] == "O":
                grid[i][j] = "."
                grid[p][j] = "O"
                p += 1

    return weight(grid)


def part2(grid):
    CYCLES = 1000000000

    states = {}
    states[serialize(grid)] = 0

    for i in range(CYCLES):
        cycle(grid)
        sg = serialize(grid)
        if sg in states:
            cycle_len = i + 1 - states[sg]
            cycles_needed = (CYCLES - i - 1) % cycle_len
            for _ in range(cycles_needed):
                cycle(grid)
            return weight(grid)

        states[sg] = i + 1


TEST_DATA = {}
TEST_DATA[
    """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".rstrip()
] = (136, 64)
