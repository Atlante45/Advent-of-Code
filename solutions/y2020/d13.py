from math import gcd, lcm, prod


def parse(data):
    time, buses = data.splitlines()
    return int(time), [int(b) if b != "x" else None for b in buses.split(",")]


def part1(time, buses):
    min_wait = float("inf")
    min_bus = None

    for bus in buses:
        if bus is None:
            continue
        wait = bus - time % bus
        if wait < min_wait:
            min_wait = wait
            min_bus = bus

    return min_bus * min_wait


def part2(time, buses):
    M = lcm(*[b for b in buses if b is not None])

    sum = 0
    for offset, bus in enumerate(buses):
        if bus is None:
            continue
        ai = -offset % bus
        Mi = M // bus
        sum += ai * Mi * pow(Mi, -1, bus)

    return sum % M


TEST_DATA = {}
TEST_DATA[
    """\
939
7,13,x,x,59,x,31,19
""".rstrip()
] = (295, 1068781)
