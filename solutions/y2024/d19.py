from functools import cache


def parse(data):
    patterns, designs = data.split("\n\n")
    patterns = tuple(patterns.split(", "))
    designs = designs.splitlines()

    return patterns, designs


@cache
def count_ways(design, patterns):
    if not design:
        return 1

    return sum(
        count_ways(design[len(pattern) :], patterns)
        for pattern in patterns
        if design.startswith(pattern)
    )


def parts(patterns, designs):
    designs = [count_ways(design, patterns) for design in designs]
    return sum(1 for design in designs if design > 0), sum(designs)


TEST_DATA = {}
TEST_DATA[
    """\
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".rstrip()
] = (6, 16)
