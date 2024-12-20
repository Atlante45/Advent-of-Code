from solutions.utils.graph import dijkstra, neighbors4


def parse(data):
    start = None
    end = None
    walls = set()

    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)
            elif c == "#":
                walls.add((x, y))

    return walls, start, end


def parts(walls, start, end):
    def neighbors(n):
        return [x for x in neighbors4(*n, 100000000) if x not in walls]

    came_from, _ = dijkstra(start, neighbors)

    path = []
    while end != start:
        path.append(end)
        end = came_from[end]
    path.append(start)

    sum1 = 0
    sum2 = 0
    for i in range(len(path)):
        for j in range(i + 102, len(path)):
            dist = abs(path[j][0] - path[i][0]) + abs(path[j][1] - path[i][1])
            if (j - i) - dist < 100:
                continue

            if dist == 2:
                sum1 += 1
            if dist <= 20:
                sum2 += 1

    return sum1, sum2


TEST_DATA = {}
TEST_DATA[
    """\
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".rstrip()
] = (None, None)
