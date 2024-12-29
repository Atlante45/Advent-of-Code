from math import prod
from more_itertools import flatten


def parse(data):
    fields, ticket, nearby = data.split("\n\n")

    fields = [f.split(": ") for f in fields.splitlines()]
    fields = {
        k: [list(map(int, r.split("-"))) for r in v.split(" or ")] for k, v in fields
    }

    ticket = list(map(int, ticket.splitlines()[1].split(",")))

    nearby = [list(map(int, n.split(","))) for n in nearby.splitlines()[1:]]

    return fields, ticket, nearby


def is_valid(fields, n):
    for ranges in fields.values():
        for r in ranges:
            if r[0] <= n <= r[1]:
                return True
    return False


def part1(fields, ticket, nearby):
    return sum(n for n in flatten(nearby) if not is_valid(fields, n))


def valid_fields(fields, values):
    valid_fields = []
    for field, ranges in fields.items():
        if all(any(r[0] <= n <= r[1] for r in ranges) for n in values):
            valid_fields.append(field)
    return set(valid_fields)


def part2(fields, ticket, nearby):
    valid_tickets = [t for t in nearby if all(is_valid(fields, n) for n in t)]

    values = list(zip(*valid_tickets))

    possible = {i: valid_fields(fields, v) for i, v in enumerate(values)}

    while any(len(p) > 1 for p in possible.values()):
        for i, p in possible.items():
            if len(p) == 1:
                for j, q in possible.items():
                    if i != j and p.issubset(q):
                        possible[j] = q - p

    return prod(
        ticket[i] for i, p in possible.items() if p.pop().startswith("departure")
    )


TEST_DATA = {}
TEST_DATA[
    """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".rstrip()
] = (71, None)
