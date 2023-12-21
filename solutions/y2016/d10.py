from collections import defaultdict
from math import prod
import re


def parse(data):
    bots = defaultdict(list)
    rules = {}
    for line in data.splitlines():
        if "value" in line:
            inst = re.match(r"^value (\d+) goes to (.+)$", line).groups()
            bots[inst[1]].append(int(inst[0]))
        else:
            inst = re.match(r"^(.+) gives low to (.+) and high to (.+)$", line).groups()
            rules[inst[0]] = (inst[1], inst[2])
    return bots, rules


def parts(bots, rules):
    p1res = None
    todo = [bot for bot, chips in bots.items() if len(chips) == 2]
    while todo:
        bot = todo.pop()
        chips = bots[bot]
        if len(chips) == 2:
            low, high = sorted(chips)
            if low == 17 and high == 61:
                p1res = bot.split()[1]
            chips.clear()
            rule = rules[bot]
            bots[rule[0]].append(low)
            bots[rule[1]].append(high)
            todo.append(rule[0])
            todo.append(rule[1])
    return p1res, prod(bots[f"output {i}"][0] for i in range(3))


TEST_DATA = {}
