def parse(data):
    rules, updates = data.split('\n\n')
    rules = [tuple(map(int, rule.split('|'))) for rule in rules.splitlines()]
    updates = [list(map(int, update.split(','))) for update in updates.splitlines()]

    return rules, updates

def sort_update(update, rules):
    if len(update) <= 1:
        return update

    before = []
    after = []
    for rule in rules:
        if update[0] == rule[0] and rule[1] in update:
            before.append(rule[1])
        elif update[0] == rule[1] and rule[0] in update:
            after.append(rule[0])


    return sort_update(after, rules) + [update[0]] + sort_update(before, rules)

def parts(rules, updates):
    sum1 = 0
    sum2 = 0
    for update in updates:
        sorted_update = sort_update(update, rules)
        mid_value = sorted_update[len(sorted_update)//2]

        if sorted_update == update:
            sum1 += mid_value
        else:
            sum2 += mid_value
        
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
