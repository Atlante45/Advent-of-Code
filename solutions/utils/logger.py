def debug_name(name, debug):
    if debug:
        print(f"Solving {name}")


def debug_part(index, value, result, debug):
    if not debug or value is None:
        return

    prefix = ""
    suffix = ""
    if result is not None and result[index] is not None:
        if value == result[index]:
            prefix = "✅ "
        else:
            prefix = "❌ "
            suffix = f" (expected {result[index]})"

    print(f"    Part {index + 1}: {prefix}{value}{suffix}")
