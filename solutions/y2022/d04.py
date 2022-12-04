from solutions.utils import logger
from aocd import data


def contained(a, b):
    return int(a[0]) <= int(b[0]) and int(b[1]) <= int(a[1])


def overlap(a, b):
    return int(a[0]) <= int(b[0]) and int(b[0]) <= int(a[1])


def part1(input):
    res = 0

    for line in input:
        sections = [section.split("-") for section in line.split(",")]
        if contained(sections[0], sections[1]) or contained(sections[1], sections[0]):
            res += 1

    return res


def part2(input):
    res = 0

    for line in input:
        sections = [section.split("-") for section in line.split(",")]
        if overlap(sections[0], sections[1]) or overlap(sections[1], sections[0]):
            res += 1

    return res


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (466, 865)
TEST_RESULT = (2, 4)
TEST_DATA = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
