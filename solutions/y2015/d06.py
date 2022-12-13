from enum import Enum
import itertools
import re

SIZE = 1000


def draw(lights):
    grid = ""
    for i in range(SIZE):
        grid += (
            "".join(["#" if c else "." for c in lights[i * SIZE : (i + 1) * SIZE]])
            + "\n"
        )
    print(grid)


def get_coords(start, end):
    return itertools.product(range(start[0], end[0] + 1), range(start[1], end[1] + 1))


class Command(Enum):
    TURN_ON = (0,)
    TURN_OFF = (1,)
    TOGGLE = 2


def parse_coords(coords):
    return [int(x) for x in coords.split(",")]


def parse_command(command):
    if command == "turn on":
        return Command.TURN_ON
    elif command == "turn off":
        return Command.TURN_OFF
    elif command == "toggle":
        return Command.TOGGLE


def parse(data):
    commands = []
    for line in data.splitlines():
        groups = re.search(
            "^(turn on|turn off|toggle) (.*) through (.*)", line
        ).groups()
        commands.append(
            (parse_command(groups[0]), parse_coords(groups[1]), parse_coords(groups[2]))
        )
    return commands


def part1(commands):
    lights = [0] * SIZE**2

    for command, start, end in commands:
        # print(command, start, end)
        for x, y in get_coords(start, end):
            if command == Command.TURN_ON:
                lights[x * SIZE + y] = 1
            elif command == Command.TURN_OFF:
                lights[x * SIZE + y] = 0
            elif command == Command.TOGGLE:
                lights[x * SIZE + y] = not lights[x * SIZE + y]
            else:
                print("ALERT!!!!")

    return sum(lights)


def part2(commands):
    lights = [0] * SIZE**2

    for command, start, end in commands:
        # print(command, start, end)
        for x, y in get_coords(start, end):
            if command == Command.TURN_ON:
                lights[x * SIZE + y] += 1
            elif command == Command.TURN_OFF:
                lights[x * SIZE + y] = max(0, lights[x * SIZE + y] - 1)
            elif command == Command.TOGGLE:
                lights[x * SIZE + y] += 2
            else:
                print("ALERT!!!!")

    return sum(lights)


TEST_DATA = {}
TEST_DATA[
    """\
turn on 1,10 through 5,15
""".rstrip()
] = (30, 30)
