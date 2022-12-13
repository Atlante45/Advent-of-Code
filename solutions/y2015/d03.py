from collections import defaultdict


def move(coords, m):
    x, y = coords
    if m == "^":
        y += 1
    elif m == "v":
        y -= 1
    elif m == ">":
        x += 1
    elif m == "<":
        x -= 1
    return x, y


def parse(data):
    return data.splitlines()


def part1(input):
    visits = defaultdict(int)
    coords = (0, 0)
    visits[coords] = 1
    for m in input[0].strip():
        coords = move(coords, m)
        visits[coords] += 1

    return len(visits)


def part2(input):
    visits = defaultdict(int)
    coords = [(0, 0), (0, 0)]
    visits[0, 0] = 1
    for i, m in enumerate(input[0].strip()):
        coords[i % 2] = move(coords[i % 2], m)
        visits[coords[i % 2]] += 1

    return len(visits)


TEST_DATA = {}
TEST_DATA[
    """\
^>v<
""".rstrip()
] = (4, 3)
