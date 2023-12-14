def parse(data):
    return [list(line) for line in data.splitlines()]


def part1(grid):
    grid = zip(*grid)

    sum = 0
    for i, line in enumerate(grid):
        s = 0
        weight = 0
        for j, c in enumerate(line):
            if c == "O":
                weight += len(line) - s
                s += 1
            if c == "#":
                s = j + 1
        sum += weight

    return sum


def cycle(grid):
    width = len(grid[0])
    height = len(grid)

    # print("\n".join("".join(line) for line in grid))
    # print()
    for j in range(width):
        p = 0
        for i in range(height):
            if grid[i][j] == "#":
                p = i + 1
            elif grid[i][j] == "O":
                grid[i][j] = "."
                grid[p][j] = "O"
                p += 1

    # print("\n".join("".join(line) for line in grid))
    # print()
    for i in range(height):
        p = 0
        for j in range(width):
            if grid[i][j] == "#":
                p = j + 1
            elif grid[i][j] == "O":
                grid[i][j] = "."
                grid[i][p] = "O"
                p += 1

    # print("\n".join("".join(line) for line in grid))
    # print()
    for j in range(width):
        p = height - 1
        for i in reversed(range(height)):
            if grid[i][j] == "#":
                p = i - 1
            elif grid[i][j] == "O":
                grid[i][j] = "."
                grid[p][j] = "O"
                p -= 1

    # print("\n".join("".join(line) for line in grid))
    # print()
    for i in range(height):
        p = width - 1
        for j in reversed(range(width)):
            if grid[i][j] == "#":
                p = j - 1
            elif grid[i][j] == "O":
                grid[i][j] = "."
                grid[i][p] = "O"
                p -= 1

    # print("\n".join("".join(line) for line in grid))
    # print()


def serialize(grid):
    return "".join("".join(line) for line in grid)


def weight(grid):
    sum = 0
    width = len(grid[0])
    height = len(grid)

    for j in range(width):
        for i in range(height):
            if grid[i][j] == "O":
                sum += len(grid) - i
    return sum


def part2(grid):
    CYCLES = 1000000000
    states = {}
    states[serialize(grid)] = 0

    for i in range(CYCLES):
        cycle(grid)
        sg = serialize(grid)
        if sg in states:
            cycle_len = i + 1 - states[sg]
            cycle_needed = (CYCLES - i - 1) % cycle_len
            for _ in range(cycle_needed):
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
