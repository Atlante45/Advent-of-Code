from solutions.utils import logger
from aocd import data


# segments = {
#     1: "cf",
#     7: "acf",
#     4: "bcdf",
#     2: "acdeg",
#     3: "acdfg",
#     5: "abdfg",
#     6: "abdefg",
#     9: "abcdfg",
#     0: "abcefg",
#     8: "abcdefg",
# }


def sub(lst1, lst2):
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3


def part1(input):
    total = 0
    for line in input:
        line = line.strip().split("|")[1].split()
        for i in line:
            if len(i) in [2, 4, 3, 7]:
                total += 1

    return total


def part2(input):
    total = 0
    for line in input:
        [pattern, key] = line.strip().split("|")
        pattern = pattern.split()
        key = key.split()

        pattern.sort(key=len)

        value = 0
        for i in key:
            if len(i) == 2:
                value += 1
            elif len(i) == 3:
                value += 7
            elif len(i) == 4:
                value += 4
            elif len(i) == 7:
                value += 8
            elif len(i) == 5:
                if len(sub(i, pattern[2])) == 3:
                    value += 2
                elif len(sub(i, pattern[0])) == 3:
                    value += 3
                else:
                    value += 5
            elif len(i) == 6:
                if len(sub(i, pattern[0])) == 5:
                    value += 6
                elif len(sub(i, pattern[2])) == 2:
                    value += 9
                else:
                    value += 0
            else:
                print("ERROR")
            value *= 10

        value = value // 10
        total += value

    return total


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (488, 1040429)
TEST_RESULT = (26, 61229)
TEST_DATA = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
