def scramble(data, lines):
    start = list(data)

    for line in lines:
        if line.startswith("swap position"):
            a, _, _, b = line.split(" ")[2:]
            tmp = start[int(a)]
            start[int(a)] = start[int(b)]
            start[int(b)] = tmp
        elif line.startswith("swap letter"):
            a, _, _, b = line.split(" ")[2:]
            a = start.index(a)
            b = start.index(b)
            tmp = start[a]
            start[a] = start[b]
            start[b] = tmp
        elif line.startswith("rotate left"):
            a = line.split()[-2]
            start = start[int(a) :] + start[: int(a)]
        elif line.startswith("rotate right"):
            a = line.split()[-2]
            start = start[-int(a) :] + start[: -int(a)]
        elif line.startswith("rotate based"):
            a = line.split()[-1]
            a = (start.index(a) + 1 + (start.index(a) >= 4)) % len(start)
            start = start[-a:] + start[:-a]
        elif line.startswith("reverse"):
            a, _, b = line.split(" ")[2:]
            start = (
                start[: int(a)]
                + list(reversed(start[int(a) : int(b) + 1]))
                + start[int(b) + 1 :]
            )
        elif line.startswith("move"):
            a, _, _, b = line.split(" ")[2:]
            tmp = start.pop(int(a))
            start.insert(int(b), tmp)
        else:
            raise ValueError(line)
    return "".join(start)


def unscramble(data, lines):
    start = list(data)

    for line in reversed(lines):
        if line.startswith("swap position"):
            a, _, _, b = line.split(" ")[2:]
            tmp = start[int(a)]
            start[int(a)] = start[int(b)]
            start[int(b)] = tmp
        elif line.startswith("swap letter"):
            a, _, _, b = line.split(" ")[2:]
            a = start.index(a)
            b = start.index(b)
            tmp = start[a]
            start[a] = start[b]
            start[b] = tmp
        elif line.startswith("rotate left"):
            a = line.split()[-2]
            start = start[-int(a) :] + start[: -int(a)]
        elif line.startswith("rotate right"):
            a = line.split()[-2]
            start = start[int(a) :] + start[: int(a)]
        elif line.startswith("rotate based"):
            a = line.split()[-1]
            a = start.index(a)
            if a % 2 == 1:
                a //= 2
            elif a == 0:
                a = 7
            else:
                a = (a + 8) // 2 - 1
            a = (a + 1 + (a >= 4)) % len(start)
            start = start[a:] + start[:a]
        elif line.startswith("reverse"):
            a, _, b = line.split(" ")[2:]
            start = (
                start[: int(a)]
                + list(reversed(start[int(a) : int(b) + 1]))
                + start[int(b) + 1 :]
            )
        elif line.startswith("move"):
            a, _, _, b = line.split(" ")[2:]
            tmp = start.pop(int(b))
            start.insert(int(a), tmp)
        else:
            raise ValueError(line)
    return "".join(start)


def parse(data):
    return [line for line in data.splitlines()]


def part1(lines):
    start = "abcdefgh" if len(lines) > 10 else "abcde"
    return scramble(start, lines)


def part2(lines):
    start = "fbgdceah" if len(lines) > 10 else "decab"
    return unscramble(start, lines)


TEST_DATA = {}
TEST_DATA[
    """\
swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
""".rstrip()
] = ("decab", None)


# a0000000
# 0a000000

# 0a000000
# 000a0000

# 00a00000
# 00000a00

# 000a0000
# 0000000a

# 0000a000
# 00a00000

# 00000a00
# 0000a000

# 000000a0
# 000000a0

# 0000000a
# a0000000
