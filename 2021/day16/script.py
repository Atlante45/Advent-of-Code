#!/usr/bin/env python3
import math
import os

versions = []


def readPacket(bits):
    global versions

    i = 0
    version = int(bits[i:i+3], 2)
    versions.append(version)
    type = int(bits[i+3:i+6], 2)
    i += 6
    # print(f'v={version}, t={type}')

    if type == 4:
        nread, literal = readLiteral(bits[i:])
        # print(f'literal={literal} ({nread})')
        i += nread
        return i, literal
    else:

        vals = []
        ltype = bits[i]
        i += 1
        if ltype == '0':
            length = int(bits[i:i+15], 2)
            i += 15
            # print(f'ltype={ltype}, length={length}')

            nread = 0
            while nread < length:
                read, val = readPacket(bits[i + nread:])
                nread += read
                vals.append(val)
            i += nread

        else:
            length = int(bits[i:i+11], 2)
            i += 11
            # print(f'ltype={ltype}, length={length}')

            nread = 0
            for _ in range(length):
                read, val = readPacket(bits[i + nread:])
                nread += read
                vals.append(val)
            i += nread

        if type == 0:
            return i, sum(vals)
        elif type == 1:
            return i, math.prod(vals)
        elif type == 2:
            return i, min(vals)
        elif type == 3:
            return i, max(vals)
        elif type == 5:
            return i, vals[0] > vals[1]
        elif type == 6:
            return i, vals[0] < vals[1]
        elif type == 7:
            return i, vals[0] == vals[1]

    print('SOMETHING WENT WRONG!!!!')

def readLiteral(bits):
    i = 0
    number = ''
    while bits[i] == '1':
        number += bits[i + 1:i + 5]
        i += 5
    number += bits[i + 1:i + 5]
    number = int(number, 2)
    return (i + 5, number)

def part1(input):
    versions.clear()

    bits = bin(int(input, 16)).lstrip('0b').zfill(4 * len(input))
    # print(bits)

    readPacket(bits)

    return sum(versions)

def part2(input):
    bits = bin(int(input, 16)).lstrip('0b').zfill(4 * len(input))
    # print(bits)

    _, res = readPacket(bits)
    return res


def readInput(filename):
    with open(filename) as f:
        return f.readlines()

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        input = input[0].strip()

        print(f'Solving {filename}')
        print(f"    Part 1: {part1(input)}")
        print(f"    Part 2: {part2(input)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
