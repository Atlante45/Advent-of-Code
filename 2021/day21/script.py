#!/usr/bin/env python3
from collections import defaultdict
from itertools import count
import os

def roll(die):
    return 1 + (next(die) - 1) % 100

def step(positions, scores, player, die):
    move = roll(die) + roll(die) + roll(die)
    positions[player] = (positions[player] + move) % 10
    scores[player] += positions[player] + 1

def part1(input):
    die = count(1)

    positions = [input[0] - 1, input[1] - 1]
    scores = [0, 0]
    while True:
        for player in range(2):
            step(positions, scores, player, die)
            if scores[player] >= 1000:
                return (next(die) - 1) * scores[player - 1]


UNIVERSES = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]

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
