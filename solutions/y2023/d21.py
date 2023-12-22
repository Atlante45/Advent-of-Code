from solutions.utils.graph import neighbors4


def count_plots(grid, start, target):
    positions = set()
    positions.add(start)
    for _ in range(target):
        new_positions = set()
        for pos in positions:
            for n in neighbors4(pos[0], pos[1], grid):
                if grid[n[0]][n[1]] != "#":
                    new_positions.add(n)
        positions = new_positions
    return len(positions)


def parse(data):
    grid = data.splitlines()
    start = None
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)
                break
    return grid, start


def part1(grid, start):
    target = 6 if len(grid) < 15 else 64
    return count_plots(grid, start, target)


def part2(grid, start):
    factor = 202300
    res = 0

    #  Full plots
    f = 2 * factor // 2
    odds = (f - 1) ** 2
    evens = f**2
    res += odds * count_plots(grid, start, 131)
    res += evens * count_plots(grid, start, 132)

    # Pointy plots
    steps = 131 - 1
    res += count_plots(grid, (0, start[1]), steps)
    res += count_plots(grid, (start[0], 0), steps)
    res += count_plots(grid, (len(grid) - 1, start[1]), steps)
    res += count_plots(grid, (start[0], len(grid[0]) - 1), steps)

    # Edge plot starts
    starts = [
        (0, 0),
        (0, len(grid[0]) - 1),
        (len(grid) - 1, 0),
        (len(grid) - 1, len(grid[0]) - 1),
    ]

    # Big edge plots
    big_edges = factor - 1
    steps = 2 * 131 - 65 - 2
    res += sum(big_edges * count_plots(grid, start, steps) for start in starts)

    # Small edge plots
    small_edges = factor
    steps = 131 - 65 - 2
    res += sum(small_edges * count_plots(grid, start, steps) for start in starts)

    return res


TEST_DATA = {}
TEST_DATA[
    """\
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
""".rstrip()
] = (16, None)
