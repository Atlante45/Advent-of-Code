def score1(adv, me):
    if (adv + 1) % 3 == me:
        return 6 + me + 1
    elif adv == me:
        return 3 + me + 1
    else:
        return 0 + me + 1


def score2(adv, end):
    if end == 0:
        return 0 + 1 + (adv + 2) % 3
    elif end == 1:
        return 3 + 1 + adv
    else:
        return 6 + 1 + (adv + 1) % 3


def compute(input, func):
    return sum([func(*game) for game in input])


def parse(data):
    return [
        (ord(line[0]) - ord("A"), ord(line[2]) - ord("X")) for line in data.splitlines()
    ]


def part1(input):
    return compute(input, score1)


def part2(input):
    return compute(input, score2)


TEST_DATA = {}
TEST_DATA[
    """\
A Y
B X
C Z
""".rstrip()
] = (15, 12)
