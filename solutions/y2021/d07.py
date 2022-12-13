def computeCost(pos, fuelCost):
    minCost = None
    for i in range(min(pos), max(pos) + 1):
        cost = sum([fuelCost(abs(i - n)) for n in pos])
        if minCost and cost > minCost:
            return minCost
        minCost = cost


def parse(data):
    return [int(v) for v in data.strip().split(",")]


def part1(pos):
    return computeCost(pos, lambda n: n)


def part2(pos):
    return computeCost(pos, lambda n: int((n * (n + 1)) / 2))


TEST_DATA = {}
TEST_DATA[
    """\
16,1,2,0,4,2,7,1,2,14
""".rstrip()
] = (37, 168)
