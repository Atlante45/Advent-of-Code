def parse(data):
    pairs = [list(map(int, line.split())) for line in data.splitlines()]
    l1, l2 = zip(*pairs)
    return sorted(list(l1)), sorted(list(l2))


def part1(l1, l2):
    return sum(abs(x - y) for x, y in zip(l1, l2))


def part2(l1, l2):
    return sum(x * l2.count(x) for x in l1)


TEST_DATA = {}
TEST_DATA[
    """\
3   4
4   3
2   5
1   3
3   9
3   3
""".rstrip()
] = (11, 31)
