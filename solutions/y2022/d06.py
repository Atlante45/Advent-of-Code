from solutions.utils import logger
from aocd import data


def find_start(data, n):
    return next(i + n for i in range(len(data) - n) if len(set(data[i : i + n])) == n)


def part1(data):
    return find_start(data, 4)


def part2(data):
    return find_start(data, 14)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.strip()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (1723, 3708)
TEST_RESULT = (11, 26)
TEST_DATA = """\
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
