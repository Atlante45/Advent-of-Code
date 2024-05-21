from itertools import combinations


def parse(data):
    return [sorted(map(int, line.split())) for line in data.splitlines()]


def part1(lines):
    return sum(line[-1] - line[0] for line in lines)


def part2(lines):
    def f(line):
        return next(b // a for a, b in combinations(line, 2) if b % a == 0)

    return sum(f(line) for line in lines)


TEST_DATA = {}
TEST_DATA[
    """\
5 1 9 5
7 5 3
2 4 6 8
""".rstrip()
] = (18, None)
TEST_DATA[
    """\
5 9 2 8
9 4 7 3
3 8 6 5
""".rstrip()
] = (None, 9)
