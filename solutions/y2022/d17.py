from itertools import cycle

from more_itertools import spy

from solutions.y2021.d19 import add


SHAPES = [
    ["####"],
    [".#.", "###", ".#."],
    ["###", "..#", "..#"],
    ["#", "#", "#", "#"],
    ["##", "##"],
]


def shift_rock(rock, x, move):
    # print("shift", move)
    if move[1] == "<":
        return max(0, x - 1)
    else:
        return min(x + 1, 7 - len(rock[0]))


def collides(chamber, rock, x, y):
    if y < 0:
        return True

    for i, l in enumerate(rock):
        if y + i >= len(chamber):
            return False
        for j, c in enumerate(l):
            if c == "#" and chamber[y + i][x + j] == "#":
                return True

    return False


def land(chamber, rock, x, y):
    for i, l in enumerate(rock):
        if y + i >= len(chamber):
            chamber += [list(".......")]
        for j, c in enumerate(l):
            if c == "#":
                chamber[y + i][x + j] = "#"


def print_chamber(chamber):
    for l in reversed(chamber):
        print("".join(l))


def drop_rock(chamber, rock, pattern):
    x = 2

    for i in range(3):
        x = shift_rock(rock, x, next(pattern))

    y = len(chamber)
    while True:
        move = next(pattern)
        new_x = shift_rock(rock, x, move)
        if not collides(chamber, rock, new_x, y):
            x = new_x

        new_y = y - 1
        if collides(chamber, rock, x, new_y):
            land(chamber, rock, x, y)
            return x, y

        y = new_y


def compute(pattern, count):
    pattern = cycle(enumerate(pattern))
    chamber = []

    repeats = {}

    rock_cycle = None
    height_cycle = None

    r = 0
    added_height = 0
    while r < count:
        # print(r, count)
        rock_id = r % len(SHAPES)
        rock = SHAPES[rock_id]
        x, y = drop_rock(chamber, rock, pattern)

        move, pattern = spy(pattern)
        key = (rock_id, move[0], x)
        if key in repeats:
            rock_cycle = r - repeats[key][0]
            height_cycle = len(chamber) - repeats[key][1]
            n = (count - r) // rock_cycle

            if added_height == 0:
                added_height = n * height_cycle
                r += n * rock_cycle
            # print(rock_cycle, height_cycle, n, added_height, n * rock_cycle)

        repeats[key] = (r, len(chamber))
        r += 1

    return len(chamber) + added_height


def parse(data):
    return data.strip()


def part1(pattern):
    return compute(pattern, 2022)


def part2(pattern):
    return compute(pattern, 1_000_000_000_000)


TEST_DATA = {}
TEST_DATA[
    """\
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
""".rstrip()
] = (3068, 1514285714288)
