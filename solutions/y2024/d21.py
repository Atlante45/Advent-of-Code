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
def move(K, v1, v2):
    if v1 == v2:
        return [["A"]]

    sx, sy = None, None
    ex, ey = None, None
    for i, row in enumerate(K):
        for j, v in enumerate(row):
            if v == v1:
                sx, sy = i, j
            elif v == v2:
                ex, ey = i, j

    if sx is None or ex is None:
        raise ValueError(f"No start or end for {v1} -> {v2}")

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
            # print(head, came_from[head])
            for f in came_from[head]:
                new_paths.append([f] + path)
        all_paths = new_paths

    res = []
    for path in all_paths:
        rp = []
        for (x1, y1), (x2, y2) in pairwise(path):
            dx, dy = x2 - x1, y2 - y1
            d = DIRS[(dx, dy)]
            rp.append(d)
        res.append(rp + ["A"])
    # print("Dijkstra", v1, v2, res)
    return res


@cache
def move_code(K, code, depth):
    best_moves = 0
    start = "A"

    for c in code:
        moves = move(K, start, c)
        # print("Moves", moves)

        best = float("inf")
        best_move = None
        for m in moves:
            # print(depth, m)
            if depth > 0:
                m = move_code(K2, tuple(m), depth - 1)
            else:
                m = len(m)
            # print(depth, m)
            if m < best:
                best = m
                best_move = m

        if best_move is None:
            raise ValueError(f"No moves for {start} -> {c}")

        # print("Best move", best_move)
        best_moves += best_move
        start = c
    return best_moves


def part1(codes):
    sum = 0
    for code in codes:
        # print("Solving", code)
        moves = move_code(K1, code, 2)
        # print("Final moves:", moves)

        c = int("".join(re.findall("\d", code)))
        # print(len(moves), c, len(moves) * c)
        sum += moves * c
    return sum


def part2(codes):
    sum = 0
    for code in codes:
        print("Solving", code)
        moves = move_code(K1, code, 25)
        # print("Final moves:", moves)

        c = int("".join(re.findall("\d", code)))
        print(moves, c, moves * c)
        sum += moves * c
    return sum


TEST_DATA = {}
TEST_DATA[
    """\
029A
""".rstrip()
] = (68 * 29, None)
# TEST_DATA[
#     """\
# 980A
# """.rstrip()
# ] = (60 * 980, None)

# TEST_DATA[
#     """\
# 379A
# """.rstrip()
# ] = (64 * 379, None)

# TEST_DATA[
#     """\
# 179A
# """.rstrip()
# ] = (68 * 179, None)
# TEST_DATA[
#     """\
# 456A
# """.rstrip()
# ] = (64 * 456, None)
# TEST_DATA[
#     """\
# 029A
# 980A
# 179A
# 456A
# 379A
# """.rstrip()
# ] = (126384, None)
