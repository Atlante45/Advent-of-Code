from more_itertools import sliding_window


def has_abba(s):
    for a, b, c, d in sliding_window(s, 4):
        if a == d and b == c and a != b:
            return True
    return False


def parse(data):
    ips = []
    for ip in data.splitlines():
        starts = [i for i, c in enumerate(ip) if c == "["]
        ends = [i for i, c in enumerate(ip) if c == "]"]
        hypernets = [ip[a + 1 : b] for a, b in zip(starts, ends)]
        supernets = [ip[a + 1 : b] for a, b in zip([-1] + ends, starts + [len(ip)])]
        ips.append((supernets, hypernets))
    return ips


def supports_tls(ip):
    supernets, hypernets = ip
    if any(has_abba(s) for s in hypernets):
        return False
    return any(has_abba(s) for s in supernets)


def supports_ssl(ip):
    supernets, hypernets = ip
    for supernet in supernets:
        for a, b, c in sliding_window(supernet, 3):
            if a == c and a != b:
                bab = "".join([b, a, b])
                for hypernet in hypernets:
                    if bab in hypernet:
                        return True
    return False


def part1(ips):
    return sum(1 for ip in ips if supports_tls(ip))


def part2(ips):
    return sum(1 for ip in ips if supports_ssl(ip))


TEST_DATA = {}
TEST_DATA[
    """\
abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
"""
] = (2, None)
