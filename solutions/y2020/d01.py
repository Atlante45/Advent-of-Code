def parse(data):
    return [int(v.strip()) for v in data.splitlines()]


def part1(input):
    for i in input:
        if 2020 - i in input:
            return i * (2020 - i)


def part2(input):
    for i in range(len(input) - 2):
        for j in range(i + 1, len(input) - 1):
            if 2020 - input[i] - input[j] in input:
                return input[i] * input[j] * (2020 - input[i] - input[j])


TEST_DATA = {}
TEST_DATA[
    """\
1721
979
366
299
675
1456
""".rstrip()
] = (514579, 241861950)
