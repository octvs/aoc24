import sys

import numpy as np

from part1 import find_substring, parse_input

TARGET = "MAS"


def check_diagonal(inp):
    all_mids = np.zeros_like(inp, dtype=bool)
    for i in range(len(TARGET) - inp.shape[1], inp.shape[0] - len(TARGET) + 1):
        diag = "".join(np.diag(inp, i))
        midpoints = []
        midpoints += find_substring(diag, TARGET)
        midpoints += find_substring(diag, TARGET[::-1])
        if midpoints:
            idx = np.zeros(len(diag), dtype=bool)
            idx[np.array(midpoints) + 1] += True
            all_mids += np.diagflat(idx, i)
    return all_mids


def main(inp):
    pattern_lr = check_diagonal(inp)
    pattern_rl = np.fliplr(check_diagonal(np.fliplr(inp)))
    return np.sum(pattern_lr & pattern_rl)


if __name__ == "__main__":
    input = parse_input(sys.stdin.read())
    print(main(input))
