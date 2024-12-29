def parse(data):
    return data.splitlines()


def walk(seq):
    x, y = 0, 0
    i = 0
    while i < len(seq):
        if seq[i] == "e":
            x += 1
            i += 1
        elif seq[i] == "w":
            x -= 1
            i += 1
        elif seq[i : i + 2] == "ne":
            y += 1
            i += 2
        elif seq[i : i + 2] == "nw":
            y += 1
            x -= 1
            i += 2
        elif seq[i : i + 2] == "se":
            y -= 1
            x += 1
            i += 2
        elif seq[i : i + 2] == "sw":
            y -= 1
            i += 2
        else:
            raise ValueError(f"Invalid sequence: {seq}")
    assert i == len(seq)

    return x, y


def neighbors(x, y):
    return set(
        [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
            (x - 1, y + 1),
            (x + 1, y - 1),
        ]
    )


def parts(lines):
    tiles = set()
    for line in lines:
        x, y = walk(line)
        if (x, y) in tiles:
            tiles.remove((x, y))
        else:
            tiles.add((x, y))

    p1 = len(tiles)

    for _ in range(100):
        new_tiles = set()
        to_check = set()

        for tile in tiles:
            ns = neighbors(*tile)
            to_check.update(ns)
            if len(ns & tiles) in [1, 2]:
                new_tiles.add(tile)

        for tile in to_check:
            ns = neighbors(*tile)
            if len(ns & tiles) == 2:
                new_tiles.add(tile)

        tiles = new_tiles

    p2 = len(tiles)

    return p1, p2


TEST_DATA = {}
TEST_DATA[
    """\
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
""".rstrip()
] = (10, 2208)
