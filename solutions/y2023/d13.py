def check_mirror(pattern, mirror):
    return all(
        pattern[mirror - i - 1] == pattern[mirror + i]
        for i in range(min(mirror, len(pattern) - mirror))
    )


def find_mirrors(pattern):
    return [m for m in range(1, len(pattern)) if check_mirror(pattern, m)]


def summarize(pattern):
    zipped = [list(a) for a in zip(*pattern)]
    vert = find_mirrors(pattern)
    horiz = find_mirrors(zipped)
    return vert, horiz


def score(pattern):
    v, h = summarize(pattern)
    return 100 * sum(v) + sum(h)


def smudge(pattern):
    v, h = summarize(pattern)
    for i, line in enumerate(pattern):
        for j, c in enumerate(line):
            pattern[i][j] = "." if c == "#" else "#"
            rv, rh = summarize(pattern)
            rv = [r for r in rv if r not in v]
            rh = [r for r in rh if r not in h]
            if len(rv) > 0 or len(rh) > 0:
                return 100 * sum(rv) + sum(rh)

            pattern[i][j] = c


def parse(data):
    return [
        [list(line) for line in pattern.splitlines()] for pattern in data.split("\n\n")
    ]


def part1(patterns):
    return sum(score(p) for p in patterns)


def part2(patterns):
    return sum(smudge(pattern) for pattern in patterns)


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
