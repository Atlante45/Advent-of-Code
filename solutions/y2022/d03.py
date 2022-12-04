from solutions.utils import logger
from aocd import data


def priority(item):
    if item >= "a" and item <= "z":
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27


def part1(input):
    res = 0

    for line in input:
        mid = len(line) // 2
        first = line[:mid]
        second = line[mid:]
        for item in first:
            if item in second:
                res += priority(item)
                break

    return res


def part2(input):
    res = 0

    for i in range(len(input) // 3):
        for c in input[3 * i]:
            if c in input[3 * i + 1] and c in input[3 * i + 2]:
                res += priority(c)
                break

    return res


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
