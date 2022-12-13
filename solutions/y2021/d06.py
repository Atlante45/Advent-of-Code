def count(input, gens):
    ageCounts = [0] * 9
    for i in range(9):
        ageCounts[i] = input.count(i)

    for _ in range(gens):
        replicatingFish = ageCounts.pop(0)
        ageCounts[6] += replicatingFish
        ageCounts.append(replicatingFish)

    return sum(ageCounts)


def parse(data):
    return [int(v) for v in data.strip().split(",")]


def part1(ages):
    return count(ages, 80)


def part2(ages):
    return count(ages, 256)


TEST_DATA = {}
TEST_DATA[
    """\
3,4,3,1,2
""".rstrip()
] = (5934, 26984457539)
