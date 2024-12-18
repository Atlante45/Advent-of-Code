def parse(data):
    return data.strip()


def react(polymer, ignore=None):
    pol = []
    for c in polymer:
        if len(pol) > 0 and pol[-1] == c.swapcase():
            pol.pop()
        elif c.lower() != ignore:
            pol.append(c)
    return pol


def part1(polymer):
    return len(react(polymer))


def part2(polymer):
    units = set(polymer.lower())
    return min(len(react(polymer, u)) for u in units)


TEST_DATA = {}
TEST_DATA[
    """\
dabAcCaCBAcCcaDA
""".rstrip()
] = (10, 4)
