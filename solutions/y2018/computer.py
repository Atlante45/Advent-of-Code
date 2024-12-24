def execute(op, a, b, registers):
    match op:
        case "addr":
            return registers[a] + registers[b]
        case "addi":
            return registers[a] + b
        case "mulr":
            return registers[a] * registers[b]
        case "muli":
            return registers[a] * b
        case "banr":
            return registers[a] & registers[b]
        case "bani":
            return registers[a] & b
        case "borr":
            return registers[a] | registers[b]
        case "bori":
            return registers[a] | b
        case "setr":
            return registers[a]
        case "seti":
            return a
        case "gtir":
            return 1 if a > registers[b] else 0
        case "gtri":
            return 1 if registers[a] > b else 0
        case "gtrr":
            return 1 if registers[a] > registers[b] else 0
        case "eqir":
            return 1 if a == registers[b] else 0
        case "eqri":
            return 1 if registers[a] == b else 0
        case "eqrr":
            return 1 if registers[a] == registers[b] else 0
        case _:
            raise ValueError(f"Invalid instruction: {op}")


def debug(ip, ip_reg, op, a, b, c):
    a_str = f"r{a}" if a != ip_reg else f"{ip}"
    b_str = f"r{b}" if b != ip_reg else f"{ip}"
    c_str = f"r{c}" if c != ip_reg else f"{ip}"

    match op:
        case "addr":
            if b == c:
                a, b = b, a
                a_str, b_str = b_str, a_str

            if c == a:
                if c == ip_reg:
                    return f"jmp {ip + 1} + {b_str}"
                else:
                    return f"{c_str} += {b_str}"
            else:
                if c == ip_reg:
                    return f"jmp {a_str} + {b_str} + 1"
                else:
                    return f"{c_str} = {a_str} + {b_str}"
        case "addi":
            if a == c:
                if c == ip_reg:
                    return f"jmp {ip + b + 1}"
                else:
                    return f"{c_str} += {b}"
            else:
                if c == ip_reg:
                    return f"jmp {a_str} + {b} + 1"
                else:
                    return f"{c_str} = {a_str} + {b}"
        case "mulr":
            if b == c:
                a, b = b, a
                a_str, b_str = b_str, a_str

            if c == a:
                if c == ip_reg:
                    return f"jmp {(ip * ip) + 1}"
                else:
                    return f"{c_str} *= {b_str}"
            else:
                if c == ip_reg:
                    return f"jmp {a_str} * {b_str} + 1"
                else:
                    return f"{c_str} = {a_str} * {b_str}"
        case "muli":
            if a == c:
                if c == ip_reg:
                    return f"jmp {(ip * b) + 1}"
                else:
                    return f"{c_str} *= {b}"
            else:
                if c == ip_reg:
                    return f"jmp ({a_str} * {b}) + 1"
                else:
                    return f"{c_str} = {a_str} * {b}"
        case "banr":
            if b == c:
                a, b = b, a
                a_str, b_str = b_str, a_str

            if c == a:
                return f"{c_str} &= {b_str}"
            else:
                return f"{c_str} = {a_str} & {b_str}"
        case "bani":
            if a == c:
                return f"{c_str} &= {b}"
            else:
                return f"{c_str} = {a_str} & {b}"
        case "borr":
            if b == c:
                a, b = b, a
                a_str, b_str = b_str, a_str

            if c == a:
                return f"{c_str} |= {b_str}"
            else:
                return f"{c_str} = {a_str} | {b_str}"
        case "bori":
            if a == c:
                return f"{c_str} |= {b}"
            else:
                return f"{c_str} = {a_str} | {b}"
        case "setr":
            if c == ip_reg:
                return f"jmp {a_str} + 1"
            else:
                return f"{c_str} = {a_str}"
        case "seti":
            if c == ip_reg:
                return f"jmp {a + 1}"
            else:
                return f"{c_str} = {a}"
        case "gtir":
            if c == ip_reg:
                raise ValueError(f"Invalid instruction: {op} assigns to ip_reg")

            return f"{c_str} = 1 if {a} > {b_str} else 0"
        case "gtri":
            if c == ip_reg:
                raise ValueError(f"Invalid instruction: {op} assigns to ip_reg")
            return f"{c_str} = 1 if {a_str} > {b} else 0"
        case "gtrr":
            if c == ip_reg:
                raise ValueError(f"Invalid instruction: {op} assigns to ip_reg")
            return f"{c_str} = 1 if {a_str} > {b_str} else 0"
        case "eqir":
            if c == ip_reg:
                raise ValueError(f"Invalid instruction: {op} assigns to ip_reg")
            return f"{c_str} = 1 if {a} == {b_str} else 0"
        case "eqri":
            if c == ip_reg:
                raise ValueError(f"Invalid instruction: {op} assigns to ip_reg")
            return f"{c_str} = 1 if {a_str} == {b} else 0"
        case "eqrr":
            if c == ip_reg:
                raise ValueError(f"Invalid instruction: {op} assigns to ip_reg")
            return f"{c_str} = 1 if {a_str} == {b_str} else 0"
        case _:
            return f"Invalid instruction: {op}"
            raise ValueError(f"Invalid instruction: {op}")


def print_program(ip, program):
    registers = [0, 0, 0, 0, 0, 0]
    ip_reg = ip
    ip = 0
    while ip < len(program):
        op, a, b, c = program[ip]
        print(f"{ip:02d}: {debug(ip, ip_reg, op, a, b, c)}")
        ip += 1
    return registers[0]
