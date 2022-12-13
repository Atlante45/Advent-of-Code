import math


class SFNum:
    def __init__(self, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent

        if isinstance(self.left, SFNum):
            self.left.parent = self
        if isinstance(self.right, SFNum):
            self.right.parent = self

    def __str__(self):
        return f"[{self.left},{self.right}]"


def parseNum(line, parent=None):
    if line[0].isdigit():
        return int(line[0]), line[1:]

    node = SFNum()
    node.parent = parent
    node.left, line = parseNum(line[1:], node)

    if not line[0] == ",":
        print("Something's wrong!!!!")

    node.right, line = parseNum(line[1:], node)

    if not line[0] == "]":
        print("Something's wrong!!!!")

    return node, line[1:]


def parseLine(line):
    num, _ = parseNum(line)
    return num


def add(left, right):
    return reduce(SFNum(left, right))


def addLeft(node, val):
    parent = node.parent
    if not parent:
        return

    if parent.left == node:
        addLeft(parent, val)
    elif isinstance(parent.left, int):
        parent.left += val
    else:
        node = parent.left
        while isinstance(node.right, SFNum):
            node = node.right
        node.right += val


def addRight(node, val):
    parent = node.parent
    if not parent:
        return

    if parent.right == node:
        addRight(parent, val)
    elif isinstance(parent.right, int):
        parent.right += val
    else:
        node = parent.right
        while isinstance(node.left, SFNum):
            node = node.left
        node.left += val


def explode(num, depth=0):
    if isinstance(num, int):
        return False

    if depth >= 4:
        addLeft(num, num.left)
        addRight(num, num.right)
        if num.parent.left == num:
            num.parent.left = 0
        else:
            num.parent.right = 0
        return True

    return explode(num.left, depth + 1) or explode(num.right, depth + 1)


def split(num):
    if isinstance(num.left, int) and num.left > 9:
        num.left = SFNum(math.floor(num.left / 2), math.ceil(num.left / 2), num)
        return True

    if isinstance(num.left, SFNum) and split(num.left):
        return True

    if isinstance(num.right, int) and num.right > 9:
        num.right = SFNum(math.floor(num.right / 2), math.ceil(num.right / 2), num)
        return True

    return isinstance(num.right, SFNum) and split(num.right)


def reduce(num):
    while True:
        if explode(num):
            # print('explode:', num)
            continue
        if split(num):
            # print('split  :', num)
            continue
        break

    return num


def mag(num):
    if isinstance(num, int):
        return num
    else:
        return 3 * mag(num.left) + 2 * mag(num.right)


def maxMag(line1, line2):
    return max(
        mag(add(parseLine(line1), parseLine(line2))),
        mag(add(parseLine(line2), parseLine(line1))),
    )


def parse(data):
    return data.splitlines()


def part1(input):
    nums = [parseLine(line.strip()) for line in input]

    sum = nums[0]
    for i in range(1, len(nums)):
        sum = add(sum, nums[i])
    # print(sum)
    return mag(sum)


def part2(input):
    res = 0

    for i in range(len(input) - 1):
        for j in range(i + 1, len(input)):
            res = max(res, maxMag(input[i], input[j]))

    return res


TEST_DATA = {}
TEST_DATA[
    """\
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
""".rstrip()
] = (4140, 3993)
