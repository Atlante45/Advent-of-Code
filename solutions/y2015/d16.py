SAMPLE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse(data):
    return data.splitlines()


def part1(lines):
    for i, line in enumerate(lines):
        line = line[line.index(":") + 1 :]
        matches = True
        for item in line.split(", "):
            name, val = item.split(": ")
            if SAMPLE[name.strip()] != int(val):
                matches = False
                break
        if matches:
            return i + 1


def part2(lines):
    for i, line in enumerate(lines):
        line = line[line.index(":") + 1 :]
        matches = True
        for item in line.split(", "):
            name, val = item.split(": ")
            name = name.strip()
            if name in ["cats", "trees"]:
                if SAMPLE[name] >= int(val):
                    matches = False
                    break
            elif name in ["pomeranians", "goldfish"]:
                if SAMPLE[name] <= int(val):
                    matches = False
                    break
            else:
                if SAMPLE[name] != int(val):
                    matches = False
                    break
        if matches:
            return i + 1


TEST_DATA = {}
