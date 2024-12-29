from functools import cache
from solutions.utils.graph import neighbors8


def parse(data):
    seats = set()
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == "L":
                seats.add((x, y))
            else:
                assert c == "."
    return seats


def solve(seats, neighbors, max_occupied):
    occupied = set()
    while True:
        new_occupied = set()
        for seat in seats:
            n = sum(1 for n in neighbors(*seat) if n in occupied)
            if seat not in occupied and n == 0:
                new_occupied.add(seat)
            elif seat in occupied and n < max_occupied:
                new_occupied.add(seat)
        if new_occupied == occupied:
            return len(occupied)
        occupied = new_occupied


def part1(seats):
    return solve(seats, neighbors8, 4)


D = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def part2(seats):
    max_x = max(x for x, _ in seats)
    max_y = max(y for _, y in seats)

    @cache
    def neighbors(x, y):
        ns = []
        for dx, dy in D:
            nx, ny = x + dx, y + dy
            while 0 <= nx <= max_x and 0 <= ny <= max_y and (nx, ny) not in seats:
                nx, ny = nx + dx, ny + dy
            if (nx, ny) in seats:
                ns.append((nx, ny))
        return ns

    return solve(seats, neighbors, 5)


TEST_DATA = {}
TEST_DATA[
    """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".rstrip()
] = (37, 26)
