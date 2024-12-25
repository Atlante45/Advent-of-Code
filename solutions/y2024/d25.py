def parse(data):
    keys = []
    locks = []
    for item in data.split("\n\n"):
        sig = [line.count("#") for line in zip(*item.splitlines())]

        if item[0] == "#":
            locks.append(sig)
        else:
            keys.append(sig)
    return keys, locks


def part1(keys, locks):
    return sum(
        all(a + b <= 7 for a, b in zip(key, lock)) for key in keys for lock in locks
    )


def part2(keys, locks):
    pass


TEST_DATA = {}
TEST_DATA[
    """\
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
""".rstrip()
] = (3, None)
