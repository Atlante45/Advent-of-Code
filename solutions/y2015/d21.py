from itertools import combinations
from math import ceil


WEAPONS = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]
ARMOR = [
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
    (0, 0, 0),
]
RINGS = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
    (0, 0, 0),
    (0, 0, 0),
]


def parse(data):
    return [int(line.split()[-1]) for line in data.splitlines()]


def fight(boss, *items):
    price, dmg, armor = [sum(x) for x in zip(*items)]
    mdmg = max(1, dmg - boss[2])
    hdmg = max(1, boss[1] - armor)
    turns = ceil(boss[0] / mdmg)
    turns2 = ceil(100 / hdmg)
    return turns <= turns2, price


def part1(boss):
    res = 1000000
    for w in WEAPONS:
        for a in ARMOR:
            for r1, r2 in combinations(RINGS, 2):
                win, price = fight(boss, w, a, r1, r2)
                res = min(res, price if win else 1000000)

    return res


def part2(boss):
    res = 0
    for w in WEAPONS:
        for a in ARMOR:
            for r1, r2 in combinations(RINGS, 2):
                win, price = fight(boss, w, a, r1, r2)
                res = max(res, price if not win else 0)

    return res


TEST_DATA = {}
TEST_DATA[
    """\
Hit Points: 103
Damage: 9
Armor: 2
""".rstrip()
] = (121, 201)
TEST_DATA[
    """\
Hit Points: 104
Damage: 8
Armor: 1
""".rstrip()
] = (78, 148)
