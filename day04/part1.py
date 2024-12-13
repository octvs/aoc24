import sys

import numpy as np

TARGET = "XMAS"


def parse_input(inp):
    return np.array([list(line) for line in inp.splitlines()])


def find_substring(line, target):
    indx = []
    while (i_match := line.find(target)) != -1:
        line = line.replace(target, "0" * len(target), 1)
        indx.append(i_match)
    return indx


def check_horizontal(inp, count=0):
    for i_row in range(inp.shape[0]):
        row = "".join(inp[i_row])
        count += len(find_substring(row, TARGET))
        count += len(find_substring(row, TARGET[::-1]))
    return count


def check_diagonal(inp, count=0):
    for i in range(len(TARGET) - inp.shape[1], inp.shape[0] - len(TARGET) + 1):
        diag = "".join(np.diag(inp, i))
        count += len(find_substring(diag, TARGET))
        count += len(find_substring(diag, TARGET[::-1]))
    return count


def main(inp):
    count = check_horizontal(inp, 0)
    count = check_horizontal(inp.T, count)
    count = check_diagonal(inp, count)
    count = check_diagonal(np.fliplr(inp), count)
    return count


if __name__ == "__main__":
    input = parse_input(sys.stdin.read())
    print(main(input))
