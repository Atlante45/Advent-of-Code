from functools import cache
from itertools import pairwise
import re
from solutions.utils.graph import neighbors4


from collections import defaultdict
from queue import PriorityQueue


def dijkstra(starts, neighbors, cost=None):
    if not isinstance(starts, list):
        starts = [starts]

    frontier = PriorityQueue()
    came_from = defaultdict(list)
    cost_so_far = {}

    for start in starts:
        frontier.put(start, 0)
        cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        for next in neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put(next, new_cost)
                came_from[next] = [current]
            if (
                next in cost_so_far
                and new_cost == cost_so_far[next]
                and current not in came_from[next]
            ):
                came_from[next].append(current)
    return came_from, cost_so_far


def parse(data):
    return data.splitlines()


K1 = (("7", "8", "9"), ("4", "5", "6"), ("1", "2", "3"), (None, "0", "A"))
K2 = ((None, "^", "A"), ("<", "v", ">"))
DIRS = {(0, -1): "<", (1, 0): "v", (0, 1): ">", (-1, 0): "^"}


@cache
def find_move_sequences(K, v1, v2):
    if v1 == v2:
        return [("A",)]

    sx, sy = None, None
    ex, ey = None, None
    for i, row in enumerate(K):
        for j, v in enumerate(row):
            if v == v1:
                sx, sy = i, j
            if v == v2:
                ex, ey = i, j

    def ns(n):
        return [
            (x, y) for x, y in neighbors4(*n, len(K), len(K[0])) if K[x][y] is not None
        ]

    came_from, _ = dijkstra((sx, sy), ns)

    all_paths = [[(ex, ey)]]
    while not all(path[0] == (sx, sy) for path in all_paths):
        new_paths = []
        for path in all_paths:
            head = path[0]
            for f in came_from[head]:
                new_paths.append([f] + path)
        all_paths = new_paths

    res = []
    for path in all_paths:
        rp = [DIRS[x2 - x1, y2 - y1] for (x1, y1), (x2, y2) in pairwise(path)]
        res.append(tuple(rp + ["A"]))
    return res


@cache
def shortest_sequence_length(K, code, depth):
    if depth < 0:
        return len(code)

    final_length = 0
    start = "A"
    for c in code:
        sequences = find_move_sequences(K, start, c)
        min_length = min(shortest_sequence_length(K2, s, depth - 1) for s in sequences)
        final_length += min_length
        start = c

    return final_length


def complexity(code, num_robots):
    numeric_code = int("".join(re.findall(r"\d", code)))
    sequence_length = shortest_sequence_length(K1, code, num_robots)
    return numeric_code * sequence_length


def part1(codes):
    return sum(complexity(code, 2) for code in codes)


def part2(codes):
    return sum(complexity(code, 25) for code in codes)


TEST_DATA = {}
TEST_DATA[
    """\
029A
980A
179A
456A
379A
""".rstrip()
] = (126384, None)
