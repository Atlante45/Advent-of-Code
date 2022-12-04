from solutions.utils import logger
from aocd import data


def get_coords(i, j):
    return [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]


def get_pixel(input_image, i, j, flip):
    if i >= 0 and i < len(input_image) and j >= 0 and j < len(input_image[0]):
        return "1" if input_image[i][j] == "#" else "0"
    else:
        return "1" if flip else "0"


def get_index(input_image, i, j, flip):
    string_index = "".join(
        [get_pixel(input_image, x, y, flip) for x, y in get_coords(i, j)]
    )
    return int(string_index, 2)


def enhance(input_image, alg, flip):
    output_image = []
    for i in range(len(input_image) + 2):
        line = ""
        for j in range(len(input_image[0]) + 2):
            line += alg[get_index(input_image, i - 1, j - 1, flip)]

        output_image.append(line)

    return output_image


def enhance_n(input_image, alg, count):
    for i in range(count):
        flip = i % 2 and alg[0] == "#"
        input_image = enhance(input_image, alg, flip)
    return input_image


def count_light(input_image):
    return sum([line.count("#") for line in input_image])


def part1(input_image, alg):
    enhanced = enhance_n(input_image, alg, 2)
    return count_light(enhanced)


def part2(input_image, alg):
    enhanced = enhance_n(input_image, alg, 50)
    return count_light(enhanced)


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    data = data.splitlines()
    alg = data[0]
    input_image = data[2:]

    ans_1 = part1(input_image, alg)
    logger.debug_part(0, ans_1, result, debug)

    ans_2 = part2(input_image, alg)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (5057, 18502)
TEST_RESULT = (35, 3351)
TEST_DATA = """\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
