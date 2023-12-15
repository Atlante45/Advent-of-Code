from functools import cache
import re

from solutions.utils.graph import dijkstra


REGEX = re.compile(r"^Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.+)$")


def parse(data):
    valves = {}
    tunnels = {}
    for line in data.splitlines():
        v, f, t = REGEX.search(line).groups()
        valves[v] = int(f)
        tunnels[v] = t.split(", ")

    edges = {}

    def neighbors(valve):
        return tunnels[valve]

    for valve in valves:
        _, cost_so_far = dijkstra(valve, neighbors)
        for dest, cost in cost_so_far.items():
            edges[(valve, dest)] = cost

    return valves, edges


def part1(valves, edges):
    candidates = [valve for valve, flow in valves.items() if flow > 0]

    @cache
    def visit(visited, pos, time_left):
        if time_left == 0:
            return (0, ())

        res = max(
            (
                visit(visited + (v,), v, time_left - edges[(pos, v)] - 1)
                for v in candidates
                if v not in visited and edges[(pos, v)] + 1 <= time_left
            ),
            key=lambda x: x[0],
            default=(0, ()),
        )

        return valves[pos] * time_left + res[0], res[1]

    return visit((), "AA", 30)[0]


def part2(valves, edges):
    candidates = [valve for valve, flow in valves.items() if flow > 0]

    @cache
    def visit(pos, visited, time_left):
        if time_left == 0:
            return (0, ())

        res = max(
            (
                visit(v, visited + (v,), time_left - edges[(pos, v)] - 1)
                for v in candidates
                if v not in visited and edges[(pos, v)] + 1 <= time_left
            ),
            key=lambda x: x[0],
            default=(0, ()),
        )

        return valves[pos] * time_left + res[0], res[1]

    flow, visited = visit("AA", (), 26)
    flow2, _ = visit(visited, "AA", 26)
    return flow + flow2

    # @cache
    # def visit(pos1, pos2, visited, time_left1, time_left2):
    #     if time_left1 == 0 and time_left2 == 0:
    #         return 0

    #     res1 = 0
    #     res2 = 0
    #     if time_left1 > time_left2:
    #         res1 = max(
    #             (
    #                 visit(
    #                     v,
    #                     pos2,
    #                     visited + (v,),
    #                     time_left1 - edges[(pos1, v)] - 1,
    #                     time_left2,
    #                 )
    #                 for v in candidates
    #                 if v not in visited and edges[(pos1, v)] + 1 <= time_left1
    #             ),
    #             default=0,
    #         )
    #     else:
    #         res2 = max(
    #             (
    #                 visit(
    #                     pos1,
    #                     v,
    #                     visited + (v,),
    #                     time_left1,
    #                     time_left2 - edges[(pos2, v)] - 1,
    #                 )
    #                 for v in candidates
    #                 if v not in visited and edges[(pos2, v)] + 1 <= time_left2
    #             ),
    #             default=0,
    #         )

    #     return max(valves[pos1] * time_left1 + res1, valves[pos2] * time_left2 + res2)

    # return visit("AA", "AA", (), 26, 26)


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
] = (1651, 1707)
