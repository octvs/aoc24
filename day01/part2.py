import sys

import numpy as np

from part1 import parse_input


def main(inp):
    matches = inp[:, 0] == inp[:, 1][np.newaxis].T
    frequencies = matches.sum(axis=0)
    return np.sum(inp[:, 0] * frequencies)


if __name__ == "__main__":
    input = parse_input(sys.stdin.read())
    print(main(input))
