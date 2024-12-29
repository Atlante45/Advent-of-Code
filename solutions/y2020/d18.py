from math import prod


def parse(data):
    return data.splitlines()


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.left} {self.value} {self.right})"


def evaluate(expression):
    stack = []

    value = 0
    op = "+"
    for token in expression:
        if token == " ":
            continue

        if token in ("+", "*"):
            op = token
        elif token == "(":
            stack.append((value, op))
            value = 0
            op = "+"
        elif token == ")":
            v, o = stack.pop()
            value = value + v if o == "+" else value * v
        else:
            value = value + int(token) if op == "+" else value * int(token)
    return value


def part1(expressions):
    return sum(evaluate(expression) for expression in expressions)


def evaluate2(expression):
    stack = []

    values = []
    op = "*"
    for token in expression:
        if token == " ":
            continue

        if token in ("+", "*"):
            op = token
        elif token == "(":
            stack.append((values, op))
            values = []
            op = "*"
        elif token == ")":
            val = prod(values)
            values, op = stack.pop()

            if op == "*":
                values.append(val)
            else:
                values[-1] += val
        else:
            if op == "*":
                values.append(int(token))
            else:
                values[-1] += int(token)
    return prod(values)


def part2(expressions):
    return sum(evaluate2(expression) for expression in expressions)


TEST_DATA = {}
TEST_DATA[
    """\
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
""".rstrip()
] = (13632, 23340)
