def parse(data):
    return data.splitlines()


def count_xmas(grid):
    count = 0
    width = len(grid[0])
    height = len(grid)

    for line in grid:
        count += line.count("XMAS")
        count += line.count("SAMX")

    for i in range(width + height + 1):
        line = ""
        for j in range(i+1):
            try:
                line += grid[i - j][j]
            except IndexError:
                pass
        count += line.count("XMAS")
        count += line.count("SAMX")
    return count

def part1(grid):
    count = count_xmas(grid)

    grid = list(zip(*grid))
    grid = [''.join(line) for line in reversed(grid)]

    count += count_xmas(grid)

    return count

def part2(grid):
    count = 0
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            if grid[i][j] == "A":
                try:
                    if grid[i-1][j-1] == "M" and grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S" and grid[i+1][j+1] == "S":
                        count += 1
                    if grid[i-1][j-1] == "S" and grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M" and grid[i+1][j+1] == "M":
                        count += 1
                    if grid[i-1][j-1] == "M" and grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M" and grid[i+1][j+1] == "S":
                        count += 1
                    if grid[i-1][j-1] == "S" and grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S" and grid[i+1][j+1] == "M":
                        count += 1
                except IndexError:
                    pass
    return count


TEST_DATA = {}
TEST_DATA[
    """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".rstrip()
] = (18, 9)
