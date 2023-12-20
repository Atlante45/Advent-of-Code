from collections import defaultdict, deque
from math import lcm


def parse(data):
    modules = {}
    types = []
    outputs = []

    id = 0
    for line in data.splitlines():
        mod, out = line.split(" -> ")
        out = out.split(", ")

        modules[mod[1:] if mod != "broadcaster" else mod] = id
        types.append(mod[0] if mod != "broadcaster" else None)
        outputs.append(out)
        id += 1

    for line in data.splitlines():
        mod, out = line.split(" -> ")
        out = out.split(", ")
        for o in out:
            if o not in modules:
                modules[o] = id
                types.append(None)
                outputs.append([])
                id += 1

    inputs = []
    for i in range(len(modules)):
        inputs += [[]]

    for mod, id in modules.items():
        id = modules[mod]
        for out in outputs[id]:
            ido = modules[out]
            inputs[ido] += [mod]

    return modules, types, inputs, outputs


def simulate(modules, types, inputs, outputs, states):
    low_pulses = 0
    high_pulses = 0

    queue = deque()
    queue.append(("button", "broadcaster", False))
    low_pulses += 1

    while queue:
        snd, mod, pulse = queue.popleft()
        if mod not in modules:
            continue
        id = modules[mod]
        match types[id]:
            case None:
                for out in outputs[id]:
                    queue.append((mod, out, pulse))
                    if pulse:
                        high_pulses += 1
                    else:
                        low_pulses += 1
            case "%":
                if not pulse:
                    states[id] = not states[id]
                    for out in outputs[id]:
                        if states[id]:
                            queue.append((mod, out, True))
                            high_pulses += 1
                        else:
                            queue.append((mod, out, False))
                            low_pulses += 1
            case "&":
                ido = inputs[id].index(snd)
                states[id][ido] = pulse
                for out in outputs[id]:
                    if all(states[id]):
                        queue.append((mod, out, False))
                        low_pulses += 1
                    else:
                        queue.append((mod, out, True))
                        high_pulses += 1

    return low_pulses, high_pulses


def part1(modules, types, inputs, outputs):
    states = [False] * len(modules)
    for id, _ in enumerate(modules):
        if types[id] == "&":
            states[id] = [False] * len(inputs[id])

    low_pulses, high_pulses = 0, 0
    for _ in range(1000):
        low, high = simulate(modules, types, inputs, outputs, states)
        low_pulses += low
        high_pulses += high
    return low_pulses * high_pulses


def part2(modules, types, inputs, outputs):
    # Find relevant inputs into the rx module
    chain_ends = []
    for i in inputs[modules["rx"]]:
        for i2 in inputs[modules[i]]:
            for i3 in inputs[modules[i2]]:
                chain_ends += [i3]

    # Find each of the module chains from the broadcaster to the rx module
    links = defaultdict(list)
    ends = {}
    for start in outputs[modules["broadcaster"]]:
        curr = start
        while True:
            curr_out = outputs[modules[curr]]
            out = [o for o in curr_out if o not in chain_ends]
            if len(out) == 0:
                ends[start] = curr_out[0]
                break
            else:
                links[start] += out
            curr = out[0]

    # Find the cycle length for each module chains
    cycles = []
    for k, v in links.items():
        end = ends[k]
        cycle = 0
        for i, b in enumerate(v):
            if b in inputs[modules[end]]:
                cycle += 2 ** (i + 1)
        cycles += [cycle + 1]

    return lcm(*cycles)


TEST_DATA = {}
TEST_DATA[
    """\
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
""".rstrip()
] = (32000000, None)
TEST_DATA[
    """\
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
""".rstrip()
] = (11687500, None)
