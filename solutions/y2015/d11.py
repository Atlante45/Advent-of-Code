from itertools import groupby
from more_itertools import triplewise


def is_valid(passw):
    if "i" in passw or "o" in passw or "l" in passw:
        return False

    groups = (len(list(g)) for _, g in groupby(passw))
    if len(list(filter(lambda n: n == 2, groups))) != 2:
        return False

    return any(
        filter(
            lambda a: a[1] == a[0] + 1 and a[1] == a[2] - 1, triplewise(map(ord, passw))
        )
    )


def next_ch(ch):
    if ch == "z":
        return "a"
    if ch == "h":
        return "j"
    if ch == "n":
        return "p"
    if ch == "k":
        return "m"
    return chr(ord(ch) + 1)


def next(passw):
    override = False
    for i, ch in enumerate(passw):
        if override:
            passw[i] = "a"
        elif ch in ["i", "o", "l"]:
            passw[i] = next_ch(ch)
            override = True

    if override:
        return passw

    for i in reversed(range(len(passw))):
        if passw[i] == "z":
            passw[i] = "a"
            continue
        else:
            passw[i] = next_ch(passw[i])
            break
    return passw


def next_valid(passw):
    passw = next(list(passw))
    while not is_valid(passw):
        passw = next(passw)

    return "".join(passw)


def parse(data):
    return data.strip()


def parts(data):
    ans_1 = next_valid(data)
    ans_2 = next_valid(ans_1)
    return ans_1, ans_2


TEST_DATA = {}
TEST_DATA[
    """\
ghijklmn
""".rstrip()
] = ("ghjaabcc", "ghjbbcdd")
