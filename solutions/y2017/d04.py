def parse(data):
    return data.splitlines()


def is_valid(passphrase):
    words = passphrase.split()
    return len(words) == len(set(words))


def is_valid2(passphrase):
    words = [tuple(sorted(word)) for word in passphrase.split()]
    return len(words) == len(set(words))


def part1(lines):
    return sum(1 for line in lines if is_valid(line))


def part2(lines):
    return sum(1 for line in lines if is_valid2(line))


TEST_DATA = {}
# TEST_DATA[
#     """\

# """.rstrip()
# ] = (None, None)
