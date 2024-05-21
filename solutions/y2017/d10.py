from functools import reduce
from math import prod
from more_itertools import batched


def twist(elements, lengths, current, skip):
    for length in lengths:
        if length > len(elements):
            continue
        for i in range(length // 2):
            a = (current + i) % len(elements)
            b = (current + length - i - 1) % len(elements)
            elements[a], elements[b] = elements[b], elements[a]

        current = (current + length + skip) % len(elements)
        skip += 1

    return elements, current, skip


def knot_hash(data):
    lengths = list(map(ord, data)) + [17, 31, 73, 47, 23]
    elements = list(range(256))

    current = skip = 0
    for _ in range(64):
        elements, current, skip = twist(elements, lengths, current, skip)

    res = ""
    for batch in batched(elements, 16):
        res += f"{reduce(lambda a, b: a ^ b, batch):02x}"
    return res


def parse(data):
    return data.strip()


def part1(data):
    lengths = list(map(int, data.split(",")))
    size = 256 if len(lengths) > 4 else 5

    elements = list(range(size))
    current = 0
    skip = 0

    elements, _, _ = twist(elements, lengths, current, skip)

    return prod(elements[:2])


def part2(data):
    return knot_hash(data)


TEST_DATA = {}
TEST_DATA[
    """\
3,4,1,5
""".rstrip()
] = (12, None)
TEST_DATA[
    """\

""".rstrip()
] = (None, "a2582a3a0e66e6e86e3812dcb672a272")
TEST_DATA[
    """\
AoC 2017
""".rstrip()
] = (None, "33efeb34ea91902bb2f59c9920caa6cd")
TEST_DATA[
    """\
1,2,3
""".rstrip()
] = (None, "3efbe78a8d82f29979031a4aa0b16a9d")
TEST_DATA[
    """\
1,2,4
""".rstrip()
] = (None, "63960835bcdc130f0b66d7ff4f6a5a8e")
