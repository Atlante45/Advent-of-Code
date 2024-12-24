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


def part2(state, instructions):
    s = []
    gates = {}
    igates = {}
    aliases = {}
    for a, b in instructions:
        x, op, y = a.split()
        x, y = sorted((x, y))
        gates[b] = (op, x, y)
        igates[(op, x, y)] = b
        if x.startswith("x"):
            assert y.startswith("y")
            assert x[1:] == y[1:]
            s.append((x, y, op, b))

            if not b.startswith("z"):
                aliases[b] = f"{'c' if op == 'AND' else 's'}{x[1:]}"

    bad_list = set(gates.keys())
    bad_units = list(range(1, 45))
    carry_ins = {}
    carry_outs = {}

    assert igates[("XOR", "x00", "y00")] == "z00"
    carry_outs[0] = igates[("AND", "x00", "y00")]
    carry_ins[45] = "z45"

    for i in range(1, 45):
        sum_i = igates[("XOR", f"x{i:02}", f"y{i:02}")]
        carry_i = igates[("AND", f"x{i:02}", f"y{i:02}")]
        op, ax, bx = gates[f"z{i:02}"]

        if op != "XOR":
            continue

        if ("AND", ax, bx) not in igates:
            continue

        intermediate = igates[("AND", ax, bx)]

        if sum_i not in [ax, bx]:
            continue

        carry_in = ax if bx == sum_i else bx

        ai, bi = sorted((intermediate, carry_i))
        if ("OR", ai, bi) not in igates:
            continue

        carry_out = igates[("OR", ai, bi)]
        carry_ins[i] = carry_in
        carry_outs[i] = carry_out

        bad_units.remove(i)
        bad_list.remove(f"z{i:02}")
        bad_list.remove(sum_i)
        bad_list.remove(carry_i)
        bad_list.remove(intermediate)

        if i - 1 in carry_outs and carry_outs[i - 1] == carry_in:
            bad_list.remove(carry_in)

    assert carry_outs[44] == carry_ins[45]

    bad_wires = []
    for i in bad_units:
        x_in = f"x{i:02}"
        y_in = f"y{i:02}"
        z_out = f"z{i:02}"
        carry_in = carry_outs[i - 1]
        carry_out = carry_ins[i + 1]

        sum_i = igates[("XOR", x_in, y_in)]
        carry_i = igates[("AND", x_in, y_in)]
        z_op, z_ax, z_bx = gates[z_out]
        co_op, co_ax, co_bx = gates[carry_out]

        if z_op != "XOR":
            # print(f"z{i:02} wrong op {z_op} instead of XOR")
            bad_wires.append(f"z{i:02}")

            wanted_gate = ("XOR", *sorted((carry_in, sum_i)))
            if wanted_gate in igates:
                bad_wires.append(igates[wanted_gate])
                # print(f"Found switched wires {z_out} <-> {igates[wanted_gate]}")
                continue

        else:
            if sum_i in [z_ax, z_bx] and carry_in not in [z_ax, z_bx]:
                # print(f"z{i:02} carry in wrong")
                bad_wires.append(carry_in)
            if sum_i not in [z_ax, z_bx] and carry_in in [z_ax, z_bx]:
                real_sum_i = z_ax if z_ax != carry_in else z_bx
                # print(f"z{i:02} sum_i wrong, should be {real_sum_i}")
                bad_wires.append(sum_i)
                bad_wires.append(real_sum_i)
                # print(f"Found switched wires {sum_i} <-> {real_sum_i}")

            if sum_i not in [z_ax, z_bx] and carry_in not in [z_ax, z_bx]:
                # print(f"z{i:02} wrong sum_i and carry_in not in z_ax, z_bx")
                bad_wires.append(f"z{i:02}")

        if co_op != "OR":
            # print(f"z{i:02} carry out wrong op {co_op} instead of OR")
            bad_wires.append(carry_ins[i + 1])
        else:
            pass

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
