from collections import deque
from itertools import pairwise


def parse(data):
    return list(map(int, data.strip()))


def part1(cups):
    num_cups = len(cups)

    for i in range(100):
        current = cups[0]
        picked = cups[1:4]
        cups = cups[4:]

        destination = (current - 2) % num_cups + 1
        while destination not in cups:
            destination = (destination - 2) % num_cups + 1

        index = cups.index(destination)
        cups = cups[: index + 1] + picked + cups[index + 1 :]
        cups.append(current)

    index = cups.index(1)
    return int("".join(map(str, cups[index + 1 :] + cups[:index])))


def part2(cups):
    og_cups = [c - 1 for c in cups]

    cups = list(range(1, 1000001))
    cups[og_cups[-1]] = len(og_cups)
    cups[len(cups) - 1] = og_cups[0]

    for a, b in pairwise(og_cups):
        cups[a] = b

    current = og_cups[0]
    for _ in range(10000000):
        picked = [cups[current], cups[cups[current]], cups[cups[cups[current]]]]
        cups[current] = cups[picked[-1]]

        destination = (current - 1) % len(cups)
        while destination in picked:
            destination = (destination - 1) % len(cups)

        temp = cups[destination]
        cups[destination] = picked[0]
        cups[picked[-1]] = temp

        current = cups[current]

    return (cups[0] + 1) * (cups[cups[0]] + 1)


TEST_DATA = {}
TEST_DATA[
    """\
389125467
""".rstrip()
] = (67384529, 149245887792)
