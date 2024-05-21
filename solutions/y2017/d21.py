START = [".#.", "..#", "###"]


def transforms(pattern):
    patterns = [pattern]

    pattern = pattern.split("/")
    patterns.append("/".join(["".join(row) for row in zip(*pattern)][::-1]))
    patterns.append("/".join("".join(row[::-1]) for row in pattern[::-1]))
    patterns.append("/".join("".join(row) for row in zip(*pattern[::-1])))

    flipped = [row[::-1] for row in pattern]
    patterns.append("/".join(flipped))
    patterns.append("/".join(["".join(row) for row in zip(*flipped)][::-1]))
    patterns.append("/".join("".join(row[::-1]) for row in flipped[::-1]))
    patterns.append("/".join("".join(row) for row in zip(*flipped[::-1])))

    return patterns


def parse(data):
    mappings = {}
    for line in data.splitlines():
        pattern, replacement = line.split(" => ")
        for t in transforms(pattern):
            mappings[t] = replacement
    return mappings


def step(state, mappings):
    new_state = []
    size = len(state)

    if size % 2 == 0:
        step = 2
    else:
        step = 3

    for y in range(0, size, step):
        new_rows = [""] * (step + 1)
        for x in range(0, size, step):
            pattern = [state[y + dy][x : x + step] for dy in range(step)]
            replacement = mappings["/".join(pattern)]
            replacement = replacement.split("/")
            for dy, row in enumerate(replacement):
                new_rows[dy] += row
        new_state.extend(new_rows)

    return new_state


def parts(mappings):
    part1 = part2 = None

    state = START
    for i in range(18):
        state = step(state, mappings)

        if i == 4:
            part1 = sum(row.count("#") for row in state)
    part2 = sum(row.count("#") for row in state)

    return part1, part2


TEST_DATA = {}
