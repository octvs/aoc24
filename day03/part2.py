import re
import sys

from part1 import main as part1


def main(inp):
    dont_pattern = re.compile(r"don't\(\).*?do\(\)", flags=re.DOTALL)
    while match := dont_pattern.search(inp):
        inp = inp[: match.start()] + inp[match.end() :]
    trailing_dont_pattern = re.compile(r"don't\(\).*", flags=re.DOTALL)
    if match := trailing_dont_pattern.search(inp):
        inp = inp[: match.start()] + inp[match.end() :]
    return part1(inp)


if __name__ == "__main__":
    print(main(sys.stdin.read()))
