from collections import deque


def parse(data):
    return int(data.strip())


def part1(elves):
    return int(bin(elves)[3:] + "1", 2)


def part2(elves):
    h1 = deque(range(1, elves // 2 + 1))
    h2 = deque(range(elves // 2 + 1, elves + 1))
    while h1 and h2:
        if len(h1) > len(h2):
            h1.pop()
        else:
            h2.popleft()
        h2.append(h1.popleft())
        h1.append(h2.popleft())
    return h1[0] or h2[0]


TEST_DATA = {}
TEST_DATA[
    """\
5
""".rstrip()
] = (3, 2)


# t = (i + (len - i) // 2) % len

# 1 1
# 1 0

# 1 1 1
# 0 0 3

# 1 1 1 1
# 2 2 0 0

# 1 1 1 1 1
# 0 2 0 3 0
