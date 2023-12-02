from curses.ascii import isdigit

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def parse(data):
    return data.splitlines()


def part1(lines):
    sum = 0
    for line in lines:
        sum += int(next(filter(isdigit, line)) + next(filter(isdigit, reversed(line))))
    return sum


def part2(lines):
    sum = 0
    for line in lines:
        first = None
        for i in range(0, len(line)):
            if isdigit(line[i]):
                first = int(line[i])
                break
            for j in range(0, len(numbers)):
                if line[i:].startswith(numbers[j]):
                    first = j + 1
                    break
            if first is not None:
                break

        last = None
        for i in reversed(range(0, len(line))):
            if isdigit(line[i]):
                last = int(line[i])
                break
            for j in reversed(range(0, len(numbers))):
                if line[i:].startswith(numbers[j]):
                    last = j + 1
                    break
            if last is not None:
                break

        sum += 10 * first + last
    return sum


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
