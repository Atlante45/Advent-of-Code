def parse(data):
    return [int(x) for x in data.split(",")]


def part1(starting):
    last = {}
    age = None
    for i, n in enumerate(starting):
        age = last.get(n, None)
        last[n] = i

    for i in range(i + 1, 2020):
        n = 0 if age is None else i - age - 1
        age = last.get(n, None)
        last[n] = i

    return n


def part2(starting):
    last = {}
    age = None
    for i, n in enumerate(starting):
        age = last.get(n, None)
        last[n] = i

    for i in range(i + 1, 30000000):
        n = 0 if age is None else i - age - 1
        age = last.get(n, None)
        last[n] = i

    return n


TEST_DATA = {}
TEST_DATA[
    """\
3,1,2
""".rstrip()
] = (1836, 362)
