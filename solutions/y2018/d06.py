from collections import defaultdict


def parse(data):
    lines = data.splitlines()
    coords = [tuple(map(int, line.split(", "))) for line in lines]
    min_x = min(x for x, _ in coords)
    max_x = max(x for x, _ in coords)
    min_y = min(y for _, y in coords)
    max_y = max(y for _, y in coords)
    return coords, min_x, min_y, max_x, max_y


def part1(coords, min_x, min_y, max_x, max_y):
    areas = defaultdict(int)
    infinite = set()
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            min_dist = float("inf")
            min_coord = None
            for coord in coords:
                dist = abs(coord[0] - i) + abs(coord[1] - j)
                if dist < min_dist:
                    min_dist = dist
                    min_coord = coord
                elif dist == min_dist:
                    min_coord = None
            if min_coord:
                areas[min_coord] += 1
            if i == min_x or i == max_x or j == min_y or j == max_y:
                infinite.add(min_coord)
    return max(areas[coord] for coord in coords if coord not in infinite)


def part2(coords, min_x, min_y, max_x, max_y):
    res = 0
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if sum(abs(coord[0] - i) + abs(coord[1] - j) for coord in coords) < 10000:
                res += 1
    return res


TEST_DATA = {}
TEST_DATA[
    """\
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
""".rstrip()
] = (17, None)
