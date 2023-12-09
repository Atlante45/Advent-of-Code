from more_itertools import pairwise


def parse(data):
    return [list(map(int, line.split())) for line in data.splitlines()]


def extrapolate(values):
    all_values = [values]
    while not all(v == 0 for v in values):
        values = [b - a for a, b in pairwise(values)]
        all_values += [values]
    return all_values


def part1(lines):
    return sum(sum(a[-1] for a in extrapolate(line)) for line in lines)


def part2(lines):
    return sum(
        sum(pow(-1, i) * a[0] for i, a in enumerate(extrapolate(line)))
        for line in lines
    )


TEST_DATA = {}
TEST_DATA[
    """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".rstrip()
] = (114, 2)
