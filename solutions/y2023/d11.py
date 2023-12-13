from itertools import combinations


def distance(start, end, empty, factor):
    visited = set(range(start, end, 1 if start < end else -1))
    return abs(end - start) + (factor - 1) * len(visited & empty)


def solve(galaxies, empty_rows, empty_cols, factor):
    return sum(
        distance(ai, bi, empty_rows, factor) + distance(aj, bj, empty_cols, factor)
        for (ai, aj), (bi, bj) in combinations(galaxies, 2)
    )


def parse(data):
    grid = data.splitlines()
    galaxies = set()
    empty_rows = set(range(len(grid)))
    empty_cols = set(range(len(grid[0])))
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "#":
                galaxies.add((i, j))
                if i in empty_rows:
                    empty_rows.remove(i)
                if j in empty_cols:
                    empty_cols.remove(j)
    return galaxies, empty_rows, empty_cols


def part1(galaxies, empty_rows, empty_cols):
    return solve(galaxies, empty_rows, empty_cols, 2)


def part2(galaxies, empty_rows, empty_cols):
    return solve(galaxies, empty_rows, empty_cols, 1000000)


TEST_DATA = {}
TEST_DATA[
    """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".rstrip()
] = (374, 82000210)
