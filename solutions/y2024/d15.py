import enum


DIR = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


def parse(data):
    map, instructions = data.split("\n\n")
    map = map.splitlines()
    instructions = "".join(instructions.splitlines())
    return instructions, map


def part1(instructions, map):
    robot = None
    boxes = set()
    walls = set()
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == "#":
                walls.add((i, j))
            elif cell == "O":
                boxes.add((i, j))
            elif cell == "@":
                robot = (i, j)

    for isntr in instructions:
        i, j = robot
        steps = 1
        while (i + steps * DIR[isntr][0], j + steps * DIR[isntr][1]) in boxes:
            steps += 1

        ei = i + steps * DIR[isntr][0]
        ej = j + steps * DIR[isntr][1]
        if (ei, ej) in walls:
            continue

        robot = (i + DIR[isntr][0], j + DIR[isntr][1])

        if robot in boxes:
            boxes.remove(robot)
            boxes.add((ei, ej))

    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if (i, j) in boxes:
                print("O", end="")
            elif (i, j) in walls:
                print("#", end="")
            elif (i, j) == robot:
                print("@", end="")
            else:
                print(".", end="")
        print()

    return sum(100 * i + j for i, j in boxes)


def part2(instructions, map):
    robot = None
    boxes = set()
    walls = set()
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == "#":
                walls.add((i, 2 * j))
                walls.add((i, 2 * j + 1))
            elif cell == "O":
                boxes.add((i, 2 * j))
            elif cell == "@":
                robot = (i, 2 * j)

    for i in range(len(map)):
        for j in range(2 * len(map[0])):
            if (i, j) in walls:
                print("#", end="")
            elif (i, j) in boxes:
                print("[", end="")
            elif (i, j - 1) in boxes:
                print("]", end="")
            elif (i, j) == robot:
                print("@", end="")
            else:
                print(".", end="")
        print()

    for isntr in instructions:
        # dprint(map, robot, boxes, walls)
        # input()
        print("Instruction:", isntr)

        i, j = robot

        ni = i + DIR[isntr][0]
        nj = j + DIR[isntr][1]
        if (ni, nj) in walls:
            print("Hit wall")
            continue

        if (ni, nj) not in boxes and (ni, nj - 1) not in boxes:
            robot = (ni, nj)
            print("Move")
            continue

        eb = set()
        if isntr == ">":
            while (ni, nj) in boxes:
                eb.add((ni, nj))
                nj += 2

            if (ni, nj) in walls:
                continue
        elif isntr == "<":
            while (ni, nj - 1) in boxes:
                eb.add((ni, nj - 1))
                nj -= 2

            if (ni, nj) in walls:
                continue
        else:
            push = set()
            if (ni, nj) in boxes:
                push.add((ni, nj))
            else:
                assert (ni, nj - 1) in boxes
                push.add((ni, nj - 1))

            success = True
            dir = DIR[isntr][0]
            while len(push) > 0:
                pi, pj = push.pop()
                if (pi + dir, pj) in walls or (pi + dir, pj + 1) in walls:
                    success = False
                    break

                eb.add((pi, pj))

                if (pi + dir, pj + 1) in boxes:
                    push.add((pi + dir, pj + 1))
                if (pi + dir, pj) in boxes:
                    push.add((pi + dir, pj))
                if (pi + dir, pj - 1) in boxes:
                    push.add((pi + dir, pj - 1))

            if not success:
                continue

        print(f"Push {len(eb)} boxes: {eb}")
        new_boxes = set()
        for box in eb:
            boxes.remove(box)
            new_boxes.add((box[0] + DIR[isntr][0], box[1] + DIR[isntr][1]))
        boxes |= new_boxes
        robot = (i + DIR[isntr][0], j + DIR[isntr][1])

    return sum(100 * i + j for i, j in boxes)


def dprint(map, robot, boxes, walls):
    for i in range(len(map)):
        for j in range(2 * len(map[0])):
            if (i, j) in walls:
                print("#", end="")
            elif (i, j) in boxes:
                print("[", end="")
            elif (i, j - 1) in boxes:
                print("]", end="")
            elif (i, j) == robot:
                print("@", end="")
            else:
                print(".", end="")
        print()


TEST_DATA = {}
TEST_DATA[
    """\
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
""".rstrip()
] = (2028, None)
TEST_DATA[
    """\
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
""".rstrip()
] = (10092, 9021)
