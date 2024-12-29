from itertools import zip_longest
import re


def parse(data):
    return data.splitlines()


def part1(lines):
    mask_0 = 0
    mask_1 = 0
    mem = {}

    for line in lines:
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
            mask_0 = int(mask.replace("X", "1"), 2)
            mask_1 = int(mask.replace("X", "0"), 2)
        else:
            addr, val = re.match(r"mem\[(\d+)\] = (\d+)", line).groups()
            addr = int(addr)
            val = int(val)
            mem[addr] = (val & mask_0) | mask_1

    return sum(mem.values())


def generate_addresses(addr, mask):
    addr = [a if b == "0" else b for a, b in zip_longest(bin(addr)[2:].zfill(36), mask)]

    for i in range(2 ** mask.count("X")):
        li = list(bin(i)[2:].zfill(mask.count("X")))
        yield int("".join([a if a != "X" else li.pop() for a in addr]), 2)


def part2(lines):
    mem = {}
    for line in lines:
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
        else:
            addr, val = re.match(r"mem\[(\d+)\] = (\d+)", line).groups()
            addr = int(addr)
            val = int(val)
            for addr in generate_addresses(addr, mask):
                mem[addr] = val

    return sum(mem.values())


TEST_DATA = {}
TEST_DATA[
    """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".rstrip()
] = (165, None)
TEST_DATA[
    """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".rstrip()
] = (None, 208)
