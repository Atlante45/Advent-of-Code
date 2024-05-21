from collections import defaultdict


def parse(data):
    return data.splitlines()


def part1(lines):
    registers = defaultdict(int)
    last_sound = None
    pos = 0

    def get_value(val):
        try:
            return int(val)
        except ValueError:
            return registers[val]

    while 0 <= pos < len(lines):
        instr = lines[pos].split()
        match instr[0]:
            case "snd":
                last_sound = get_value(instr[1])
            case "set":
                registers[instr[1]] = get_value(instr[2])
            case "add":
                registers[instr[1]] += get_value(instr[2])
            case "mul":
                registers[instr[1]] *= get_value(instr[2])
            case "mod":
                registers[instr[1]] %= get_value(instr[2])
            case "rcv":
                if get_value(instr[1]) != 0:
                    return last_sound
            case "jgz":
                if get_value(instr[1]) > 0:
                    pos += get_value(instr[2])
                    continue
        pos += 1

    return None


class Program:
    def __init__(self, id, lines, send_queue, recv_queue):
        self.registers = defaultdict(int)
        self.registers["p"] = id
        self.lines = lines
        self.pos = 0
        self.sent = 0
        self.send_queue = send_queue
        self.recv_queue = recv_queue

    def get_value(self, val):
        try:
            return int(val)
        except ValueError:
            return self.registers[val]

    def run(self):
        while 0 <= self.pos < len(self.lines):
            instr = self.lines[self.pos].split()
            match instr[0]:
                case "snd":
                    self.send_queue.append(self.get_value(instr[1]))
                    self.sent += 1
                case "set":
                    self.registers[instr[1]] = self.get_value(instr[2])
                case "add":
                    self.registers[instr[1]] += self.get_value(instr[2])
                case "mul":
                    self.registers[instr[1]] *= self.get_value(instr[2])
                case "mod":
                    self.registers[instr[1]] %= self.get_value(instr[2])
                case "rcv":
                    if not self.recv_queue:
                        return
                    self.registers[instr[1]] = self.recv_queue.pop(0)
                case "jgz":
                    if self.get_value(instr[1]) > 0:
                        self.pos += self.get_value(instr[2])
                        continue
            self.pos += 1


def part2(lines):
    q0 = []
    q1 = []
    p0 = Program(0, lines, q0, q1)
    p1 = Program(1, lines, q1, q0)

    while True:
        p0.run()
        p1.run()
        if not q1:
            break

    return p1.sent


TEST_DATA = {}
TEST_DATA[
    """\
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
""".rstrip()
] = (4, None)
