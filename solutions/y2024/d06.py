from collections import defaultdict

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def parse(data):
    lines = data.splitlines()

    size = len(lines), len(lines[0])
    start = None
    obstacles = set()

    col_obstacles = defaultdict(list)
    row_obstacles = defaultdict(list)

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                obstacles.add((i, j))
                col_obstacles[j].append(i)
                row_obstacles[i].append(j)
            elif c == '^':
                start = (i, j)

    for col in col_obstacles:
        col_obstacles[col].sort()
    for row in row_obstacles:
        row_obstacles[row].sort()


    return start, size, obstacles, col_obstacles, row_obstacles

def cast_ray(pos, dir, size, col_obstacles, row_obstacles):
    if dir == 0:
        for obstacle in reversed(col_obstacles[pos[1]]):
            if obstacle < pos[0]:
                return (obstacle + 1, pos[1]), False
        return (0, pos[1]), True
    elif dir == 1:
        for obstacle in row_obstacles[pos[0]]:
            if obstacle > pos[1]:
                return (pos[0], obstacle - 1), False
        return (pos[0], size[1] - 1), True
    elif dir == 2:
        for obstacle in col_obstacles[pos[1]]:
            if obstacle > pos[0]:
                return (obstacle - 1, pos[1]), False
        return (size[0] - 1, pos[1]), True
    elif dir == 3:
        for obstacle in reversed(row_obstacles[pos[0]]):
            if obstacle < pos[1]:
                return (pos[0], obstacle + 1), False
        return (pos[0], 0), True


def does_loop(obstacles, start, size, obstacle):
    dir = 0
    pos = start

    visited = defaultdict(set)
    visited[pos].add(dir)

    while True:
        next_pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])

        if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= size[0] or next_pos[1] >= size[1]:
            break

        if next_pos != obstacle and next_pos not in obstacles:
            pos = next_pos   
        else:
            dir = (dir + 1) % 4
        
        if dir in visited[pos]:
            return True
        visited[pos].add(dir)

    return False

def parts(start, size, obstacles, col_obstacles, row_obstacles):
    dir = 0
    pos = start

    visited = set()


    while True:
        next_pos, escaped = cast_ray(pos, dir, size, col_obstacles, row_obstacles)
        if dir in [0, 2]:
            for i in range(pos[0], next_pos[0], DIRS[dir][0]):
                visited.add((i, pos[1]))
        else:
            for j in range(pos[1], next_pos[1], DIRS[dir][1]):
                visited.add((pos[0], j))

        if escaped:
            visited.add(next_pos)
            break

        pos = next_pos
        dir = (dir + 1) % 4
    

    ans1 = len(visited)
        
    visited.remove(start)
    ans2 = sum(does_loop(obstacles, start, size, pos) for pos in visited)

    return ans1, ans2


TEST_DATA = {}
TEST_DATA[
    """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".rstrip()
] = (41, 6)
