import re
from z3 import Solver, Ints, sat

R1 = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X\=(\d+), Y\=(\d+)")

def parse(data):
    machines = []
    for machine in data.split('\n\n'):
        match = R1.match(machine)
        machines.append(list(map(int, match.groups())))
    return machines

def solve(ax, ay, bx, by, px, py, added):
    S = Solver()
    a, b = Ints("a b")
    S.add(a * ax + b * bx == px + added)
    S.add(a * ay + b * by == py + added)
    return S.model()[a].as_long() * 3 + S.model()[b].as_long() if S.check() == sat else 0

def part1(machines):
    return sum(solve(*machine, 0) for machine in machines)

def part2(machines):
    return sum(solve(*machine, 10000000000000) for machine in machines)

TEST_DATA = {}
TEST_DATA[
    """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".rstrip()
] = (480, None)
