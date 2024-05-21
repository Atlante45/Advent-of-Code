def parse(data):
    return int(data.strip())


def part1(repeat):
    buffer = [0]
    pos = 0
    for i in range(1, 2018):
        pos = (pos + repeat) % len(buffer) + 1
        buffer.insert(pos, i)
    return buffer[pos + 1]


def part2(repeat):
    pos = 0
    res = 0
    for i in range(1, 50_000_001):
        pos = (pos + repeat) % i + 1
        if pos == 1:
            res = i
    return res


TEST_DATA = {}
TEST_DATA[
    """\
3
""".rstrip()
] = (638, None)
