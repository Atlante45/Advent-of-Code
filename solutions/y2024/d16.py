from collections import defaultdict
from queue import PriorityQueue


def dijkstra(starts, neighbors, cost=None):
    if not isinstance(starts, list):
        starts = [starts]
    if cost is None:
        cost = lambda c, n: 1

    frontier = PriorityQueue()
    came_from = defaultdict(list)
    cost_so_far = {}

    for start in starts:
        frontier.put(start, 0)
        cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        for next in neighbors(current):
            new_cost = cost_so_far[current] + cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put(next, new_cost)
                came_from[next] = [current]
            if next in cost_so_far and new_cost == cost_so_far[next]:
                came_from[next].append(current)
    return came_from, cost_so_far


def parse(data):
    maze = data.splitlines()
    start = None
    end = None
    for i, row in enumerate(maze):
        for j, c in enumerate(row):
            if c == "S":
                start = (i, j)
            elif c == "E":
                end = (i, j)
    return maze, start, end


D = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def parts(maze, start, end):
    i, j = start

    def neighbors(pos):
        i, j, dir = pos
        ns = [(i, j, (dir + 1) % 4), (i, j, (dir + 3) % 4)]

        ni, nj = i + D[dir][0], j + D[dir][1]
        if maze[ni][nj] != "#":
            ns.append((ni, nj, dir))
        return ns

    def cost(pos, next):
        return 1 if pos[2] == next[2] else 1000

    came_from, cost_so_far = dijkstra((i, j, 0), neighbors, cost)
    p1 = min(cost_so_far[(end[0], end[1], i)] for i in range(4))

    p1 = float("inf")
    end_positions = []
    for (i, j, dir), c in cost_so_far.items():
        if (i, j) != end:
            continue

        if c < p1:
            p1 = c
            end_positions = [(i, j, dir)]
        elif c == p1:
            end_positions.append((i, j, dir))

    seats = set([end])
    while len(end_positions) > 0:
        i, j, dir = end_positions.pop()
        for ci, cj, cdir in came_from[(i, j, dir)]:
            seats.add((ci, cj))
            if (ci, cj, cdir) not in end_positions:
                end_positions.append((ci, cj, cdir))

    return p1, len(seats)


TEST_DATA = {}
TEST_DATA[
    """\
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""".rstrip()
] = (7036, 45)
