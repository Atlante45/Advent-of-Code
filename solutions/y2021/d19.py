from solutions.utils import logger
from aocd import data

from collections import defaultdict
import math
import re
from scipy.spatial.transform import Rotation


def dist(a, b):
    return math.sqrt(sum([(a_i - b_i) ** 2 for a_i, b_i in zip(a, b)]))


def sub(a, b):
    return [a_i - b_i for a_i, b_i in zip(a, b)]


def add(a, b):
    return [a_i + b_i for a_i, b_i in zip(a, b)]


def parts(scanners):
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

    mapped = {"0": {"trl": [0, 0, 0], "rot": Rotation.from_euler("x", 0, degrees=True)}}
    unmapped = [s for s in scanners if s != "0"]

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
                        "trl": [
                            round(v)
                            for v in add(
                                mapped[s1]["trl"], mapped[s1]["rot"].apply(trl)
                            )
                        ],
                        "rot": mapped[s1]["rot"] * rot,
                    }
                    unmapped.remove(s2)
                    break

    beacons = set()
    for v in scanners["0"]:
        beacons.add((v[0], v[1], v[2]))

    for s in [s for s in scanners if s != "0"]:
        for b in scanners[s]:
            trl = mapped[s]["trl"]
            rot = mapped[s]["rot"]
            v = [round(v) for v in add(trl, rot.apply(b))]
            beacons.add((v[0], v[1], v[2]))

    # print(sorted(beacons))

    maxDist = 0
    for i in range(len(mapped) - 1):
        for j in range(i + 1, len(mapped)):
            v1 = mapped[str(i)]["trl"]
            v2 = mapped[str(j)]["trl"]
            maxDist = max(maxDist, sum([abs(j - i) for i, j in zip(v1, v2)]))

    return len(beacons), maxDist


def readScanner(input):
    scanner = re.search("^--- scanner ([0-9]*) ---", input.pop(0)).group(1)
    beacons = []

    line = input.pop(0).strip()
    while line:
        beacons.append([int(v) for v in line.strip().split(",")])
        line = input.pop(0).strip() if input else ""

    return scanner, beacons


def solve(data, name="input", result=None, debug=False):
    logger.debug_name(name, debug)

    input = data.splitlines()
    scanners = {}
    while input:
        s, b = readScanner(input)
        scanners[s] = b

    ans_1, ans_2 = parts(scanners)
    logger.debug_part(0, ans_1, result, debug)
    logger.debug_part(1, ans_2, result, debug)

    return ans_1, ans_2


INPUT_RESULT = (315, 13192)
TEST_RESULT = (79, 3621)
TEST_DATA = """\
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
""".rstrip()

if __name__ == "__main__":
    solve(TEST_DATA, name="example", result=TEST_RESULT, debug=True)
    solve(data, name="input", result=INPUT_RESULT, debug=True)
