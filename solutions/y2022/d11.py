from math import prod
import re

REGEX = a = re.compile(
    r"""
Monkey (\d+):
  Starting items: (.+)
  Operation: new = old (.) (\d+|old)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)
    """.strip()
)


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


def parse(data):
    monkeys = []
    gdiv = 1

    chunks = data.split("\n\n")
    for chunk in chunks:
        monkeys.append(Monkey(chunk))
        gdiv *= monkeys[-1].div

    return monkeys, gdiv


def part1(monkeys, _):
    for _ in range(20):
        for m in monkeys:
            while m.has_items():
                item, nm = m.examine_item(3)
                monkeys[nm].catch_item(item)

    counts = sorted(m.num_examines() for m in monkeys)
    return prod(counts[-2:])


def part2(monkeys, gdiv):
    for _ in range(10000):
        for m in monkeys:
            while m.has_items():
                item, nm = m.examine_item(1, gdiv)
                monkeys[nm].catch_item(item)

    counts = sorted(m.num_examines() for m in monkeys)
    return prod(counts[-2:])


TEST_DATA = {}
TEST_DATA[
    """\
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
] = (10605, 2713310158)
