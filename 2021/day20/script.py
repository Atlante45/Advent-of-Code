#!/usr/bin/env python3
import os

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
        return '1' if input_image[i][j] == '#' else '0'
    else:
        return '1' if flip else '0'

def get_index(input_image, i, j, flip):
    string_index = ''.join([get_pixel(input_image, x, y, flip) for x, y in get_coords(i, j)])
    return int(string_index, 2)

def enhance(input_image, alg, flip):
    output_image = []
    for i in range(len(input_image) + 2):
        line = ''
        for j in range(len(input_image[0]) + 2):
            line += alg[get_index(input_image, i - 1, j - 1, flip)]

        output_image.append(line)

    return output_image

def enhance_n(input_image, alg, count):
    for i in range(count):
        flip = i % 2 and alg[0] == '#'
        input_image = enhance(input_image, alg, flip)
    return input_image

def count_light(input_image):
    return sum([line.count('#') for line in input_image])

def part1(input_image, alg):
    enhanced = enhance_n(input_image, alg, 2)
    return count_light(enhanced)

def part2(input_image, alg):
    enhanced = enhance_n(input_image, alg, 50)
    return count_light(enhanced)

def readInput(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        alg = input[0]
        input_image = input[2:]

        print(f'Solving {filename}')
        print(f"    Part 1: {part1(input_image, alg)}")
        print(f"    Part 2: {part2(input_image, alg)}")

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
