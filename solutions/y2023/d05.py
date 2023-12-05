from cmath import inf

from more_itertools import batched


def parse(data):
    lines = data.splitlines()

    category = lines[0].split(":")[0]
    seeds = list(map(int, lines[0].split(":")[1].split()))
    # print(category, seeds)

    mappings = {}
    source = None
    dest = None
    ranges = []
    for line in lines[2:]:
        if line.endswith("map:"):
            source, dest = line.split()[0].split("-to-")
        elif line == "":
            mappings[source] = {"dest": dest, "ranges": ranges}
            ranges = []
        else:
            ranges += [list(map(int, line.split()))]

    mappings[source] = {"dest": dest, "ranges": ranges}

    # print(mappings)
    return "seed", seeds, mappings


def part1(category, seeds, mappings):
    while category != "location":
        # print(category)
        # print(seeds)
        # print(mappings[category]["ranges"])
        things = []
        mapping = mappings[category]

        for v in seeds:
            new_v = None
            for d, s, l in mapping["ranges"]:
                if v >= s and v < s + l:
                    new_v = v - s + d
                    break

            if new_v is None:
                new_v = v

            things.append(new_v)

        category = mapping["dest"]
        seeds = things

    return min(seeds)


def part2(category, seeds, mappings):
    seeds = list(batched(seeds, 2))

    sum = 0
    for _, l in seeds:
        sum += l

    while category != "location":
        # print(category)
        # print(seeds)
        # print(mappings[category]["ranges"])
        things = []
        mapping = mappings[category]

        while len(seeds) > 0:
            start, length = seeds[0]
            seeds = seeds[1:]
            new_v = None
            for d, s, l in mapping["ranges"]:
                if start >= s and start + length <= s + l:
                    new_v = [(d + (start - s), length)]
                    break
                elif s > start and s + l < start + length:
                    new_v = [(d, l)]
                    seeds += [
                        (start, s - start),
                        (s + l, start + length - (s + l)),
                    ]
                    assert (s - start) + (l) + (start + length - (s + l)) == length
                    assert s - start > 0
                    assert start + length - (s + l) > 0
                    break
                elif start >= s and start < s + l:
                    new_length = l - (start - s)
                    new_v = [(d + (start - s), new_length)]
                    seeds += [(start + new_length, length - new_length)]
                    assert new_length > 0
                    break
                elif start + length > s and start + length <= s + l:
                    new_length = length - (s - start)
                    new_v = [(d, new_length)]
                    seeds += [(start, length - new_length)]
                    assert new_length > 0
                    break
                else:
                    assert start + length <= s or start >= s + l

            if new_v is None:
                new_v = [(start, length)]

            things += new_v

        # print(things, category, mapping["dest"])
        category = mapping["dest"]
        seeds = things

    min_v = inf
    for s, l in seeds:
        min_v = min(min_v, s)
        sum -= l

    # print(min_v)
    return min_v


TEST_DATA = {}
TEST_DATA[
    """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".rstrip()
] = (35, 46)
