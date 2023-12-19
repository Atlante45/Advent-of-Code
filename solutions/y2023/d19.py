import copy
from math import prod


def parse(data):
    wfs, parts = data.split("\n\n")
    workflows = {}
    for wf in wfs.splitlines():
        name, rules = wf.split("{")
        rules = [r.split(":") if ":" in r else [None, r] for r in rules[:-1].split(",")]
        workflows[name] = rules
    parts = [
        eval(part.replace("=", ":"), {v: v for v in "xmas"})
        for part in parts.splitlines()
    ]
    return workflows, parts


def accepted(workflows, workflow, part):
    if workflow == "A":
        return True
    if workflow == "R":
        return False

    workflow = workflows[workflow]
    for rule, dest in workflow:
        if rule is None or eval(rule, part.copy()):
            return accepted(workflows, dest, part)


def part1(workflows, parts):
    return sum(sum(p.values()) for p in parts if accepted(workflows, "in", p))


def split_part(rule, part):
    if rule is None:
        return part

    ind = rule[0]
    val = int(rule[2:])

    accepted_part = copy.deepcopy(part)
    rejected_part = part
    if rule[1] == "<":
        accepted_part[ind][1] = min(accepted_part[ind][1], val - 1)
        rejected_part[ind][0] = max(rejected_part[ind][0], val)
    else:
        accepted_part[ind][0] = max(accepted_part[ind][0], val + 1)
        rejected_part[ind][1] = min(rejected_part[ind][1], val)

    return accepted_part if accepted_part[ind][0] <= accepted_part[ind][1] else None


def compute(workflows, part, workflow):
    if workflow == "R" or part is None:
        return 0
    if workflow == "A":
        return prod([p[1] - p[0] + 1 for p in part.values()])

    res = 0
    for rule, dest in workflows[workflow]:
        accepted_part = split_part(rule, part)
        res += compute(workflows, accepted_part, dest)
    return res


def part2(workflows, _):
    part = {v: [1, 4000] for v in "xmas"}
    return compute(workflows, part, "in")


TEST_DATA = {}
TEST_DATA[
    """\
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
""".rstrip()
] = (19114, 167409079868000)
