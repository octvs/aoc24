import re
import sys


def main(inp):
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    return sum([int(a) * int(b) for a, b in pattern.findall(inp)])


if __name__ == "__main__":
    print(main(sys.stdin.read()))
