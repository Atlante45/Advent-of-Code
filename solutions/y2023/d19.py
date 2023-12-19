from math import prod
import re


REGEX = r"{x=(.*),m=(.*),a=(.*),s=(.*)}"


def parse_workflow(workflow):
    name, rules = workflow.split("{")
    rules = rules[:-1].split(",")
    return name, rules


def parse(data):
    wfs, parts = data.split("\n\n")
    workflows = {}
    for wf in wfs.splitlines():
        name, rules = parse_workflow(wf)
        workflows[name] = rules
    parts = [
        list(map(int, re.match(REGEX, part).groups())) for part in parts.splitlines()
    ]
    return workflows, parts


INDEX = "xmas"


def matcth_rule(rule, part):
    if rule[1] == "<":
        return part[INDEX.index(rule[0])] < int(rule[2:])
    else:
        return part[INDEX.index(rule[0])] > int(rule[2:])


def is_acceptable(workflows, workflow, part):
    if workflow == "A":
        return True
    if workflow == "R":
        return False
    workflow = workflows[workflow]
    for rule in workflow:
        if ":" in rule:
            if matcth_rule(rule.split(":")[0], part):
                return is_acceptable(workflows, rule.split(":")[1], part)
        else:
            return is_acceptable(workflows, rule, part)


def part1(workflows, parts):
    res = 0
    for part in parts:
        if is_acceptable(workflows, "in", part):
            res += sum(part)
    return res


def split_part(rule, part):
    ind = INDEX.index(rule[0])
    op = rule[1]
    val = int(rule[2:])

    part1 = [p.copy() for p in part]
    part2 = [p.copy() for p in part]
    if op == "<":
        part1[ind][1] = min(part1[ind][1], val - 1)
        part2[ind][0] = max(part1[ind][0], val)
    else:
        part1[ind][0] = max(part1[ind][0], val + 1)
        part2[ind][1] = min(part1[ind][1], val)

    return part1 if part1[ind][0] <= part1[ind][1] else None, part2 if part2[ind][
        0
    ] <= part2[ind][1] else None


def compute(workflows, part, workflow):
    if workflow == "R" or part is None:
        return 0
    if workflow == "A":
        return prod([p[1] - p[0] + 1 for p in part])

    workflow = workflows[workflow]
    res = 0
    for rule in workflow:
        if ":" in rule:
            part1, part2 = split_part(rule.split(":")[0], part)
            res += compute(workflows, part1, rule.split(":")[1])
            part = part2
        else:
            res += compute(workflows, part, rule)
    return res


def part2(workflows, parts):
    part = [
        [1, 4000],
        [1, 4000],
        [1, 4000],
        [1, 4000],
    ]
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
