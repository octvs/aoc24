import sys

import numpy as np


def parse_input(inp):
    return tuple(part.splitlines() for part in inp.split("\n\n"))


def parse_rules(rules):
    _rules = np.array([[int(x) for x in line.split("|")] for line in rules])
    rules_matrix = np.zeros((_rules.max() + 1,) * 2, dtype=int)
    rules_matrix[_rules[:, 1], _rules[:, 0]] += 1
    return rules_matrix


def main(inp):
    rules_mat, updates = parse_rules(inp[0]), inp[1]
    sum = 0
    for update in updates:
        update_matrix = np.zeros_like(rules_mat)
        _update = [int(x) for x in update.split(",")]
        for i in range(len(_update) - 1):
            update_matrix[_update[i], _update[i + 1 :]] += 1
        if np.sum(rules_mat * update_matrix) == 0:
            sum += _update[len(_update) // 2]
    return sum


if __name__ == "__main__":
    input = parse_input(sys.stdin.read())
    print(main(input))
