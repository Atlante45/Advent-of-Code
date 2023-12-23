from solutions.utils.graph import a_star, neighbors4


def parse(data):
    return int(data)


def part1(number):
    def is_wall(x, y):
        return bin(x * x + 3 * x + 2 * x * y + y + y * y + number).count("1") % 2 == 1

    def neighbors(p):
        return [n for n in neighbors4(*p, 100000) if not is_wall(*n)]

    goal = (7, 4) if number == 10 else (31, 39)
    _, cost_so_far = a_star((1, 1), goal, neighbors)
    return cost_so_far[goal]


def part2(number):
    def is_wall(x, y):
        return bin(x * x + 3 * x + 2 * x * y + y + y * y + number).count("1") % 2 == 1

    def neighbors(p):
        return [n for n in neighbors4(*p, 100000) if not is_wall(*n)]

    visited = set()
    frontier = [(1, 1)]
    for _ in range(50):
        new_frontier = []
        for p in frontier:
            visited.add(p)
            new_frontier.extend(n for n in neighbors(p) if n not in visited)
        frontier = new_frontier
    visited |= set(frontier)
    return len(visited)


TEST_DATA = {}
TEST_DATA[
    """\
10
""".rstrip()
] = (11, None)
