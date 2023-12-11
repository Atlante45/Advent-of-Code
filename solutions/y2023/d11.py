from itertools import combinations


def distance(start, end, empty_list, factor):
        si = min(start, end)
        ei = max(start, end)
        empty_count = len(set(range(si, ei)).intersection(empty_list)) 
        return (ei - si) + (factor - 1) * empty_count

def solve(galaxies, empty_rows, empty_cols, factor):
    return sum(distance(ai, bi, empty_rows, factor) + distance(aj, bj, empty_cols, factor) for (ai, aj), (bi, bj) in combinations(galaxies, 2))


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
] = (374, None)
