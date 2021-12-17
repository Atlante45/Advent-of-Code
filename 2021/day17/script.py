#!/usr/bin/env python3
import os

def yhits(yvel, yrange):
    y = 0
    while y + yvel >= yrange[0]:
        # print(y, yvel, yrange)
        y += yvel
        yvel -= 1

    return y <= yrange[1]

def part1(xrange, yrange):
    maxy = 0
    for y in range(1000):
        if yhits(y, yrange):
            maxy = max(maxy, y)

    return maxy*(maxy+1)//2

def yhitsatstep(minstep, maxstep, yrange):
    count = 0
    for yvel in range(yrange[0], 1000):
        cur = yvel
        y = 0
        step = 0
        for _ in range(maxstep):
            y += yvel
            yvel -= 1
            step += 1

            if y >= yrange[0] and y <= yrange[1] and step >= minstep:
                # print(f'   yvel={cur} = HIT!!')
                count += 1
                break

    return count

def part2(xrange, yrange):
    count = 0
    for xvel in range(xrange[1] + 1):
        cur = xvel
        x = 0
        minstep = 100000000
        maxstep = 0
        step = 0
        while x + xvel <= xrange[1] and step < 1000:
            x += xvel
            xvel = max(0, xvel - 1)
            step += 1
            if x >= xrange[0]:
                minstep = min(minstep, step)
                maxstep = max(maxstep, step)
        if minstep > 0:
            # print(f'xvel={cur}')
            count += yhitsatstep(minstep, maxstep, yrange)

    return count

def readInput(filename):
    with open(filename) as f:
        return f.readlines()

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:

        if filename == 'example.txt':
            xrange = (20, 30)
            yrange = (-10, -5)
        else:
            xrange = (138, 184)
            yrange =  (-125, -71)
        print(f'Solving {filename}')
        print(f"    Part 1: {part1(xrange, yrange)}")
        print(f"    Part 2: {part2(xrange, yrange)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
