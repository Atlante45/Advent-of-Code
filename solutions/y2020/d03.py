from math import prod


def parse(data):
    return data.splitlines()


def count_trees(grid, dx, dy):
    return sum(
        grid[i * dy][(i * dx) % len(grid[0])] == "#" for i in range(len(grid) // dy)
    )


def part1(grid):
    return count_trees(grid, 3, 1)


def part2(grid):
    return prod(
        count_trees(grid, dx, dy) for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    )


TEST_DATA = {}
TEST_DATA[
    """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".rstrip()
] = (7, 336)
