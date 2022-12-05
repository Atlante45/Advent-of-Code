from solutions.utils import logger
from aocd import data


def score1(adv, me):
    if (adv + 1) % 3 == me:
        return 6 + me + 1
    elif adv == me:
        return 3 + me + 1
    else:
        return 0 + me + 1


def score2(adv, end):
    if end == 0:
        return 0 + 1 + (adv + 2) % 3
    elif end == 1:
        return 3 + 1 + adv
    else:
        return 6 + 1 + (adv + 1) % 3


def compute(input, func):
    return sum([func(*game) for game in input])


def part1(input):
    return compute(input, score1)


def part2(input):
    return compute(input, score2)


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
TEST_DATA = """\
A Y
B X
C Z
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
