import sys

import numpy as np


def parse_input(inp):
    _map = {".": 0, "#": 1, "^": 2}
    _inp = np.array([[_map[ch] for ch in li] for li in inp.splitlines()])
    _obj = np.array(np.where(_inp == 1)) - np.array(np.where(_inp == 2))
    _obj[0] *= -1  # rotate x axis to be pos up
    return _obj.T


def objects_ahead(objects):
    return objects[(objects[:, 1] == 0) & (objects[:, 0] > 0)]


def turn_to_right(objects):
    objects[:, 0] *= -1
    return objects[:, [1, 0]]


def move_till(objects, dst, moves):
    objects[:, 0] -= dst - 1
    moves.append(dst - 1)
    return objects, moves


def move_forward(objs, moves=[]):
    objs, moves = move_till(objs, np.min(objects_ahead(objs)[:, 0]), moves)
    objs = turn_to_right(objs)
    if np.any(objects_ahead(objs)):
        objs, moves = move_forward(objs, moves)
    else:
        objs, moves = move_till(objs, np.max(objs[:, 0]) + 1, moves)
    return objs, moves


def check_unique_locs(moves):
    dir = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])
    traj = [[0, 0]]
    for i, step in enumerate(moves):
        for st in range(step):
            traj.append(traj[-1] + dir[i % 4])
    return np.unique(traj, axis=0).shape[0]


def main(inp):
    _, moves = move_forward(inp)
    return check_unique_locs(moves)


if __name__ == "__main__":
    input = parse_input(sys.stdin.read())
    print(main(input))
