import re
from typing import Counter


REGEX = r"^([\w-]+)-(\d+)\[(\w+)\]$"


def parse(data):
    return [re.match(REGEX, line).groups() for line in data.splitlines()]


def is_real(name, checksum):
    cnt = Counter([c for c in name if c != "-"]).most_common()
    cnt = "".join(c for c, _ in sorted(cnt, key=lambda x: (-x[1], x[0])))[:5]
    return cnt == checksum


def decrypt(name, sector):
    return "".join(
        chr((ord(c) - ord("a") + sector) % 26 + ord("a")) if c != "-" else " "
        for c in name
    )


def part1(rooms):
    return sum(
        int(sector) for name, sector, checksum in rooms if is_real(name, checksum)
    )


def part2(rooms):
    ROOM = "northpole object storage"
    for name, sector, checksum in rooms:
        if is_real(name, checksum) and decrypt(name, int(sector)) == ROOM:
            return sector


TEST_DATA = {}
TEST_DATA[
    """\
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
""".rstrip()
] = (1514, None)
