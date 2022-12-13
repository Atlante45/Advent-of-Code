import string
from more_itertools import chunked, divide


def priority(group):
    group = list(map(set, group))
    item = group.pop().intersection(*group).pop()
    return string.ascii_letters.index(item) + 1


def compute(groups):
    return sum(map(priority, groups))


def parse(data):
    return data.splitlines()


def part1(input):
    return compute([divide(2, line) for line in input])


def part2(input):
    return compute(chunked(input, 3))


TEST_DATA = {}
TEST_DATA[
    """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()
] = (157, 70)
