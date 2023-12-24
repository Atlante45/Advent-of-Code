from itertools import pairwise, permutations

from solutions.utils.graph import dijkstra, neighbors4


def parse(data):
    grid = data.splitlines()
    pois = {
        int(c): (i, j)
        for i, line in enumerate(grid)
        for j, c in enumerate(line)
        if c not in "#."
    }

    def neighbors(p):
        return [x for x in neighbors4(*p, grid) if grid[x[0]][x[1]] != "#"]

    distances = {}
    for loc, pos in pois.items():
        _, cost_so_far = dijkstra(pos, neighbors)
        for loc2, pos2 in pois.items():
            if loc == loc2:
                continue
            distances[loc, loc2] = cost_so_far[pos2]

    return pois.keys() - [0], distances


def path_length(path, distances):
    return sum(distances[i, j] for i, j in pairwise(path))


def part1(pois, distances):
    return min(path_length((0,) + p, distances) for p in permutations(pois))


def part2(pois, distances):
    return min(path_length((0,) + p + (0,), distances) for p in permutations(pois))


TEST_DATA = {}
TEST_DATA[
    """\
###########
#0.1.....2#
#.#######.#
#4.......3#
###########
""".rstrip()
] = (14, None)
