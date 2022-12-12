#!/usr/bin/env python3
from math import prod
import re
from solutions.utils import logger
from aocd import data

REGEX = r"Monkey (\d+):\n  Starting items: (.+)\n  Operation: new = old (.) (\d+|old)\n  Test: divisible by (\d+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)"


class Monkey:
    def __init__(self, chunk) -> None:
        groups = re.search(REGEX, chunk.strip()).groups()
        self.id = int(groups[0])
        self.items = list(map(int, groups[1].split(", ")))
        self.op = groups[2]
        self.val = groups[3]
        self.div = int(groups[4])
        self.tmon = int(groups[5])
        self.fmon = int(groups[6])

        self.examines = 0

        if self.val != "old":
            self.val = int(self.val)

    def has_items(self):
        return len(self.items)

    def num_examines(self):
        return self.examines

    def examine_item(self, level, gdiv=None):
        self.examines += 1
        item = self.items[0]
        self.items = self.items[1:]

        val = item if self.val == "old" else self.val
        if self.op == "*":
            item *= val
        else:
            item += val
        item //= level

        if gdiv is not None:
            item %= gdiv

        return (item, self.tmon if item % self.div == 0 else self.fmon)

    def catch_item(self, item):
        self.items.append(item)


def part1(data):
    monkeys = []

    chunks = data.split("\n\n")
    for chunk in chunks:
        monkeys.append(Monkey(chunk))

    for i in range(20):
        for m in monkeys:
            while m.has_items():
                item, nm = m.examine_item(3)
                monkeys[nm].catch_item(item)

    counts = []
    for m in monkeys:
        counts.append(m.num_examines())
    counts.sort()

    return prod(counts[-2:])


def part2(data):
    monkeys = []

    gdiv = 1

    chunks = data.split("\n\n")
    for chunk in chunks:
        monkeys.append(Monkey(chunk))
        gdiv *= monkeys[-1].div

    for i in range(10000):
        for m in monkeys:
            while m.has_items():
                item, nm = m.examine_item(1, gdiv)
                monkeys[nm].catch_item(item)

    counts = []
    for m in monkeys:
        counts.append(m.num_examines())
    counts.sort()

    return prod(counts[-2:])


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (None, None)
TEST_RESULT = (10605, 2713310158)
TEST_DATA = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
