from solutions.utils import logger
from aocd import data

from collections import deque


def part1(input):
    res = 0
    last = int(input[0])

    for line in input:
        cur = int(line)

        if cur > last:
            res += 1

        last = cur

    return res


def part2(input):
    res = 0
    vals = deque([])

    for line in input:
        cur = int(line)

        if len(vals) == 3 and cur > vals.popleft():
            res += 1

        vals.append(cur)

    return res


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (1713, 1734)
TEST_RESULT = (7, 5)
TEST_DATA = """\
199
200
208
210
200
207
240
269
260
263
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
