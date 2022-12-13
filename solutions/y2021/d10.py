chars = {"<": ">", "[": "]", "{": "}", "(": ")"}

score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

vals = {"<": 4, "[": 2, "{": 3, "(": 1}


def parse(data):
    return data.splitlines()


def part1(input):
    res = 0

    stack = []
    for line in input:
        for c in line.strip():
            if c in chars.keys():
                stack.append(c)
            elif chars[stack.pop()] != c:
                res += score[c]
                break
        stack.clear()

    return res


def part2(input):
    scores = []

    stack = []
    for line in input:
        skip = False
        for c in line.strip():
            if c in chars.keys():
                stack.append(c)
            elif chars[stack.pop()] != c:
                skip = True
                break

        if not skip:
            score = 0
            for i in reversed(stack):
                score = 5 * score + vals[i]
            scores.append(score)

        stack.clear()

    scores = sorted(scores)

    return scores[len(scores) // 2]


TEST_DATA = {}
TEST_DATA[
    """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".rstrip()
] = (26397, 288957)
