#!/usr/bin/env python3
from solutions.utils import logger
from aocd import data


def add_file(root, path, file, size):
    if not path:
        root[file] = size
        return
    if path[0] not in root:
        root[path[0]] = {}

    add_file(root[path[0]], path[1:], file, size)


def du(root):
    size = 0
    total = 0
    for k, v in root.items():
        if isinstance(v, dict):
            s, t = du(v)
            size += s
            total += t
        else:
            size += v
    if size < 100000:
        total += size
    return size, total


def find(root, needed):
    size = 0
    cur_min = 1000000000000000000000000
    for k, v in root.items():
        if isinstance(v, dict):
            s, v_min = find(v, needed)
            cur_min = min(v_min, cur_min)
            size += s
        else:
            size += v

    if size >= needed:
        cur_min = min(size, cur_min)
    return size, cur_min


def part1(data):
    root = {}
    path = []
    for line in data:
        items = line.split()
        # print("line", items)
        # print(path)
        # print(root)
        if items[0] == "$":
            if items[1] == "cd":
                if items[2] == "/":
                    path = []
                    continue
                elif items[2] == "..":
                    path.pop()
                else:
                    path.append(items[2])
        else:
            if items[0] != "dir":
                add_file(root, path, items[1], int(items[0]))

    # print(root)
    # print()
    _, total = du(root)

    return total


def part2(data):
    root = {}
    path = []
    for line in data:
        items = line.split()
        # print("line", items)
        # print(path)
        # print(root)
        if items[0] == "$":
            if items[1] == "cd":
                if items[2] == "/":
                    path = []
                    continue
                elif items[2] == "..":
                    path.pop()
                else:
                    path.append(items[2])
        else:
            if items[0] != "dir":
                add_file(root, path, items[1], int(items[0]))

    # print(root)
    # print()
    size, total = du(root)
    available = 70000000 - size
    needed = 30000000 - available
    _, res = find(root, needed)
    return res


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()

    ans_1 = part1(data)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(data)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (None, None)
TEST_RESULT = (95437, 24933642)
TEST_DATA = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
