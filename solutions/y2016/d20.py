import re


def parse(data):
    return sorted([tuple(map(int, line.split("-"))) for line in data.splitlines()])


def part1(ip_ranges):
    ip = 0
    for range in ip_ranges:
        if ip < range[0]:
            return ip
        ip = max(ip, range[1] + 1)


def part2(ip_ranges):
    allowed = 0
    ip = 0
    for range in ip_ranges:
        if ip < range[0]:
            allowed += range[0] - ip
        ip = max(ip, range[1] + 1)
    return allowed + (2**32 - ip)


TEST_DATA = {}
TEST_DATA[
    """\
5-8
0-2
4-7
""".rstrip()
] = (3, None)
