#!/usr/local/bin/python3
from collections import defaultdict
from enum import Enum
from functools import cache
import os

def draw(hallway, rooms):
    hallway_d = ''.join(x if x else '.' for x in hallway)
    rd = ['#'.join(x if x else '.' for x in r) for r in zip(*rooms.values())]
    print(f'#############')
    print(f'#{hallway_d}#')
    print(f'###{rd[0]}###')
    print(f'  #{rd[1]}#  ')
    if len(rd) > 2:
        print(f'  #{rd[2]}#  ')
        print(f'  #{rd[3]}#  ')
    print(f'  #########  ')

HALLWAY_POSITIONS = [0, 1, 3, 5, 7, 9, 10]

def move_cost(x):
    if x == 'A':
        return 1
    if x == 'B':
        return 10
    if x == 'C':
        return 100
    if x == 'D':
        return 1000

    print(x)
    raise 'PANIC'

def own_room(x):
    if x == 'A':
        return 2
    if x == 'B':
        return 4
    if x == 'C':
        return 6
    if x == 'D':
        return 8

    print(x)
    raise 'PANIC'

def room(hallway, rooms, r):
    return hallway if r == 0 else rooms[r]

def unmove(hallway, rooms, m):
    s, d = m
    move(hallway, rooms, (d, s))

def move(hallway, rooms, m):
    (a, b), (c, d) = m
    room_a = room(hallway, rooms, a)
    room_c = room(hallway, rooms, c)
    room_a[b], room_c[d] = room_c[d], room_a[b]

    cost = abs((d if c == 0 else c) - (b if a == 0 else a))
    cost += b+1 if a != 0 else 0
    cost += d+1 if c != 0 else 0
    return cost * move_cost(room_c[d])

def room_open(rooms, r):
    return all(own_room(v) == r for v in rooms[r] if v)

def path_clear(hallway, src, dst):
    return not [a for a in hallway[min(src + 1, dst):max(src, dst + 1)] if a]

def solved(rooms):
    for r, slots in rooms.items():
        if any(not v or own_room(v) != r for v in slots):
            return False
    return True

def possible_moves(hallway, rooms):
    moves = defaultdict(list)

    for i, x in enumerate(hallway):
        if not x:
            continue

        src = 0, i
        r = own_room(x)
        if room_open(rooms, r) and path_clear(hallway, i, r):
            slots = rooms[r]
            slot = next((s for s, x in enumerate(slots) if x), len(slots)) - 1
            return [(src, (r, slot))]

    for i, slots in rooms.items():
        s, x = next(((s, x) for s, x in enumerate(slots) if x), (None, None))
        if not x:
            continue

        src = i, s
        r = own_room(x)
        if r == i and room_open(rooms, r):
            continue

        if room_open(rooms, r) and path_clear(hallway, i, r):
            slots = rooms[r]
            slot = next((s for s, x in enumerate(slots) if x), len(slots)) - 1
            return [(src, (r, slot))]


        for p in HALLWAY_POSITIONS:
            if path_clear(hallway, i, p):
                moves[x].append((src, (0, p)))

    return moves['A'] + moves['B'] + moves['C'] + moves['D']

@cache
def recurse(hallway, rooma, roomb, roomc, roomd):
    hallway = list(hallway)
    rooms = {2: list(rooma), 4: list(roomb), 6: list(roomc), 8: list(roomd)}
    if solved(rooms):
        return 0

    min_cost = 1000000000

    for m in possible_moves(list(hallway), rooms):
        c = move(hallway, rooms, m)
        new_min_cost = recurse(tuple(hallway), tuple(rooms[2]), tuple(rooms[4]), tuple(rooms[6]), tuple(rooms[8]))
        min_cost = min(min_cost, c + new_min_cost)
        unmove(hallway, rooms, m)

    return min_cost

def part1(hallway, rooms):
    return recurse(tuple(hallway), tuple(rooms[2]), tuple(rooms[4]), tuple(rooms[6]), tuple(rooms[8]))

def part2(hallway, rooms):
    rooms[2] = [rooms[2][0], 'D', 'D', rooms[2][1]]
    rooms[4] = [rooms[4][0], 'C', 'B', rooms[4][1]]
    rooms[6] = [rooms[6][0], 'B', 'A', rooms[6][1]]
    rooms[8] = [rooms[8][0], 'A', 'C', rooms[8][1]]

    return recurse(tuple(hallway), tuple(rooms[2]), tuple(rooms[4]), tuple(rooms[6]), tuple(rooms[8]))


def readInput(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        hallway = [None] * 11
        rooms = {
            2: [input[2][3], input[3][1]],
            4: [input[2][5], input[3][3]],
            6: [input[2][7], input[3][5]],
            8: [input[2][9], input[3][7]],
        }

        print(f'Solving {filename}')
        draw(hallway, rooms)
        print(f"    Part 1: {part1(hallway, rooms)}")
        print(f"    Part 2: {part2(hallway, rooms)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
