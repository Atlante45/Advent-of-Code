#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data


chars = {"<": ">", "[": "]", "{": "}", "(": ")"}

score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

vals = {"<": 4, "[": 2, "{": 3, "(": 1}


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


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (345441, 3235371166)
TEST_RESULT = (26397, 288957)
TEST_DATA = """\
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

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
