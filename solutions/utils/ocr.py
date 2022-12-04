ALPHABET = {
    ".##.\n#..#\n#..#\n####\n#..#\n#..#": "A",
    "###.\n#..#\n###.\n#..#\n#..#\n###.": "B",
    ".##.\n#..#\n#...\n#...\n#..#\n.##.": "C",
    "####\n#...\n###.\n#...\n#...\n####": "E",
    "####\n#...\n###.\n#...\n#...\n#...": "F",
    ".##.\n#..#\n#...\n#.##\n#..#\n.###": "G",
    "#..#\n#..#\n####\n#..#\n#..#\n#..#": "H",
    "###.\n.#..\n.#..\n.#..\n.#..\n###.": "I",
    "..##\n...#\n...#\n...#\n#..#\n.##.": "J",
    "#..#\n#.#.\n##..\n#.#.\n#.#.\n#..#": "K",
    "#...\n#...\n#...\n#...\n#...\n####": "L",
    ".##.\n#..#\n#..#\n#..#\n#..#\n.##.": "O",
    "###.\n#..#\n#..#\n###.\n#...\n#...": "P",
    "###.\n#..#\n#..#\n###.\n#.#.\n#..#": "R",
    ".###\n#...\n#...\n.##.\n...#\n###.": "S",
    "#..#\n#..#\n#..#\n#..#\n#..#\n.##.": "U",
    "#...\n#...\n.#.#\n..#.\n..#.\n..#.": "Y",
    "####\n...#\n..#.\n.#..\n#...\n####": "Z",
}

FILL = "#"
EMPTY = "."
WIDTH = 4
HEIGHT = 6


def parse(drawing):
    lines = drawing.splitlines()
    if len(lines) != HEIGHT:
        return None
    length = len(lines[0])
    if not all(map(lambda line: len(line) == length, lines)):
        return None

    result = ""

    index = 0
    while length - index >= WIDTH:
        skip = all(map(lambda line: line[index] == EMPTY, lines))
        if skip:
            index += 1
            continue
        letter = "\n".join(map(lambda line: line[index : index + WIDTH], lines))
        letter = ALPHABET[letter]

        result += letter
        index += 5 if letter == "Y" else 4

    return result
