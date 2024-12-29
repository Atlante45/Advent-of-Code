from more_itertools import flatten


def parse(data):
    rules, messages = data.split("\n\n")
    messages = messages.splitlines()

    rules_dict = {}
    for rule in rules.splitlines():
        r, s = rule.split(": ")
        if s.startswith('"'):
            rules_dict[r] = s[1:-1]
        elif "|" in s:
            rules_dict[r] = [a.split() for a in s.split("|")]
        else:
            rules_dict[r] = [s.split()]

    return rules_dict, messages


def match_subrule(rules, message, subrule, indices):
    for rule in subrule:
        matches = match_rule(rules, message, rule, indices)
        if not matches:
            return set()
        indices = matches
    return indices


def match_rule(rules, message, r="0", indices=set([0])):
    indices = set([i for i in indices if i < len(message)])
    if not indices:
        return set()

    rule = rules[r]
    if isinstance(rule, str):
        return set([i + 1 for i in indices if message[i] == rule])

    return set(
        flatten(match_subrule(rules, message, subrule, indices) for subrule in rule)
    )


def part1(rules, messages):
    return sum(1 for message in messages if len(message) in match_rule(rules, message))


def part2(rules, messages):
    rules["8"] = [["42", "8"], ["42"]]
    rules["11"] = [["42", "11", "31"], ["42", "31"]]
    return sum(1 for message in messages if len(message) in match_rule(rules, message))


TEST_DATA = {}
TEST_DATA[
    """\
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
""".rstrip()
] = (3, 12)
