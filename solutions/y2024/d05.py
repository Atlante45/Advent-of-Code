def parse(data):
    rules, updates = data.split('\n\n')
    rules = [tuple(map(int, rule.split('|'))) for rule in rules.splitlines()]
    updates = [tuple(map(int, update.split(','))) for update in updates.splitlines()]

    return rules, updates

def is_valid(update, rules):
    for rule in rules:
        try:
            i1 = update.index(rule[0])
            i2 = update.index(rule[1])
            if i1 > i2:
                return False
        except ValueError:
            pass
    return True

def fix_update(update, rules):
    if len(update) <= 1:
        return list(update)

    before = []
    after = []
    for rule in rules:
        if update[0] == rule[0] and rule[1] in update:
            before.append(rule[1])
        elif update[0] == rule[1] and rule[0] in update:
            after.append(rule[0])

    return fix_update(after, rules) + [update[0]] + fix_update(before, rules)

def parts(rules, updates):
    sum1 = 0
    sum2 = 0
    for update in updates:
        if is_valid(update, rules):
            sum1 += update[len(update)//2]
        else:
            up = fix_update(update, rules)
            sum2 += up[len(up)//2]


    return sum1, sum2



TEST_DATA = {}
TEST_DATA[
    """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".rstrip()
] = (143, 123)
