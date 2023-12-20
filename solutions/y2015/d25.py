import re


def parse(data):
    row, col = map(int, re.findall(r"\d+", data))
    return row, col


def next(code):
    return (code * 252533) % 33554393


def part1(row, col):
    index = sum(range(row + col - 1)) + col

    code = 20151125
    for i in range(index - 1):
        code = next(code)
    return code


def part2(row, col):
    pass


TEST_DATA = {}
TEST_DATA[
    """\
To continue, please consult the code grid in the manual.  Enter the code at row 6, column 6.
""".rstrip()
] = (27995004, None)
