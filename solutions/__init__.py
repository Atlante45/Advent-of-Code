import importlib


def solve(year, day, data):
    mod_name = f"solutions.y{year}.d{day:02d}"
    mod = importlib.import_module(mod_name)
    return mod.solve(data)
