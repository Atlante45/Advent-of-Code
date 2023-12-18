from itertools import cycle
from more_itertools import spy


SHAPES = [
    ["####"],
    [".#.", "###", ".#."],
    ["###", "..#", "..#"],
    ["#", "#", "#", "#"],
    ["##", "##"],
]


def shift_rock(rock, x, move):
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


def drop_rock(chamber, rock, moves):
    x = 2
    for _ in range(3):
        x = shift_rock(rock, x, next(moves))

    y = len(chamber)
    while True:
        move = next(moves)
        new_x = shift_rock(rock, x, move)
        if not collides(chamber, rock, new_x, y):
            x = new_x

        new_y = y - 1
        if collides(chamber, rock, x, new_y):
            land(chamber, rock, x, y)
            return x, y

        y = new_y


def compute(pattern, count):
    moves = cycle(enumerate(pattern))
    shapes = cycle(enumerate(SHAPES))

    chamber = []
    repeats = {}

    rock_cycle = 0
    cur_cycle = 0
    added_height = 0

    rock_index = 0
    while rock_index < count:
        shape_id, shape = next(shapes)
        x, _ = drop_rock(chamber, shape, moves)

        if added_height == 0:
            [(move_id, _)], moves = spy(moves)
            key = (shape_id, move_id, x)
            if key in repeats:
                rock_cycle = max(0, rock_index - repeats[key][0])
                cur_cycle += 1

                if cur_cycle == rock_cycle:
                    n = (count - rock_index) // rock_cycle
                    added_height = n * (len(chamber) - repeats[key][1])
                    rock_index += n * rock_cycle
            else:
                cur_cycle = 0
            repeats[key] = (rock_index, len(chamber))
        rock_index += 1

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
