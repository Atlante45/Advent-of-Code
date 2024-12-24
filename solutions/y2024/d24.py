def parse(data):
    state, instructions = data.split("\n\n")
    state = state.split("\n")
    instructions = instructions.split("\n")
    state = [line.split(": ") for line in state]
    instructions = [line.split(" -> ") for line in instructions]
    return state, instructions


def part1(state, instructions):
    vals = {}
    for line in state:
        vals[line[0]] = True if line[1] == "1" else False

    while instructions:
        for line in instructions:
            a, op, b = line[0].split()

            if a in vals and b in vals:
                if op == "AND":
                    vals[line[1]] = vals[a] and vals[b]
                elif op == "OR":
                    vals[line[1]] = vals[a] or vals[b]
                elif op == "XOR":
                    vals[line[1]] = vals[a] != vals[b]
                instructions.remove(line)
                break

    zs = sorted(i for i in vals.keys() if i.startswith("z"))
    res = 0
    for i in reversed(zs):
        res *= 2
        res += 1 if vals[i] else 0
    return res


def analyze_adder(i, gates, igates):
    sum_i = igates[("XOR", f"x{i:02}", f"y{i:02}")]
    carry_i = igates[("AND", f"x{i:02}", f"y{i:02}")]
    op, ax, bx = gates[f"z{i:02}"]

    if op != "XOR":
        return False, None, None

    if ("AND", ax, bx) not in igates:
        return False, None, None

    intermediate = igates[("AND", ax, bx)]

    if sum_i not in [ax, bx]:
        return False, None, None

    carry_in = ax if bx == sum_i else bx

    ai, bi = sorted((intermediate, carry_i))
    if ("OR", ai, bi) not in igates:
        return False, None, None

    carry_out = igates[("OR", ai, bi)]

    return True, carry_in, carry_out


def find_bad_wires(i, carry_in, carry_out, gates, igates):
    x_in = f"x{i:02}"
    y_in = f"y{i:02}"
    z_out = f"z{i:02}"

    sum_i = igates[("XOR", x_in, y_in)]
    z_op, z_ax, z_bx = gates[z_out]

    if z_op != "XOR":
        # print(f"z{i:02} wrong op {z_op} instead of XOR")
        wanted_gate = igates[("XOR", *sorted((carry_in, sum_i)))]
        # print(f"Found switched wires {z_out} <-> {igates[wanted_gate]}")
        return z_out, wanted_gate

    if sum_i not in [z_ax, z_bx] and carry_in in [z_ax, z_bx]:
        real_sum_i = z_ax if z_ax != carry_in else z_bx
        # print(f"z{i:02} sum_i wrong, should be {real_sum_i}")
        # print(f"Found switched wires {sum_i} <-> {real_sum_i}")
        return sum_i, real_sum_i

    # carry_i = igates[("AND", x_in, y_in)]
    # co_op, co_ax, co_bx = gates[carry_out]
    # if sum_i in [z_ax, z_bx] and carry_in not in [z_ax, z_bx]:
    #     # print(f"z{i:02} carry in wrong")
    #     bad_wires.append(carry_in)
    # if sum_i not in [z_ax, z_bx] and carry_in not in [z_ax, z_bx]:
    #     # print(f"z{i:02} wrong sum_i and carry_in not in z_ax, z_bx")
    #     bad_wires.append(f"z{i:02}")

    raise ValueError(f"No bad wires found for {i}")


def check_fix(i, pair, gates, igates):
    g = gates.copy()
    ig = igates.copy()
    # swap the wires
    g[pair[0]], g[pair[1]] = g[pair[1]], g[pair[0]]
    ig[g[pair[0]]] = pair[0]
    ig[g[pair[1]]] = pair[1]

    ok, _, _ = analyze_adder(i, g, ig)
    assert ok


def part2(state, instructions):
    gates = {}
    igates = {}
    for a, b in instructions:
        x, op, y = a.split()
        x, y = sorted((x, y))

        gates[b] = (op, x, y)
        igates[(op, x, y)] = b

    bad_units = []
    carry_ins = {}
    carry_outs = {}

    assert igates[("XOR", "x00", "y00")] == "z00"
    carry_outs[0] = igates[("AND", "x00", "y00")]
    carry_ins[45] = "z45"

    for i in range(1, 45):
        ok, carry_in, carry_out = analyze_adder(i, gates, igates)
        if ok:
            carry_ins[i] = carry_in
            carry_outs[i] = carry_out
        else:
            bad_units.append(i)

    assert carry_outs[44] == carry_ins[45]

    bad_wires = []
    for i in bad_units:
        carry_in = carry_outs[i - 1]
        carry_out = carry_ins[i + 1]
        pair = find_bad_wires(i, carry_in, carry_out, gates, igates)

        # Confirms each swaps confined to a single unit
        # check_fix(i, pair, gates, igates)

        bad_wires.extend(pair)

    return ",".join(sorted(bad_wires))


TEST_DATA = {}
TEST_DATA[
    """\
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
""".rstrip()
] = (2024, None)
