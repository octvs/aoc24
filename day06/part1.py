import sys

import numpy as np

DIRS = tuple(np.array(x) for x in [[-1, 0], [0, 1], [1, 0], [0, -1]])


def parse_input(inp):
    # Assume the guard always starts facing north
    _map = {".": 0, "#": 2, "^": 3}
    return np.array([[_map[ch] for ch in line] for line in inp.splitlines()])


def mark_path(inp, a, b):
    diff = np.array(b) - np.array(a)
    move_axis = np.nonzero(diff)[0][0]
    dir = int(diff[move_axis] / abs(diff[move_axis]))
    _idx = list(a)
    _idx[move_axis] = slice(a[move_axis], b[move_axis], dir)
    inp[tuple(_idx)] = 1
    return inp


def move(inp, loc, direction):
    print(inp)
    print(type(loc))
    [axis], [dir] = np.where(direction != 0)[0], direction[direction != 0]
    path = inp.take(loc[1 - axis], 1 - axis)[loc[axis] + dir :: dir]
    blocks_ahead = list(*np.where(path == 2))
    if not blocks_ahead:
        print("Gonna leave")
        new_loc = list(loc)
        _val = int((inp.shape[axis] - 1) * (1 + dir) / 2)  # 0 if dir==-1
        new_loc[axis] = _val
        new_loc = tuple(new_loc)
        inp = mark_path(inp, loc, new_loc)
        inp[new_loc] = 1
        return inp
    new_loc = tuple(loc + direction * blocks_ahead[0])
    inp = mark_path(inp, loc, new_loc)
    inp[new_loc] = 3
    return inp


def main(inp):
    dir = 0
    while loc := list(zip(*np.where(inp == 3))):
        inp = move(inp, loc[0], DIRS[dir % 4])
        dir += 1
    print(inp)
    return np.sum(inp == 1)


if __name__ == "__main__":
    input = parse_input(sys.stdin.read())
    print(main(input))
