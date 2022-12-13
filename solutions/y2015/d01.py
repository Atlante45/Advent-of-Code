def parse(data):
    return data.strip()


def part1(input):
    return sum([1 if c == "(" else -1 for c in input])


def part2(input):
    floor = 0
    for i, c in enumerate(input):
        floor += 1 if c == "(" else -1
        if floor == -1:
            return i + 1


TEST_DATA = {}
TEST_DATA[
    """\
()())
""".rstrip()
] = (-1, 5)
