from curses.ascii import isdigit

numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def replace(line):
    for i, n in enumerate(numbers):
        line = line.replace(n, n[0] + str(i + 1) + n[-1])
    return line


def parse(data):
    return data.splitlines()


def part1(lines):
    digits = [list(map(int, filter(isdigit, line))) for line in lines]
    return sum(10 * nums[0] + nums[-1] for nums in digits)


def part2(lines):
    lines = map(replace, lines)
    return part1(lines)


TEST_DATA = {}
TEST_DATA[
    """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".rstrip()
] = (142, None)
TEST_DATA[
    """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".rstrip()
] = (None, 281)
