from more_itertools import pairwise


SOURCE = (500, 0)


def draw(slice, min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 4):
        for x in range(min_x - 5, max_x + 7):
            if (x, y) == (500, 0):
                print("+", end="")
            elif (x, y) in slice:
                print(slice[(x, y)], end="")
            else:
                print(".", end="")
        print()


def range_coords(a, b):
    ax, ay = a
    bx, by = b
    if ax == bx:
        sign = 1 if by > ay else -1
        for y in range(ay, by + sign, sign):
            yield ax, y
    else:
        sign = 1 if bx > ax else -1
        for x in range(ax, bx + sign, sign):
            yield x, ay


def add_sand(slice, max_y, floor=False):
    if SOURCE in slice:
        return False

    x = SOURCE[0]
    for y in range(SOURCE[1], max_y):
        if (x, y + 1) not in slice:
            continue

        if (x - 1, y + 1) not in slice:
            x = x - 1
            continue

        if (x + 1, y + 1) not in slice:
            x = x + 1
            continue

        slice[(x, y)] = "o"
        return True

    if floor:
        slice[(x, y)] = "o"
        return True

    return False


def simulate(slice, max_y, floor):
    res = 0
    while add_sand(slice, max_y + (2 if floor else 0), floor):
        res += 1
    return res


def parse(data):
    min_x = max_x = 500
    min_y = max_y = 0
    slice = {}

    for line in data.splitlines():
        segments = []
        for coords in line.split(" -> "):
            x, y = map(int, coords.split(","))
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            segments += [(x, y)]

        for a, b in pairwise(segments):
            for x, y in range_coords(a, b):
                slice[(x, y)] = "#"

    print(min_x, max_x, min_y, max_y)

    return slice, min_x, max_x, min_y, max_y


def part1(slice, min_x, max_x, min_y, max_y):
    return simulate(slice, max_y, False)


def part2(slice, min_x, max_x, min_y, max_y):
    return simulate(slice, max_y, True)


TEST_DATA = {}
TEST_DATA[
    """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".rstrip()
] = (24, 93)
