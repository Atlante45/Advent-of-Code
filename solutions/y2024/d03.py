import re

R1 = re.compile(r"mul\((\d+),(\d+)\)")
R2 = re.compile(r"don't\(\).*?do\(\)", re.DOTALL)

def parse(data):
    return data

def part1(data):
    return sum(int(a) * int(b) for a, b in R1.findall(data))

def part2(data):
    return part1(R2.sub("", data + "do()"))


TEST_DATA = {}
TEST_DATA[
    """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""".rstrip()
] = (161, 161)
TEST_DATA[
    """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".rstrip()
] = (161, 48)
