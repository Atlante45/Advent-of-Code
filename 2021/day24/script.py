#!/usr/local/bin/python3
from functools import cache
import os

@cache
def compute_substep(w, z, c):
    x = w != (z % 26 + c[1])
    y = 25 * x + 1
    z = y * (z // c[0]) + (w + c[2]) * x
    return z

constants = []

@cache
def compute_step(z, step, inversed = True):
    if step == 14:
        return z == 0, ''

    global constants
    c = constants[step]
    r = range(1, 10)
    if inversed:
        r = reversed(r)
    for i in r:
        new_z = compute_substep(i, z, c)
        if new_z < 0:
            continue

        valid, monad = compute_step(new_z, step + 1, inversed)
        if valid:
            return valid, str(i) + monad

    return False, ''

def part1():
    valid, monad = compute_step(0, 0)
    assert(valid)
    return monad

def part2():
    valid, monad = compute_step(0, 0, False)
    assert(valid)
    return monad



def readInput(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        input = [line.split() for line in input]

        global constants
        constants = []
        for i in range(14):
            constants.append((int(input[18*i + 4][2]), int(input[18*i + 5][2]), int(input[18*i + 15][2])))

        print(f'Solving {filename}')
        print(f"    Part 1: {part1()}")
        print(f"    Part 2: {part2()}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
