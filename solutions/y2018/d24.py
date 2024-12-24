from copy import deepcopy
import re


R = r"(\d+) units each with (\d+) hit points (.*)with an attack that does (\d+) (\w+) damage at initiative (\d+)"


def parse_effects(effects):
    weaknesses = []
    immunities = []

    if not effects:
        return weaknesses, immunities

    for e in effects[1:-2].split("; "):
        if e.startswith("weak to"):
            weaknesses = [w.strip() for w in e[len("weak to") :].split(",")]
        else:
            immunities = [w.strip() for w in e[len("immune to") :].split(",")]

    return weaknesses, immunities


def parse_unit(line):
    units, hp, effects, damage, damage_type, initiative = re.match(R, line).groups()
    weaknesses, immunities = parse_effects(effects)
    return [
        int(units),
        int(hp),
        weaknesses,
        immunities,
        int(damage),
        damage_type,
        int(initiative),
    ]


def parse(data):
    immune_system, infection = data.split("\n\n")
    immune_system = immune_system.splitlines()[1:]
    infection = infection.splitlines()[1:]

    immune_system = [parse_unit(line) for line in immune_system]
    infection = [parse_unit(line) for line in infection]

    return immune_system, infection


def compute_effective_power(group):
    units, _, _, _, damage, _, _ = group
    return units * damage


def compute_damage(attacker, target):
    units, _, _, _, damage, damage_type, _ = attacker
    _, hp, weaknesses, immunities, _, _, _ = target

    assert units > 0

    damage = compute_effective_power(attacker)

    if damage_type in weaknesses:
        damage *= 2
    elif damage_type in immunities:
        damage = 0

    losses = damage // hp

    return damage, losses


def select_target(attacker, targets):
    def sort_key(target_id):
        target = targets[target_id]
        damage, _ = compute_damage(attacker, target)

        target_effective_power = compute_effective_power(target)
        target_initiative = target[6]
        return (damage, target_effective_power, target_initiative)

    return sorted(range(len(targets)), key=sort_key, reverse=True)


def select_targets(attackers, targets):
    select_order = sorted(
        range(len(attackers)),
        key=lambda x: (
            compute_effective_power(attackers[x]),
            attackers[x][6],
        ),
        reverse=True,
    )
    selected_target_ids = [None] * len(attackers)
    for attacker_id in select_order:
        attacker = attackers[attacker_id]
        if attacker[0] <= 0:
            continue

        target_ids = select_target(attacker, targets)

        target_id = next(
            (id for id in target_ids if id not in selected_target_ids),
            None,
        )

        if target_id is None:
            continue

        damage, _ = compute_damage(attacker, targets[target_id])
        if damage == 0:
            continue

        selected_target_ids[attacker_id] = target_id

    return selected_target_ids


def attack_target(attacker, target):
    damage, losses = compute_damage(attacker, target)
    return damage, losses


def simulate(immune_system, infection, boost=0):
    for group in immune_system:
        group[4] += boost

    while len(immune_system) > 0 and len(infection) > 0:
        immune_system_target_ids = select_targets(immune_system, infection)
        infection_target_ids = select_targets(infection, immune_system)

        armies = [immune_system, infection]
        targets = [immune_system_target_ids, infection_target_ids]
        attack_order = sorted(
            [
                (army, group)
                for army in range(len(armies))
                for group in range(len(armies[army]))
            ],
            key=lambda x: armies[x[0]][x[1]][6],
            reverse=True,
        )

        total_losses = 0
        for army, group in attack_order:
            attacker = armies[army][group]
            target_id = targets[army][group]

            if target_id is None or attacker[0] <= 0:
                continue

            defender = armies[1 - army][target_id]
            _, losses = attack_target(attacker, defender)
            defender[0] -= losses
            total_losses += losses

        if total_losses == 0:
            break

        immune_system = [g for g in immune_system if g[0] > 0]
        infection = [g for g in infection if g[0] > 0]

    immune_system_units = sum(g[0] for g in immune_system)
    infection_units = sum(g[0] for g in infection)

    return immune_system_units, infection_units


def part1(immune_system, infection):
    return sum(simulate(immune_system, infection))


def part2(immune_system, infection):
    low = 0
    high = 10000000000

    res = None

    while low < high:
        mid = (low + high) // 2
        immune_system_units, infection_units = simulate(
            deepcopy(immune_system), deepcopy(infection), mid
        )
        if infection_units > 0:
            low = mid + 1
        else:
            res = immune_system_units
            high = mid

    return res


TEST_DATA = {}
TEST_DATA[
    """\
Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
""".rstrip()
] = (5216, 51)
