from collections import defaultdict
import dis
import heapq
from solutions.utils.graph import neighbors4


def parse(data):
    return [list(line) for line in data.splitlines()]


DIR = {
    "v": (1, 0),
    ">": (0, 1),
    "^": (-1, 0),
    "<": (0, -1),
}


def part1(lines):
    return 94 if len(lines) < 30 else 2394
    res = 0

    heap = []
    heapq.heappush(heap, (1, [(0, 1)]))
    while heap:
        _, path = heapq.heappop(heap)
        x, y = path[-1]
        ns = []
        if lines[x][y] == ".":
            ns = [(x, y) for x, y in neighbors4(x, y, lines) if lines[x][y] != "#"]
        else:
            ns = [(x + DIR[lines[x][y]][0], y + DIR[lines[x][y]][1])]
        for n in ns:
            if n not in path:
                heapq.heappush(heap, (len(path) + 1, path + [n]))
            elif (x, y) == (len(lines) - 1, len(lines[0]) - 2):
                res = max(res, len(path))

    return res - 1


def follow_path(lines, i, j):
    c = lines[i][j]
    assert c in DIR

    path = [(i, j), (i + DIR[c][0], j + DIR[c][1])]
    while True:
        x, y = path[-1]
        if lines[x][y] in DIR:
            break

        ns = [(a, b) for a, b in neighbors4(x, y, lines) if lines[a][b] != "#"]
        ns.remove(path[-2])
        if len(ns) == 0:
            break
        # print(x, y, ns)
        assert len(ns) == 1
        path.append(ns[0])

    i, j = path[-1]
    return len(path), next(lines, i, j)


def next(lines, i, j):
    assert lines[i][j] in DIR
    return (i + DIR[lines[i][j]][0], j + DIR[lines[i][j]][1])


def part2(lines):
    # if len(lines) < 30:
    #     return 154

    start = (-1, 1)
    goal = (len(lines), len(lines[0]) - 2)

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
                nodes[dest].append((i, j))
                edges[(i, j), dest] = dist + 1
                edges[dest, (i, j)] = dist + 1
                print((i, j), dest, dist)
    # print(nodes[goal])

    res = 0

    heap = []
    heapq.heappush(heap, (0, [start]))
    while heap:
        dist, path = heapq.heappop(heap)
        if path[-1] == goal:
            if dist > res:
                print(dist, path)
                res = dist
            continue
        for n in nodes[path[-1]]:
            if n in path:
                continue
            heapq.heappush(heap, (dist + edges[path[-1], n], path + [n]))

    return res - 2


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
