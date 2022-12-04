from solutions.utils import logger
from aocd import data

from collections import defaultdict
import math


def step(template, pairs):
    res = ""
    for i in range(len(template) - 1):
        pair = template[i : i + 2]
        res += template[i]
        res += pairs[pair]
    res += template[-1]

    return res


def part1(template, pairs):
    for _ in range(10):
        template = step(template, pairs)

    counts = [template.count(i) for i in set(template)]
    return max(counts) - min(counts)


def step2(template, pairs):
    current = defaultdict(int)

    for p in template:
        current[p[0] + pairs[p]] += template[p]
        current[pairs[p] + p[1]] += template[p]

    return current


def part2(template, pairs):
    current = defaultdict(int)
    for i in range(len(template) - 1):
        current[template[i : i + 2]] += 1

    for _ in range(40):
        current = step2(current, pairs)

    counts = defaultdict(int)
    for p in current:
        counts[p[0]] += current[p]
        counts[p[1]] += current[p]

    least = math.ceil(min(counts.values()) / 2)
    most = math.ceil(max(counts.values()) / 2)

    return most - least


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    template = data.splitlines()[0].strip()

    pairs = {}
    for line in data.splitlines()[2:]:
        (p, i) = line.split(" -> ")
        pairs[p] = i

    ans_1 = part1(template, pairs)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(template, pairs)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (2768, 2914365137499)
TEST_RESULT = (1588, 2188189693529)
TEST_DATA = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
