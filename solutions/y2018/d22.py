from functools import cache

from solutions.utils.graph import dijkstra, neighbors4


def parse(data):
    depth, target = data.splitlines()
    depth = int(depth.split(": ")[1])
    target = tuple(map(int, target.split(": ")[1].split(",")))
    return depth, target


@cache
def erosion_level(x, y, depth, target):
    return (geologic_index(x, y, depth, target) + depth) % 20183


@cache
def geologic_index(x, y, depth, target):
    if (x, y) == target:
        return 0
    if x == 0:
        return y * 48271
    if y == 0:
        return x * 16807
    return erosion_level(x - 1, y, depth, target) * erosion_level(
        x, y - 1, depth, target
    )


def region_type(x, y, depth, target):
    return erosion_level(x, y, depth, target) % 3


def part1(depth, target):
    return sum(
        region_type(x, y, depth, target)
        for x in range(target[0] + 1)
        for y in range(target[1] + 1)
    )


TOOLS = {"neither", "torch", "climbing gear"}
T = set(range(3))


def next_tool(current_tool, region_type):
    if current_tool != region_type:
        return current_tool
    return next(iter(T - {current_tool, region_type}))


def part2(depth, target):
    start = (0, 0, 1)
    end = (*target, 1)

    def neighbors(p):
        x, y, tool = p
        NS = []
        for nx, ny in neighbors4(x, y, max_i=target[0] + 40, max_j=target[1] + 40):
            if tool != region_type(nx, ny, depth, target):
                NS.append((nx, ny, tool))
        NS.append((x, y, next(iter(T - {tool, region_type(x, y, depth, target)}))))
        return NS

    def cost(a, b):
        return 1 if a[2] == b[2] else 7

    _, cost_so_far = dijkstra(start, neighbors, cost)

    return cost_so_far[end]


TEST_DATA = {}
TEST_DATA[
    """\
depth: 510
target: 10,10
""".rstrip()
] = (114, 45)
