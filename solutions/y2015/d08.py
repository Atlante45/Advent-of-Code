import re

REGEX = r"(\\\\|\\\"|\\x[0-9A-Fa-f]{2})"


def parse(data):
    return data


def part1(data):
    file_chars = sum(len(line) for line in data.splitlines())
    data = re.sub(REGEX, ".", data)
    disk_chars = sum(len(line) - 2 for line in data.splitlines())

    return file_chars - disk_chars


def part2(data):
    file_chars = sum(len(line) for line in data.splitlines())
    expanded_chars = sum(
        len(line) + line.count('"') + line.count("\\") + 2 for line in data.splitlines()
    )
    return expanded_chars - file_chars


TEST_DATA = {}
TEST_DATA[
    """\
""
"abc"
"aaa\\"aaa"
"\\x27"
""".rstrip()
] = (12, 19)
