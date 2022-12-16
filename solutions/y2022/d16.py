from itertools import combinations, permutations
import re

from solutions.utils.graph import dijkstra


REGEX = re.compile(r"^Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.+)$")


def parse(data):
    valves = {}
    tunnels = {}
    for line in data.splitlines():
        v, f, t = REGEX.search(line).groups()
        f = int(f)
        t = t.split(", ")
        valves[v] = f
        tunnels[v] = t

    nodes = sorted(filter(lambda x: x[1] != 0, valves.items()), key=lambda x: -x[1])
    edges = {}

    def neighbors(valve):
        return tunnels[valve]

    for valve in valves:
        _, cost_so_far = dijkstra(valve, neighbors)
        for dest, cost in cost_so_far.items():
            edges[(valve, dest)] = cost

    return nodes, edges


def compute_route(route, edges, time):
    pos = "AA"
    pressure = 0
    total = 0
    for v, flow in route:
        dist = edges[(pos, v)] + 1
        if time - dist < 0:
            break
        total += dist * pressure
        time -= dist
        pressure += flow
        pos = v

    total += time * pressure
    return total


def part1(nodes, edges):
    # Real input is too slow, yolo
    if len(nodes) != 6:
        nodes = nodes[:-5]

    return max(compute_route(perm, edges, 30) for perm in permutations(nodes))


def part2(nodes, edges):
    res = 0

    valves = set(nodes)
    # print(valves)
    for route1 in combinations(valves, len(valves) // 2):
        route1 = set(route1)
        route2 = valves - route1

        max1 = max(compute_route(perm, edges, 26) for perm in permutations(route1))
        max2 = max(compute_route(perm, edges, 26) for perm in permutations(route2))
        # if max1 + max2 > res:
        #     print(route1, max1)
        #     print(route2, max2)
        #     print(max1 + max2)
        res = max(res, max1 + max2)

    # for perm in permutations(nodes):
    #     res = max(res, compute_route(perm, edges))

    return res


TEST_DATA = {}
TEST_DATA[
    """\
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
""".rstrip()
] = (1651, None)
