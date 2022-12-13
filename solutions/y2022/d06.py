def find_start(data, n):
    return next(i + n for i in range(len(data) - n) if len(set(data[i : i + n])) == n)


def parse(data):
    return data.strip()


def part1(data):
    return find_start(data, 4)


def part2(data):
    return find_start(data, 14)


TEST_DATA = {}
TEST_DATA[
    """\
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
""".rstrip()
] = (11, 26)
