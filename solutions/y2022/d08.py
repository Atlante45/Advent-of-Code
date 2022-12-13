from itertools import chain, product
from more_itertools import first, split_after
from math import prod


def ranges(trees, a, b):
    def outward(i, n, func):
        return [map(func, reversed(range(i))), map(func, range(i + 1, n))]

    return chain(
        outward(a, len(trees), lambda i: trees[i][b]),
        outward(b, len(trees[a]), lambda j: trees[a][j]),
    )


def is_visible(trees, a, b):
    return any(map(lambda range: max(range) < trees[a][b], ranges(trees, a, b)))


def score(trees, a, b):
    def view_dist(range):
        return len(first(split_after(range, lambda x: x >= trees[a][b])))

    return prod(view_dist(range) for range in ranges(trees, a, b))


def parse(data):
    return data.splitlines()


def part1(data):
    trees = list(list(map(int, list(line))) for line in data)
    indices = product(range(1, len(data) - 1), range(1, len(data[0]) - 1))

    res = 2 * len(trees) + 2 * len(trees[0]) - 4
    res += sum(is_visible(trees, i, j) for i, j in indices)
    return res


def part2(data):
    trees = list(list(map(int, list(line))) for line in data)
    indices = product(range(1, len(data) - 1), range(1, len(data[0]) - 1))
    return max(score(trees, i, j) for i, j in indices)


TEST_DATA = {}
TEST_DATA[
    """\
30373
25512
65332
33549
35390
""".rstrip()
] = (21, 8)
