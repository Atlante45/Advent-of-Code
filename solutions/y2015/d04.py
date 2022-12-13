import hashlib
from itertools import count


def find(input, prefix, start):
    for i in count(start):
        secret = input + str(i)
        if hashlib.md5(secret.encode()).hexdigest().startswith(prefix):
            return i


def parse(data):
    return data.strip()


def parts(data):
    ans_1 = find(data, "00000", 1)
    ans_2 = find(data, "000000", ans_1)
    return ans_1, ans_2


TEST_DATA = {}
TEST_DATA[
    """\
abcdef
""".rstrip()
] = (609043, 6742839)
