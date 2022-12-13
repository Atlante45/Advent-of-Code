from solutions.utils.graph import dijkstra, neighbors4


def parse(data):
    start = end = None

    heightmap = []
    for r, line in enumerate(data.splitlines()):
        row = []
        for c, p in enumerate(line):
            match p:
                case "S":
                    row.append(0)
                    start = (r, c)
                case "E":
                    row.append(25)
                    end = (r, c)
                case _:
                    row.append(ord(p) - ord("a"))
        heightmap.append(row)
    return start, end, heightmap


def part1(start, end, heightmap):
    def neighbors(n):
        i, j = n
        return [
            (x, y)
            for (x, y) in neighbors4(i, j, heightmap)
            if heightmap[x][y] <= heightmap[i][j] + 1
        ]

    _, cost_so_far = dijkstra(start, neighbors)
    return cost_so_far[end]


def part2(_, end, heightmap):
    def neighbors(n):
        i, j = n
        return [
            (x, y)
            for (x, y) in neighbors4(i, j, heightmap)
            if heightmap[x][y] <= heightmap[i][j] + 1
        ]

    starts = []
    for i, r in enumerate(heightmap):
        for j, c in enumerate(r):
            if heightmap[i][j] == 0:
                starts.append((i, j))

    _, cost_so_far = dijkstra(starts, neighbors)
    return cost_so_far[end]


TEST_DATA = {}
TEST_DATA[
    """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".rstrip()
] = (31, 29)
