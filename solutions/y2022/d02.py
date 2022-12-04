from solutions.utils import logger
from aocd import data


def part1(input):
    res = 0

    for (adv, me) in input:
        res += me + 1
        if (adv + 1) % 3 == me:
            res += 6
        elif adv == me:
            res += 3

    return res


def part2(input):
    res = 0

    for (adv, end) in input:
        if end == 0:
            res += 0 + 1 + (adv + 2) % 3
        elif end == 1:
            res += 3 + 1 + adv
        else:
            res += 6 + 1 + (adv + 1) % 3

    return res


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = [
        (ord(line[0]) - ord("A"), ord(line[2]) - ord("X")) for line in data.splitlines()
    ]

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (13675, 14184)
TEST_RESULT = (15, 12)
TEST_DATA = """
A Y
B X
C Z
""".strip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
