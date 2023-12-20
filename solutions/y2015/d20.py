from itertools import count
from math import ceil


def gifts(num):
    return sum(i + (num // i) for i in range(1, int(num**0.5) + 1) if num % i == 0)


def gifts2(num):
    return sum([num // i for i in range(1, 51) if num % i == 0])


def parse(data):
    return int(data)


def part1(target):
    target = ceil(target / 10)

    for house in count(target // 5):
        if gifts(house) >= target:
            return house


def part2(target):
    target = ceil(target / 11)

    for house in count(target // 50):
        if gifts2(house) >= target:
            return house


TEST_DATA = {}
# TEST_DATA[
#     """\
# 150
# """.rstrip()
# ] = (8, None)
