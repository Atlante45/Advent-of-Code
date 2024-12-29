from collections import defaultdict


def parse(data):
    bags = defaultdict(list)
    ibags = defaultdict(list)

    for line in data.splitlines():
        bag, contents = line.split(" bags contain ")
        contents = contents[:-1].split(", ")
        for content in contents:
            if content == "no other bags":
                continue
            content = content.split()
            count = int(content[0])
            color = " ".join(content[1:-1])
            bags[bag].append((count, color))
            ibags[color].append(bag)
    return bags, ibags


def part1(bags, ibags):
    edge = ["shiny gold"]
    visited = set()

    while edge:
        bag = edge.pop()
        visited.add(bag)
        for color in ibags[bag]:
            if color not in visited:
                edge.append(color)
    return len(visited) - 1


def part2(bags, ibags):
    edge = defaultdict(int)
    edge["shiny gold"] = 1

    res = 0
    while edge:
        bag, count = edge.popitem()
        res += count
        for c, color in bags[bag]:
            edge[color] += count * c
    return res - 1


TEST_DATA = {}
TEST_DATA[
    """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".rstrip()
] = (4, 32)
