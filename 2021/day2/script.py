

def main():

    aim = 0
    x = 0
    z = 0

    with open('day2/input.txt') as f:
        for line in f:
            line = line.strip().split()

            direction = line[0]
            length = int(line[1])
            if direction == 'forward':
                x += length
                z += aim*length
            elif direction == 'up':
                aim -= length
            elif direction == 'down':
                aim += length

    print(x, z, x*z)



if __name__ == "__main__":
    main()