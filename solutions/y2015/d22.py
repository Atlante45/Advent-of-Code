import copy
import heapq

SPELLS = [
    (53, 4, 0, 0, 0, 0),
    (73, 2, 2, 0, 0, 0),
    (113, 0, 0, 7, 0, 6),
    (173, 3, 0, 0, 0, 6),
    (229, 0, 0, 0, 101, 5),
]


def parse(data):
    return [int(line.split()[-1]) for line in data.splitlines()]


def turn(s, cost, bhp, bdmg, php, pmana, effects, hard_mode):
    spell = SPELLS[s]
    if spell[0] > pmana or s in [e for e, _ in effects]:
        return False, None

    # Player turn
    if spell[5] > 0:
        effects += [(s, spell[5])]
    else:
        bhp -= spell[1]
        php += spell[2]
    pmana -= spell[0]
    cost += spell[0]

    # Boss turn effects
    effects_sum = (
        [sum(v) for v in zip(*[SPELLS[e] for e, _ in effects])]
        if len(effects) > 0
        else [0] * 6
    )
    bhp -= effects_sum[1]
    parmor = effects_sum[3]
    pmana += effects_sum[4]
    effects = [(e, t - 1) for e, t in effects if t > 1]

    if bhp <= 0:
        return True, cost

    # Boss turn
    php -= max(1, bdmg - parmor)

    if hard_mode:
        php -= 1

    if php <= 0:
        return False, None

    # Player turn effects
    effects_sum = (
        [sum(v) for v in zip(*[SPELLS[e] for e, _ in effects])]
        if len(effects) > 0
        else [0] * 6
    )
    effects = [(e, t - 1) for e, t in effects if t > 1]

    bhp -= effects_sum[1]
    pmana += effects_sum[4]

    if bhp <= 0:
        return True, cost

    return None, (cost, bhp, bdmg, php, pmana, effects)


def simulate(boss, hard_mode):
    # cost, bhp, bdmg, php, pmana, effects
    state = (0, boss[0], boss[1], 50, 500, [])
    if hard_mode:
        state = (0, boss[0], boss[1], 50 - 1, 500, [])

    heap = []
    heapq.heappush(heap, state)

    costs = 1000000000
    while heap:
        state = heapq.heappop(heap)
        if state[0] >= costs:
            return costs

        for s in range(len(SPELLS)):
            st = copy.deepcopy(state)
            res, s = turn(s, *st, hard_mode)
            match res:
                case True:
                    costs = min(costs, s)
                case False:
                    pass
                case None:
                    heapq.heappush(heap, s)


def part1(boss):
    return simulate(boss, False)


def part2(boss):
    return simulate(boss, True)


TEST_DATA = {}
TEST_DATA[
    """\
Hit Points: 55
Damage: 8
""".rstrip()
] = (953, 1289)
