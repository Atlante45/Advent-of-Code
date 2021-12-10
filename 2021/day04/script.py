#!/usr/bin/env python3

import os

class BingoCard:


    def __init__(self, lines):
        self.grid = []
        self.count = 0
        self.cols = [0] * 5
        self.rows =  [0] * 5
        self.won =  False
        
        for line in lines:
            line = line.strip()
            for val in line.split():
                self.grid.append(int(val))
                self.count += int(val)
    
    def check(self, number):
        if self.won:
            return False

        if number in self.grid:
            self.count -= number
            
            index = self.grid.index(number)
            row = index // 5
            col = index % 5

            self.rows[row] += 1
            self.cols[col] += 1

            self.won = self.rows[row] == 5 or self.cols[col] == 5

            return self.won
        
        return False
        


def parse_input(lines):
    numbers = lines[0].strip().split(',')
    numbers = list(map(lambda v: int(v), numbers))
    lines = lines[2:]

    cards = []

    while lines:
        cards.append(BingoCard(lines[0:5]))
        lines = lines[6:]

    return (numbers, cards) 

def part1(lines):
    (numbers, cards) = parse_input(lines)
    
    res = 0

    for n in numbers:
        for c in cards:
            if c.check(n):
                res = c.count * n
                break
        
        if res: break

    print(f'Part 1: {res}')


def part2(lines):
    (numbers, cards) = parse_input(lines)
    
    res = 0

    cardsLeft = len(cards)

    for n in numbers:
        for c in cards:
            if c.check(n):
                cardsLeft -= 1

                if cardsLeft == 0:
                    res = c.count * n
                    break

        
        if res: break
    print(f'Part 2: {res}')



def readInput(filename):
    with open(filename) as f:
        return f.readlines()

def main():
    # inputfile = os.path.join(os.path.dirname(__file__), 'test.txt')
    inputfile = os.path.join(os.path.dirname(__file__), 'input.txt')

    lines = readInput(inputfile)

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()