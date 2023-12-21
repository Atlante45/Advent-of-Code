from hashlib import md5
from itertools import count


def parse(data):
    return data


def part1(door_id):
    password = ""
    for i in count():
        hash = md5((door_id + str(i)).encode()).hexdigest()
        if hash.startswith("00000"):
            password += hash[5]
            if len(password) == 8:
                return password


def part2(door_id):
    password = [None] * 8
    for i in count():
        hash = md5((door_id + str(i)).encode()).hexdigest()
        if hash.startswith("00000") and hash[5].isdigit():
            pos = int(hash[5])
            if pos >= 8 or password[pos] is not None:
                continue
            password[pos] = hash[6]
            if all(x is not None for x in password):
                return "".join(password)


TEST_DATA = {}
TEST_DATA[
    """\
abc
""".rstrip()
] = ("18f47a30", "05ace8e3")
