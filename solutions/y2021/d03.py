from solutions.utils import logger
from aocd import data


def lineToArray(line):
    return list(map(lambda c: int(c), list(line.strip())))


def part1(lines):
    numLines = len(lines)

    mask = list(map(lambda c: "1", list(lines[0].strip())))
    mask = int("".join(mask), 2)

    bitLists = list(map(lineToArray, lines))
    mostCommonBits = [str(round(sum(i) / numLines)) for i in zip(*bitLists)]
    gammaRate = int("".join(mostCommonBits), 2)
    epsilonRate = ~gammaRate & mask

    return gammaRate * epsilonRate


def bitOccurence(index, bitLists):
    bitsAtIndex = [bits[index] for bits in bitLists]
    zeroOccurence = bitsAtIndex.count(0)
    return (zeroOccurence, len(bitsAtIndex) - zeroOccurence)


def bitFilter(val, index, bitLists):
    return list(filter(lambda bitList: bitList[index] == val, bitLists))


def computeRating(criteria, bitLists):

    for i in range(len(bitLists[0])):
        (zeros, ones) = bitOccurence(i, bitLists)
        bitLists = bitFilter(criteria(zeros, ones), i, bitLists)

        if len(bitLists) == 1:
            break

    return int("".join(map(lambda c: str(c), bitLists[0])), 2)


def part2(lines):
    bitLists = list(map(lineToArray, lines))

    oxRating = computeRating(lambda z, o: int(not z > o), bitLists)
    co2Rating = computeRating(lambda z, o: int(not z <= o), bitLists)

    return oxRating * co2Rating


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (4174964, 4474944)
TEST_RESULT = (198, 230)
TEST_DATA = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
