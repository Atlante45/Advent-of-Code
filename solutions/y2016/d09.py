def parse(data):
    return data.replace("\n", "")


def decompress(data, recursive):
    size = 0
    pos = 0
    while pos < len(data):
        if data[pos] == "(":
            end = data.find(")", pos)
            length, repeat = map(int, data[pos + 1 : end].split("x"))
            if recursive:
                size += decompress(data[end + 1 : end + 1 + length], True) * repeat
            else:
                size += length * repeat
            pos = end + 1 + length
        else:
            size += 1
            pos += 1
    return size


def part1(lines):
    return decompress(lines, False)


def part2(lines):
    return decompress(lines, True)


TEST_DATA = {}
TEST_DATA[
    """\
X(8x2)(3x3)ABCY
""".rstrip()
] = (18, 20)
