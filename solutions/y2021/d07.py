from solutions.utils import logger
from aocd import data


def computeCost(pos, fuelCost):
    minCost = None
    for i in range(min(pos), max(pos) + 1):
        cost = sum([fuelCost(abs(i - n)) for n in pos])
        if minCost and cost > minCost:
            return minCost
        minCost = cost


def part1(pos):
    return computeCost(pos, lambda n: n)


def part2(pos):
    return computeCost(pos, lambda n: int((n * (n + 1)) / 2))


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()
    pos = [int(v) for v in data[0].split(",")]

    ans_1 = part1(pos)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(pos)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (348664, 100220525)
TEST_RESULT = (37, 168)
TEST_DATA = """\
16,1,2,0,4,2,7,1,2,14
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
