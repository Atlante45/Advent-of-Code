from solutions.utils import logger
from aocd import data


def part1(input):
    res = 0

    cur = 0
    for line in input:
        if line:
            cur += int(line)
        else:
            res = max(res, cur)
            cur = 0

    return res


def part2(input):
    cals = []
    cur = 0
    for line in input:
        if line:
            cur += int(line)
        else:
            cals += [cur]
            cur = 0
    cals += [cur]

    cals = sorted(cals)
    return sum(cals[-3:])


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (72511, 212117)
TEST_RESULT = (24000, 45000)
TEST_DATA = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".strip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
