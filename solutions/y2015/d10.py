from itertools import groupby


def look_and_say(seq):
    return "".join(str(len(list(g))) + k for k, g in groupby(seq))


def parse(data):
    return data.strip()


def parts(data):
    for _ in range(40):
        data = look_and_say(data)
    ans_1 = len(data)

    for _ in range(10):
        data = look_and_say(data)
    ans_2 = len(data)

    return ans_1, ans_2


TEST_DATA = {}
