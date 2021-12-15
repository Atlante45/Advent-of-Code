#!/usr/bin/env python3
import os
from queue import PriorityQueue

def neighbors4(i, j, max_i, max_j=None):
    if isinstance(max_i, list):
        max_j = len(max_i[0])
        max_i = len(max_i)

    if not max_j:
        max_j = max_i

    cells = [
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
    ]

    return [(x, y) for (x, y) in cells if x >= 0 and x < max_i and y >= 0 and y < max_j]

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(start, goal, neighbors, cost):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in neighbors(current):
            new_cost = cost_so_far[current] + cost(next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far

def part1(input):
    size = len(input)
    start = (0, 0)
    end = (size - 1, size - 1)

    def neighbors(n):
        i, j = n
        return neighbors4(i, j, input)
    def cost(n):
        i, j = n
        return input[i][j]
    _, cost_so_far = a_star_search(start, end, neighbors, cost)
    return cost_so_far[end]

def part2(input):
    size = len(input)
    start = (0, 0)
    end = (5 * size - 1, 5 * size - 1)

    def neighbors(n):
        i, j = n
        return neighbors4(i, j, 5 * size, 5 * size)
    def cost(n):
        i, j = n
        return (input[i % size][j % size] + i // size + j // size - 1) % 9 + 1
    _, cost_so_far = a_star_search(start, end, neighbors, cost)
    return cost_so_far[end]


def readInput(filename):
    with open(filename) as f:
        return f.readlines()

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        data = []
        for line in input:
            data.append([int(v) for v in line.strip()])

        print(f'Solving {filename}')
        print(f"    Part 1: {part1(data)}")
        print(f"    Part 2: {part2(data)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
