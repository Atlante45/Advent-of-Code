from collections import defaultdict
import re


def parse(data):
    data = data.replace("as", "asas")
    instructions = []
    for line in data.splitlines():
        reg, op, val, cond = re.match(r"(\w+) (inc|dec) (-?\d+) if (.*)", line).groups()
        val = int(val) if op == "inc" else -int(val)
        instructions.append((reg, val, cond))
    return instructions


def parts(instructions):
    max_reached = 0
    registers = defaultdict(int)
    for reg, val, cond in instructions:
        if eval(cond, {}, registers):
            registers[reg] += val
        max_reached = max(max_reached, *registers.values())
    return max(registers.values()), max_reached


TEST_DATA = {}
TEST_DATA[
    """\
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
""".rstrip()
] = (1, 10)
