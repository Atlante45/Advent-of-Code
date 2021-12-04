

from collections import deque


def main():
    count = 0
    vals = deque([])

    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if line.isnumeric():
                cur = int(line)

                if len(vals) == 3 and cur > vals.popleft():
                    count += 1

                vals.append(cur)

    print('Count is {}'.format(count))




if __name__ == "__main__":
    main()
