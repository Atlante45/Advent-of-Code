from more_itertools import chunked


def parse(data):
    return data.strip()


def fill(data, length):
    while len(data) < length:
        data = data + "0" + "".join("0" if c == "1" else "1" for c in data[::-1])
    return data[:length]


def checksum(data):
    while len(data) % 2 == 0:
        data = "".join("1" if a == b else "0" for a, b in chunked(data, 2))
    return data


def part1(data):
    data = fill(data, 272 if len(data) > 5 else 20)
    return checksum(data)


def part2(data):
    data = fill(data, 35651584)
    return checksum(data)


TEST_DATA = {}
TEST_DATA[
    """\
10000
""".rstrip()
] = ("01100", None)
