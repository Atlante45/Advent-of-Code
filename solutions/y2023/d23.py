from collections import defaultdict
from solutions.utils.graph import neighbors4


def parse(data):
    return [list(line) for line in data.splitlines()]


DIR = {
    "v": (1, 0),
    ">": (0, 1),
    "^": (-1, 0),
    "<": (0, -1),
}


def next(lines, i, j):
    return (i + DIR[lines[i][j]][0], j + DIR[lines[i][j]][1])


def follow_path(lines, i, j):
    path = [(i, j), next(lines, i, j)]
    while lines[path[-1][0]][path[-1][1]] not in DIR:
        ns = [(a, b) for a, b in neighbors4(*path[-1], lines) if lines[a][b] != "#"]
        ns.remove(path[-2])
        path.append(ns[0])
    return len(path) + 1, next(lines, *path[-1])


def compute_graph(lines, start):
    lines[0][1] = "v"
    lines[-1][-2] = "v"

    nodes = defaultdict(list)
    edges = dict()

    starts = [start]
    while starts:
        i, j = starts.pop()
        for x, y in neighbors4(i, j, lines):
            if lines[x][y] in DIR and next(lines, x, y) != (i, j):
                dist, dest = follow_path(lines, x, y)

                if dest not in nodes:
                    starts.append(dest)

                nodes[(i, j)].append(dest)
                edges[(i, j), dest] = dist

                nodes[dest].append((i, j))
                edges[dest, (i, j)] = -dist

    return nodes, edges


def parts(lines):
    start = (-1, 1)
    goal = (len(lines), len(lines[0]) - 2)

    nodes, edges = compute_graph(lines, start)

    res = [0, 0]

    def dfs(current, cost, visited, directed):
        if current == goal:
            res[0] = cost if cost > res[0] and directed else res[0]
            res[1] = cost if cost > res[1] else res[1]
            return

        for n in nodes[current]:
            if n not in visited:
                visited.add(n)
                weight = edges[current, n]
                dfs(n, cost + abs(weight), visited, directed and weight > 0)
                visited.remove(n)

    dfs(start, -2, set([start]), True)
    return res


TEST_DATA = {}
TEST_DATA[
    """\
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
""".rstrip()
] = (94, 154)
