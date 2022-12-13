def dfs(path, links, canRevis):
    if path[-1] == "end":
        return 1
    if path[-1] == "start" and len(path) > 1:
        return 0

    res = 0

    for n in links[path[-1]]:
        revis = any(c for c in n if c.islower()) and n in path
        if revis and not canRevis:
            continue
        res += dfs(path + [n], links, canRevis and not revis)

    return res


def parse(data):
    links = {}
    for line in data.splitlines():
        a, b = line.strip().split("-")
        links[a] = links.get(a, []) + [b]
        links[b] = links.get(b, []) + [a]
    return links


def part1(links):
    return dfs(["start"], links, False)


def part2(links):
    return dfs(["start"], links, True)


TEST_DATA = {}
TEST_DATA[
    """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".rstrip()
] = (10, 36)
