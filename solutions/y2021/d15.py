from solutions.utils.graph import a_star, neighbors4


def parse(data):
    input = []
    for line in data.splitlines():
        input.append([int(v) for v in line.strip()])
    return input


def part1(input):
    size = len(input)
    start = (0, 0)
    end = (size - 1, size - 1)

    def neighbors(n):
        i, j = n
        return neighbors4(i, j, input)

    def cost(_, n):
        i, j = n
        return input[i][j]

    _, cost_so_far = a_star(start, end, neighbors, cost)
    return cost_so_far[end]


def part2(input):
    size = len(input)
    start = (0, 0)
    end = (5 * size - 1, 5 * size - 1)

    def neighbors(n):
        i, j = n
        return neighbors4(i, j, 5 * size, 5 * size)

    def cost(_, n):
        i, j = n
        return (input[i % size][j % size] + i // size + j // size - 1) % 9 + 1

    _, cost_so_far = a_star(start, end, neighbors, cost)
    return cost_so_far[end]


TEST_DATA = {}
TEST_DATA[
    """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".rstrip()
] = (40, 315)
