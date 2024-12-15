import sys

import numpy as np


def parse_input(inp):
    return tuple(part.splitlines() for part in inp.split("\n\n"))


def parse_rules(rules):
    _rules = np.array([[int(x) for x in line.split("|")] for line in rules])
    rules_matrix = np.zeros((_rules.max() + 1,) * 2, dtype=int)
    rules_matrix[_rules[:, 1], _rules[:, 0]] += 1
    return rules_matrix


def descending(arr):
    return np.all(arr[:-1] >= arr[1:])


def main(inp, sum=0):
    rules_mat, updates = parse_rules(inp[0]), inp[1]
    for update in updates:
        _update = np.array([int(x) for x in update.split(",")])
        _rule_sum = np.sum(1 - rules_mat[_update][:, _update], axis=1)
        if descending(_rule_sum):
            sum += _update[len(_update) // 2]
    return sum


if __name__ == "__main__":
    input = parse_input(sys.stdin.read())
    print(main(input))
