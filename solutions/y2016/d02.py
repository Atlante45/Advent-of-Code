from solutions.utils.graph import p, v

DIR = {"U": v(-1, 0), "D": v(1, 0), "L": v(0, -1), "R": v(0, 1)}
KEYPAD = [
    [" ", " ", " ", " ", " "],
    [" ", "1", "2", "3", " "],
    [" ", "4", "5", "6", " "],
    [" ", "7", "8", "9", " "],
    [" ", " ", " ", " ", " "],
]
KEYPAD2 = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "1", " ", " ", " "],
    [" ", " ", "2", "3", "4", " ", " "],
    [" ", "5", "6", "7", "8", "9", " "],
    [" ", " ", "A", "B", "C", " ", " "],
    [" ", " ", " ", "D", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
]


def solve(lines, keypad, start):
    code = ""
    pos = start
    for line in lines:
        for step in line:
            new_pos = pos + DIR[step]
            if keypad[new_pos[0]][new_pos[1]] != " ":
                pos = new_pos
        code += keypad[pos[0]][pos[1]]

    return code


def parse(data):
    return data.splitlines()


def part1(lines):
    return solve(lines, KEYPAD, p(2, 2))


def part2(lines):
    return solve(lines, KEYPAD2, p(3, 1))


TEST_DATA = {}
TEST_DATA[
    """\
ULL
RRDDD
LURDL
UUUUD
""".rstrip()
] = ("1985", "5DB3")
