import numpy as np
import re

REGEX = r"^\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"


def gen(sum, depth):
    for i in range(sum + 1):
        if depth > 2:
            for j in gen(sum - i, depth - 1):
                yield [i] + j
        else:
            yield [i, sum - i]


def parse_data(data):
    matrix = []
    cals = []
    for line in data:
        vals = list(map(int, re.search(REGEX, line).groups()))
        matrix.append(vals[:-1])
        cals.append(vals[-1])
    matrix = np.rot90(np.array(matrix), axes=(1, 0))
    cals.reverse()

    return matrix, cals


def compute_score(matrix, cals, vec):
    vec = np.array(vec)
    tcal = np.sum(np.matmul(cals, vec))
    vec = np.matmul(matrix, vec)
    if all(map(lambda i: i >= 0, vec)):
        return np.prod(vec), tcal

    return None, None


def parse(data):
    return parse_data(data.splitlines())


def parts(matrix, cals):
    maximum = 0
    maximum_cals = 0
    for vec in gen(100, len(cals)):
        score, tcal = compute_score(matrix, cals, vec)
        if not score:
            continue

        maximum = max(maximum, score)
        if tcal == 500:
            maximum_cals = max(maximum_cals, score)

    return maximum, maximum_cals


TEST_DATA = {}
TEST_DATA[
    """\
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""".rstrip()
] = (62842880, 57600000)
