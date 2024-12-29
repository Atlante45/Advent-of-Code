def parse(data):
    return [group.splitlines() for group in data.split("\n\n")]


def part1(groups):
    return sum(len(set("".join(group))) for group in groups)


def part2(groups):
    return sum(
        len(set.intersection(*[set(person) for person in group])) for group in groups
    )


TEST_DATA = {}
TEST_DATA[
    """\
abc

a
b
c

ab
ac

a
a
a
a

b
""".rstrip()
] = (11, 6)
