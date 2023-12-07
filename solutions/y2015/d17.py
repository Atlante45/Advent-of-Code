from more_itertools import powerset


def parse(data):
    return list(map(int, data.splitlines()))


def part1(values):
    return sum(sum(v) == 150 for v in powerset(values))


def part2(values):
    sizes = [len(v) for v in powerset(values) if sum(v) == 150]
    return sizes.count(min(sizes))


TEST_DATA = {}
TEST_DATA[
    """\

""".rstrip()
] = (None, None)
