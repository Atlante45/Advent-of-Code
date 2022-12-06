#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data


def dfs(path, links, canRevis):
    if path[-1] == "end":
        return 1
    if path[-1] == "start" and len(path) > 1:
        return 0

    res = 0

    for n in links[path[-1]]:
        revis = any(c for c in n if c.islower()) and n in path
        if revis and not canRevis:
            continue
        res += dfs(path + [n], links, canRevis and not revis)

    return res


def part1(links):
    return dfs(["start"], links, False)


def part2(links):
    return dfs(["start"], links, True)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    links = {}
    for line in data.splitlines():
        a, b = line.strip().split("-")
        links[a] = links.get(a, []) + [b]
        links[b] = links.get(b, []) + [a]

    ans_1 = part1(links)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(links)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (3369, 85883)
TEST_RESULT = (10, 36)
TEST_DATA = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
