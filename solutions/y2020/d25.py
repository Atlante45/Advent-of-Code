from itertools import count


def parse(data):
    k1, k2 = data.splitlines()
    return int(k1), int(k2)


def part1(k1, k2):
    value = 1
    for i in count(1):
        value = (value * 7) % 20201227
        if value == k1 or value == k2:
            break

    if value == k1:
        k1, k2 = k2, k1

    value = 1
    for _ in range(i):
        value = (value * k1) % 20201227
    return value


def part2(k1, k2):
    pass


TEST_DATA = {}
TEST_DATA[
    """\
17807724
5764801
""".rstrip()
] = (14897079, None)
