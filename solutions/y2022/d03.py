import string

from more_itertools import chunked, divide
from solutions.utils import logger
from aocd import data


def priority(group):
    group = list(map(set, group))
    item = group.pop().intersection(*group).pop()
    return string.ascii_letters.index(item) + 1


def compute(groups):
    return sum(map(priority, groups))


def part1(input):
    return compute([divide(2, line) for line in input])


def part2(input):
    return compute(chunked(input, 3))


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (8139, 2668)
TEST_RESULT = (157, 70)
TEST_DATA = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
