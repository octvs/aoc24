import sys

import numpy as np
from part1 import descending, parse_input, parse_rules


def main(inp, sum=0):
    rules_mat, updates = parse_rules(inp[0]), inp[1]
    for update in updates:
        _update = np.array([int(x) for x in update.split(",")])
        _rule_sum = np.sum(1 - rules_mat[_update][:, _update], axis=1)
        if not descending(_rule_sum):
            _update = _update[np.argsort(-_rule_sum)]
            sum += _update[len(_update) // 2]
    return sum


if __name__ == "__main__":
    input = parse_input(sys.stdin.read())
    print(main(input))
