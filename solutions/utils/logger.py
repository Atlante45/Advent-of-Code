import logging

logging.basicConfig(
    format="%(asctime)s.%(msecs)03d %(message)s",
    datefmt="%H:%M:%S",
    encoding="utf-8",
    level=logging.WARNING,
)

logger = logging.getLogger("aoc")
