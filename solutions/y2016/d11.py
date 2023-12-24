from collections import defaultdict
import heapq
from itertools import pairwise
import re


DEBUG = False


def debug(elevator, generators, microchips):
    if not DEBUG:
        return
    for i in range(4, -1, -1):
        print(f"F{i} {'E  ' if elevator == i else '.  '} ", end="")
        for x in range(len(generators)):
            print(str(x) + "G " if generators[x] == i else ".  ", end="")
            print(str(x) + "M " if microchips[x] == i else ".  ", end="")
        print()


def debug2(rec):
    if not DEBUG:
        return
    R = "\033[0m"
    for s1, s2 in pairwise(rec):
        _, _, el, ge, mi = s1
        steps, moves, elevator, generators, microchips = s2
        print(f"==== Move {moves} - {steps} steps ====")
        for i in range(4, -1, -1):
            c = "\033[92m" if elevator == i and el != i else ""
            print(f"F{i} {c}{'E  ' if elevator == i else '.  '}{R}", end="")
            for x in range(len(generators)):
                c = "\033[92m" if generators[x] == i and ge[x] != i else ""
                print(f"{c}{x}G{R} " if generators[x] == i else ".  ", end="")
                c = "\033[92m" if microchips[x] == i and mi[x] != i else ""
                print(f"{c}{x}M{R} " if microchips[x] == i else ".  ", end="")
            print()
        print()


def is_valid(elevator, generators, microchips):
    for i in range(len(generators)):
        if (
            generators[i] == microchips[i]
            or (microchips[i], generators[i]) == (0, elevator)
            or (microchips[i], generators[i]) == (elevator, 0)
        ):
            continue
        if (
            microchips[i] in generators
            or (microchips[i] == 0 and elevator in generators)
            or (microchips[i] == elevator and 0 in generators)
        ):
            return False
    return True


def parse(data):
    gadgets = defaultdict(dict)
    for i, line in enumerate(data.splitlines(), 1):
        generators = [(g, "g") for g in re.findall(r"(\w+) generator", line)]
        microchips = [(m, "m") for m in re.findall(r"(\w+)-compatible", line)]
        for name, type in generators + microchips:
            gadgets[name][type] = i

    generators = []
    microchips = []
    for _, items in gadgets.items():
        generators.append(items["g"])
        microchips.append(items["m"])
    return generators, microchips


def solve(generators, microchips):
    elevator = 1
    debug(elevator, generators, microchips)

    history = set()

    heap = []
    heapq.heappush(heap, (0, 0, elevator, generators, microchips, []))
    while heap:
        steps, moves, elevator, generators, microchips, rec = heapq.heappop(heap)

        state = (elevator, tuple(sorted(zip(generators, microchips))))
        if state in history:
            continue
        history.add(state)

        if DEBUG:
            rec.append((steps, moves, elevator, generators, microchips))

        if all(x == 4 for x in generators + microchips):
            debug2(rec)
            return steps

        if not is_valid(elevator, generators, microchips):
            continue

        elevator_count = sum(x == 0 for x in generators + microchips)
        if elevator_count > 0:
            if elevator < 4:
                gen_copy = generators.copy()
                mic_copy = microchips.copy()
                rec = rec.copy()
                heapq.heappush(
                    heap, (steps + 1, moves + 1, elevator + 1, gen_copy, mic_copy, rec)
                )
            if elevator > 1:
                gen_copy = generators.copy()
                mic_copy = microchips.copy()
                rec = rec.copy()
                heapq.heappush(
                    heap, (steps + 1, moves + 1, elevator - 1, gen_copy, mic_copy, rec)
                )

        for i in range(len(generators)):
            gen_copy = generators.copy()
            mic_copy = microchips.copy()
            rec = rec.copy()
            if gen_copy[i] == elevator and elevator_count < 2:
                gen_copy[i] = 0
                heapq.heappush(
                    heap, (steps, moves + 1, elevator, gen_copy, mic_copy, rec)
                )
            elif gen_copy[i] == 0:
                gen_copy[i] = elevator
                heapq.heappush(
                    heap, (steps, moves + 1, elevator, gen_copy, mic_copy, rec)
                )

        for i in range(len(microchips)):
            gen_copy = generators.copy()
            mic_copy = microchips.copy()
            rec = rec.copy()
            if mic_copy[i] == elevator and elevator_count < 2:
                mic_copy[i] = 0
                heapq.heappush(
                    heap, (steps, moves + 1, elevator, gen_copy, mic_copy, rec)
                )
            elif mic_copy[i] == 0:
                mic_copy[i] = elevator
                heapq.heappush(
                    heap, (steps, moves + 1, elevator, gen_copy, mic_copy, rec)
                )


def part1(generators, microchips):
    return solve(generators, microchips)


def part2(generators, microchips):
    return solve(generators + [1, 1], microchips + [1, 1])


TEST_DATA = {}
TEST_DATA[
    """\
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
""".rstrip()
] = (11, None)
