from itertools import count
from queue import PriorityQueue
from solutions.utils.graph import neighbors4


def parse(data):
    lines = data.splitlines()
    cave = set()
    goblins = set()
    elves = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "G":
                goblins.add((x, y))
            elif c == "E":
                elves.add((x, y))

            if c != "#":
                cave.add((x, y))

    return cave, goblins, elves


def render(cave, goblins, elves, width, height, unit=None, path=None):
    render = ""
    for y in range(height):
        for x in range(width):
            if (x, y) == unit:
                render += "\033[34m@\033[0m"
            elif (x, y) in goblins:
                render += "\033[32mG\033[0m"
            elif (x, y) in elves:
                render += "\033[33mE\033[0m"
            elif path and (x, y) in path:
                render += "\033[34m*\033[0m"
            elif (x, y) in cave:
                render += " "
            else:
                render += "\033[31m#\033[0m"
        render += "\n"
    return render


# Modified Dijkstra biased towards lower y values and x values
# Stops when it finds a target
def dijkstra(start, targets, neighbors):
    frontier = PriorityQueue()
    came_from = {}
    cost_so_far = {}

    frontier.put((0, start[1], start[0]))
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        cost, y, x = frontier.get()

        for nx, ny in neighbors((x, y)):
            new_cost = cost + 1
            if (nx, ny) not in cost_so_far:
                cost_so_far[(nx, ny)] = new_cost
                came_from[(nx, ny)] = (x, y)
                frontier.put((new_cost, ny, nx))

            if (nx, ny) in targets:
                return (x, y), came_from

    return None, None


def pathfind(cave, unit, targets, other_units):
    free_cells = cave - other_units

    def neighbors(n):
        return [n for n in neighbors4(*n) if n in free_cells]

    next, came_from = dijkstra(unit, targets, neighbors)

    if next is None or next == unit:
        return None

    while came_from[next] != unit:
        next = came_from[next]

    return next


def part1(cave, goblins, elves):
    hp = {}
    for goblin in goblins:
        hp[goblin] = 200

    for elf in elves:
        hp[elf] = 200

    for turn in count(1):
        units = sorted(goblins | elves, key=lambda u: (-u[1], -u[0]))
        while units:
            unit = units.pop()
            if unit in goblins:
                friends = goblins
                targets = elves
            else:
                friends = elves
                targets = goblins

            move_to = pathfind(cave, unit, targets, friends)
            if move_to:
                friends.remove(unit)
                friends.add(move_to)
                hp[move_to] = hp[unit]
                hp.pop(unit)
                unit = move_to

            targets = [t for t in neighbors4(*unit) if t in targets]
            if not targets:
                continue

            target = min(targets, key=lambda t: (hp[t], t[1], t[0]))
            hp[target] -= 3
            if hp[target] <= 0:
                hp.pop(target)
                if target in units:
                    units.remove(target)
                if target in goblins:
                    goblins.remove(target)
                else:
                    elves.remove(target)

            if not elves or not goblins:
                if len(units) > 0:
                    turn -= 1
                return turn * sum(hp.values())


def simulate(cave, goblins, elves, elf_power):
    hp = {}
    for goblin in goblins:
        hp[goblin] = 200

    for elf in elves:
        hp[elf] = 200

    for turn in count(1):
        units = sorted(goblins | elves, key=lambda u: (-u[1], -u[0]))
        while units:
            unit = units.pop()
            if unit in goblins:
                friends = goblins
                targets = elves
            else:
                friends = elves
                targets = goblins

            move_to = pathfind(cave, unit, targets, friends)
            if move_to:
                friends.remove(unit)
                friends.add(move_to)
                hp[move_to] = hp[unit]
                hp.pop(unit)
                unit = move_to

            targets = [t for t in neighbors4(*unit) if t in targets]
            if not targets:
                continue

            target = min(targets, key=lambda t: (hp[t], t[1], t[0]))
            hp[target] -= 3 if unit in goblins else elf_power
            if hp[target] <= 0:
                hp.pop(target)
                if target in units:
                    units.remove(target)
                if target in goblins:
                    goblins.remove(target)
                else:
                    return None

            if not goblins:
                if len(units) > 0:
                    turn -= 1
                return turn * sum(v for k, v in hp.items() if k in elves)


def part2(cave, goblins, elves):
    for power in count(4):
        sim = simulate(cave, goblins.copy(), elves.copy(), power)
        if sim is not None:
            return sim


TEST_DATA = {}
TEST_DATA[
    """\
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
""".rstrip()
] = (27730, None)
TEST_DATA[
    """\
#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
""".rstrip()
] = (36334, None)
TEST_DATA[
    """\
#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######
""".rstrip()
] = (39514, None)
TEST_DATA[
    """\
#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######
""".rstrip()
] = (27755, None)
TEST_DATA[
    """\
#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######
""".rstrip()
] = (28944, None)
TEST_DATA[
    """\
#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########
""".rstrip()
] = (18740, None)
