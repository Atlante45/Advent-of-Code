#!/usr/bin/python3
from collections import defaultdict
import math
import os
import re
import numpy as np
from scipy.spatial.transform import Rotation

def dist(a, b):
    return math.sqrt(sum([(a_i - b_i)**2 for a_i, b_i in zip(a, b)]))

def sub(a, b):
    return [a_i - b_i for a_i, b_i in zip(a, b)]

def add(a, b):
    return [a_i + b_i for a_i, b_i in zip(a, b)]

def part1(scanners):
    res = 0

    beaconDistances = {}
    scannersSeenWithDist = defaultdict(lambda: {})
    for s in scanners:
        for i in range(len(scanners[s]) - 1):
            for j in range(i + 1, len(scanners[s])):
                d = dist(scanners[s][i], scanners[s][j])
                beaconDistances[(s, i, j)] = d
                scannersSeenWithDist[d][s] = [i, j]


    reccuringDist = {}
    for i in beaconDistances.values():
        count = list(beaconDistances.values()).count(i)
        if count == 2:
            reccuringDist[i] = [k[0] for k, d in beaconDistances.items() if d == i]
            reccuringDist[i] = (reccuringDist[i][0], reccuringDist[i][1])

    mapped = {
        '0': {
            'trl': [0, 0, 0],
            'rot': Rotation.from_euler('x', 0, degrees=True)
        }
    }
    unmapped = [s for s in scanners if s != '0']

    commonDistForPairs = {}
    for v in reccuringDist.values():
        commonDistForPairs[v] = [d for d, v1 in reccuringDist.items() if v == v1]


    while unmapped:
        for (s1, s2), ds in commonDistForPairs.items():
            if (s1 in mapped and s2 in mapped) or (s1 in unmapped and s2 in unmapped):
                continue
            if s2 in mapped:
                s1, s2 = s2, s1

            i1, j1 = scannersSeenWithDist[ds[0]][s1]
            i2, j2 = scannersSeenWithDist[ds[0]][s2]
            for d in ds[1:]:
                b1 = scannersSeenWithDist[d][s1]
                b2 = scannersSeenWithDist[d][s2]
                if (i1 in b1 or j1 in b1) and (i2 in b2 or j2 in b2):
                    if j1 in b1:
                        i1, j1 = j1, i1
                    if j2 in b2:
                        i2, j2 = j2, i2

                    k1 = b1[0] if b1[0] != i1 else b1[1]
                    k2 = b2[0] if b2[0] != i2 else b2[1]

                    a1 = sub(scanners[s1][j1], scanners[s1][i1])
                    b1 = sub(scanners[s1][k1], scanners[s1][i1])
                    a2 = sub(scanners[s2][j2], scanners[s2][i2])
                    b2 = sub(scanners[s2][k2], scanners[s2][i2])

                    rot, _ = Rotation.align_vectors([a1, b1], [a2, b2])
                    trl = sub(scanners[s1][i1], rot.apply(scanners[s2][i2]))

                    x1 = scanners[s1][j1]
                    x2 = [round(v) for v in add(trl, rot.apply(scanners[s2][j2]))]
                    y1 = scanners[s1][k1]
                    y2 = [round(v) for v in add(trl, rot.apply(scanners[s2][k2]))]
                    if x1 != x2:
                        print(x1, x2)
                    if y1 != y2:
                        print(y1, y2)

                    mapped[s2] = {
                        'trl': [round(v) for v in add(mapped[s1]['trl'], mapped[s1]['rot'].apply(trl))],
                        'rot': mapped[s1]['rot'] * rot
                    }
                    unmapped.remove(s2)
                    break


    beacons = set()
    for v in scanners['0']:
        beacons.add((v[0], v[1], v[2]))

    for s in [s for s in scanners if s != '0']:
        for b in scanners[s]:
            trl = mapped[s]['trl']
            rot = mapped[s]['rot']
            v = [round(v) for v in add(trl, rot.apply(b))]
            beacons.add((v[0], v[1], v[2]))

    # print(sorted(beacons))

    maxDist = 0
    for i in range(len(mapped) - 1):
        for j in range(i+1, len(mapped)):
            v1 = mapped[str(i)]['trl']
            v2 = mapped[str(j)]['trl']
            maxDist = max(maxDist, sum([abs(j - i) for i, j in zip(v1, v2)]))

    print(f"    Part 1: {len(beacons)}")
    print(f"    Part 2: {maxDist}")



def readInput(filename):
    with open(filename) as f:
        return f.readlines()

def readScanner(input):
    scanner = re.search('^--- scanner ([0-9]*) ---', input.pop(0)).group(1)
    beacons = []

    line = input.pop(0).strip()
    while line:
        beacons.append([int(v) for v in line.strip().split(',')])
        line = input.pop(0).strip() if input else ''

    return scanner, beacons

def solve(filename):
    inputFile = os.path.join(os.path.dirname(__file__), filename)
    input = readInput(inputFile)

    if input:
        scanners = {}
        while input:
            s, b = readScanner(input)
            scanners[s] = b

        print(f'Solving {filename}')
        part1(scanners)

def main():
    solve('example.txt')
    solve('input.txt')

if __name__ == "__main__":
    main()
