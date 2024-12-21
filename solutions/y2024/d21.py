from functools import cache
from itertools import pairwise
from collections import defaultdict

from solutions.utils.graph import dijkstra_full, neighbors4


K1 = (("7", "8", "9"), ("4", "5", "6"), ("1", "2", "3"), (None, "0", "A"))
K2 = ((None, "^", "A"), ("<", "v", ">"))
DIRS = {(0, -1): "<", (1, 0): "v", (0, 1): ">", (-1, 0): "^"}


def map_grid(K):
    neighbors = defaultdict(list)
    directions = {}
    for i, row in enumerate(K):
        for j, v in enumerate(row):
            if v is None:
                continue

            for x, y in neighbors4(i, j, len(K), len(K[0])):
                if K[x][y] is not None:
                    neighbors[v].append(K[x][y])
                    directions[v, K[x][y]] = DIRS[x - i, y - j]

    return neighbors, directions


NEIGHBORS1, DIRECTIONS1 = map_grid(K1)
NEIGHBORS2, DIRECTIONS2 = map_grid(K2)


def parse(data):
    return data.splitlines()


@cache
def find_move_sequences(K, from_key, pressed_key):
    if from_key == pressed_key:
        return [("A",)]

    if K == K1:
        NEIGHBORS = NEIGHBORS1
        DIRECTIONS = DIRECTIONS1
    else:
        NEIGHBORS = NEIGHBORS2
        DIRECTIONS = DIRECTIONS2

    came_from, _ = dijkstra_full(from_key, lambda n: NEIGHBORS[n])

    all_paths = [[pressed_key]]
    while not all(path[0] == from_key for path in all_paths):
        new_paths = []
        for path in all_paths:
            new_paths.extend([[f] + path for f in came_from[path[0]]])
        all_paths = new_paths

    return [
        tuple([DIRECTIONS[a, b] for a, b in pairwise(path)] + ["A"])
        for path in all_paths
    ]


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
    numeric_code = int(code[:-1])
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
