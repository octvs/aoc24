import sys

import numpy as np
from part1 import check_update, parse_input, parse_rules


def swap_elements(array, cond):
    x0, x1 = list(zip(*np.where(cond)))[0]
    i0 = np.where(array == x0)
    i1 = np.where(array == x1)
    array[i0], array[i1] = x1, x0
    return array


def main(inp, sum=0):
    rules_mat, updates = parse_rules(inp[0]), inp[1]
    for update in updates:
        _update = np.array([int(x) for x in update.split(",")])
        fault = check_update(_update, rules_mat)
        if not np.any(fault):
            continue
        else:
            while np.sum(fault) > 0:
                _update = swap_elements(_update, fault)
                fault = check_update(_update, rules_mat)
            sum += _update[len(_update) // 2]
    return sum


if __name__ == "__main__":
    input = parse_input(sys.stdin.read())
    print(main(input))
