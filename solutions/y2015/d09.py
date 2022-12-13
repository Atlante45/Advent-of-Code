from itertools import pairwise, permutations
import re

REGEX = r"^(\w+) to (\w+) = (\d+)$"


def parse(data):
    groups = [re.match(REGEX, line).groups() for line in data.splitlines()]

    locations = set()
    links = {}
    for a, b, d in groups:
        locations.add(a)
        locations.add(b)
        links[(a, b)] = links[(b, a)] = int(d)

    return links, locations


def cost(links, path):
    return sum(links[link] for link in pairwise(path))


def compute(links, locations, func):
    return func(cost(links, perm) for perm in permutations(locations))


def part1(links, locations):
    return compute(links, locations, min)


def part2(links, locations):
    return compute(links, locations, max)


TEST_DATA = {}
TEST_DATA[
    """\
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
""".rstrip()
] = (605, 982)
