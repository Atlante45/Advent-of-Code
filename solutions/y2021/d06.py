from solutions.utils import logger
from aocd import data


def count(input, gens):
    ageCounts = [0] * 9
    for i in range(9):
        ageCounts[i] = input.count(i)

    for _ in range(gens):
        replicatingFish = ageCounts.pop(0)
        ageCounts[6] += replicatingFish
        ageCounts.append(replicatingFish)

    return sum(ageCounts)


def part1(ages):
    return count(ages, 80)


def part2(ages):
    return count(ages, 256)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()
    ages = [int(v) for v in data[0].split(",")]

    ans_1 = part1(ages)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(ages)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (390011, 1746710169834)
TEST_RESULT = (5934, 26984457539)
TEST_DATA = """\
3,4,3,1,2
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
