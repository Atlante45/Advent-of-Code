#!/usr/bin/env python3

import sys


def lineToArray(line):
    return list(map(lambda c: int(c), list(line.strip())))

def part1(lines):
    numLines = len(lines)

    mask = list(map(lambda c: '1', list(lines[0].strip())))
    mask = int("".join(mask), 2)

    bitLists = list(map(lineToArray, lines))
    mostCommonBits = [str(round(sum(i) / numLines)) for i in zip(*bitLists)]
    gammaRate = int("".join(mostCommonBits), 2)
    epsilonRate = ~gammaRate & mask

    print(gammaRate, epsilonRate, gammaRate * epsilonRate)

def bitOccurence(index, bitLists):
    bitsAtIndex = [bits[index] for bits in bitLists]
    zeroOccurence = bitsAtIndex.count(0)
    return (zeroOccurence, len(bitsAtIndex) - zeroOccurence)

def bitFilter(val, index, bitLists):
    return list(filter(lambda l: l[index] == val, bitLists))

def computeRating(criteria, bitLists):

    for i in range(len(bitLists[0])):
        (zeros, ones) = bitOccurence(i, bitLists)
        bitLists = bitFilter(criteria(zeros, ones), i, bitLists)

        if len(bitLists) == 1:
            break
    
    print(bitLists)

    return int("".join(map(lambda c: str(c), bitLists[0])), 2)

def part2(lines):
    
    bitLists = list(map(lineToArray, lines))

    oxRating = computeRating(lambda z, o: int(not z > o), bitLists)
    co2Rating = computeRating(lambda z, o: int(not z <= o), bitLists)

    print(f'Part 2: {oxRating * co2Rating}')


def main():
    with open('day3/input.txt') as f:
        lines = f.readlines()

        part1(lines)
        part2(lines)
        


if __name__ == "__main__":
    main()