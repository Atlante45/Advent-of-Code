from copy import deepcopy
import time
from solutions.utils.logger import logger


def test(module):
    passed = True
    test_data = getattr(module, "TEST_DATA", [])

    logger.info("tests:")
    for i, (data, results) in enumerate(test_data.items()):
        skip_1 = results[0] is None
        skip_2 = results[1] is None
        ans_1, ans_2, _, _ = solve(module, data, skip_1, skip_2)

        ico_1 = ico_2 = "⬜"
        if not skip_1:
            ico_1 = "✅" if ans_1 == results[0] else "❌"
        if not skip_2:
            ico_2 = "✅" if ans_2 == results[1] else "❌"
        message = f"    {i}. {ico_1} {ico_2}"
        if (ans_1, ans_2) != results:
            message += f" expected {results} got {(ans_1, ans_2)}"
            passed = False

        logger.info(message)

    return passed


def solve(module, data, skip_1=None, skip_2=None):
    if getattr(module, "parse", None) is not None:
        data = module.parse(data)
    else:
        data = data.splitlines()
    if not isinstance(data, tuple):
        data = (data,)

    ans_1 = ans_2 = None
    time_1 = time_2 = None
    if getattr(module, "parts", None) is not None:
        start = time.time()
        ans_1, ans_2 = module.parts(*data)
        time_2 = time.time() - start
    else:
        if not skip_1:
            start = time.time()
            ans_1 = module.part1(*deepcopy(data))
            time_1 = time.time() - start

        if not skip_2:
            start = time.time()
            ans_2 = module.part2(*data)
            time_2 = time.time() - start

    return ans_1, ans_2, time_1, time_2


def print_answer(part, answer, expected, time=None):
    if not isinstance(answer, str):
        answer = str(answer)
    if not isinstance(expected, str):
        expected = str(expected)

    suffix = ""
    if answer is not None and expected is not None:
        if answer == expected:
            suffix = " ✅"
        else:
            suffix = f" ❌ (expected {expected})"

    timing = f" {time:.3f}s".rjust(8) if time else ""

    logger.info(f"    Part {part + 1}: {answer.rjust(20)}{suffix.ljust(20)}{timing}")
