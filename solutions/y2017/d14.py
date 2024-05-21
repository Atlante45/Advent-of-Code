from solutions.utils.graph import neighbors4
from solutions.y2017.d10 import knot_hash


def parse(data):
    return data.strip()


def part1(key):
    res = 0
    for row in range(128):
        hash = knot_hash(f"{key}-{row}")
        res += bin(int(hash, 16)).count("1")
    return res


def part2(key):
    grid = set()
    for row in range(128):
        hash = knot_hash(f"{key}-{row}")
        cells = bin(int(hash, 16))[2:].rjust(128, "0")
        for col, cell in enumerate(cells):
            if cell == "1":
                grid.add((row, col))

    res = 0
    while grid:
        queue = [grid.pop()]
        visited = set(queue)
        while queue:
            i, j = queue.pop()
            for x, y in neighbors4(i, j, 128):
                if (x, y) in grid and (x, y) not in visited:
                    queue.append((x, y))
                    visited.add((x, y))
        grid -= visited
        res += 1

    return res


TEST_DATA = {}
TEST_DATA[
    """\
flqrgnkx
""".rstrip()
] = (8108, 1242)
