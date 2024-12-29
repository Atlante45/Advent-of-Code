def parse(data):
    passwords = []
    for line in data.splitlines():
        a, b, c = line.split()
        a1, a2 = map(int, a.split("-"))

        passwords.append((a1, a2, b[0], c))
    return passwords


def part1(passwords):
    return sum(1 for a1, a2, b, c in passwords if a1 <= c.count(b) <= a2)


def part2(passwords):
    return sum(1 for a1, a2, b, c in passwords if (c[a1 - 1] == b) ^ (c[a2 - 1] == b))


TEST_DATA = {}
TEST_DATA[
    """\

""".rstrip()
] = (None, None)
