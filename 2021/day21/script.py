#!/usr/bin/env python3
from collections import defaultdict
import os
from tkinter import scrolledtext
from turtle import pos, position

def roll_die(x):
    # print(x)
    res = x
    x = (x + 1) % 100
    res += x
    x = (x + 1) % 100
    res += x
    # print('  ', res + 3)
    return res + 3

def part1(input):
    res = 0

    pos1 = input[0] - 1
    pos2 = input[1] - 1
    score1 = 0
    score2 = 0
    die = 0
    rolls = 0
    while score1 < 1000 and score2 < 1000:
        pos1 = (pos1 + roll_die(die)) % 10
        score1 += pos1 + 1
        die = (die + 3) % 100
        rolls += 3
        # print(f'1: {pos1} {score1}')
        if score1 >= 1000:
            # print(rolls, score1, score2)
            return rolls * score2


        pos2 = (pos2 + roll_die(die)) % 10
        score2 += pos2 + 1
        die = (die + 3) % 100
        rolls += 3
        # print(f'2: {pos2} {score2}')
        if score2 >= 1000:
            # print(rolls, score1, score2)
            return rolls * score1


    # print(score1, score2)
    return score1 * score2

UNIVERSES = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]
UNIVERSES_MULT = sum(UNIVERSES)

def part2(input):
    boards = {}
    boards[(input[0] - 1, input[1] - 1, 0, 0)] = 1

    wins = [0, 0]
    while boards:
        # print(boards)
        new_boards = defaultdict(int)
        for board, uni_count in boards.items():
            # print(board, uni_count)
            pos1, pos2, score1, score2 = board
            for rolls in range(3, 10):
                new_pos1 = (pos1 + rolls) % 10
                new_score1 = score1 + new_pos1 + 1
                new_uni_count1 = uni_count * UNIVERSES[rolls]
                if new_score1 >= 21:
                    wins[0] += new_uni_count1
                else:
                    for rolls in range(3, 10):
                        new_pos2 = (pos2 + rolls) % 10
                        new_score2 = score2 + new_pos2 + 1
                        new_uni_count2 = new_uni_count1 * UNIVERSES[rolls]
                        if new_score2 >= 21:
                            wins[1] += new_uni_count2
                        else:
                            # print(new_pos1, new_pos2, new_score1, new_score2)
                            new_boards[(new_pos1, new_pos2, new_score1, new_score2)] += new_uni_count2

        boards = new_boards
        # print(boards)
        # break

    # print(wins)
    return max(wins)


def readInput(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        if filename == "example.txt":
            input = (4, 8)
        else:
            input = (4, 10)
        print(f'Solving {filename}')
        print(f"    Part 1: {part1(input)}")
        print(f"    Part 2: {part2(input)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
