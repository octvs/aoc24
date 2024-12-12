import re
import sys

import numpy as np


def parse_input(inp):
    pattern = re.compile(r"^(\d+)\s{3}(\d+)")
    inp = [
        [int(nr) for nr in pattern.match(line).groups()]
        for line in inp.splitlines()
    ]
    return np.asarray(inp)


def main(inp):
    return np.sum(np.abs(np.sort(inp[:, 0]) - np.sort(inp[:, 1])))


if __name__ == "__main__":
    input = parse_input(sys.stdin.read())
    print(main(input))
