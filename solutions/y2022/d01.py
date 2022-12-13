def parse(data):
    return [sum(map(int, chunk.splitlines())) for chunk in data.split("\n\n")]


def part1(input):
    return max(input)


def part2(input):
    return sum(sorted(input)[-3:])


TEST_DATA = {}
TEST_DATA[
    """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".rstrip()
] = (24000, 45000)
