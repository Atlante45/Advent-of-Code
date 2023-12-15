def check_mirror(pattern, mirror):
    return sum(
        int(pattern[mirror - i - 1][j] != pattern[mirror + i][j])
        for i in range(min(mirror, len(pattern) - mirror))
        for j in range(len(pattern[0]))
    )


def find_mirrors(pattern, offset):
    return [m for m in range(1, len(pattern)) if check_mirror(pattern, m) == offset]


def summarize(pattern, offset):
    zipped = [list(a) for a in zip(*pattern)]
    vert = find_mirrors(pattern, offset)
    horiz = find_mirrors(zipped, offset)
    return 100 * sum(vert) + sum(horiz)


def parse(data):
    return [[list(row) for row in grid.splitlines()] for grid in data.split("\n\n")]


def part1(patterns):
    return sum(summarize(p, 0) for p in patterns)


def part2(patterns):
    return sum(summarize(p, 1) for p in patterns)


TEST_DATA = {}
TEST_DATA[
    """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".rstrip()
] = (405, 400)
