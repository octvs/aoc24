#!/usr/bin/env python

import re

import numpy as np


def parse_input(input_file):
    pattern = re.compile(r"^(\d+)\s{3}(\d+)")
    with open(input_file, "r") as f:
        inp = [[int(nr) for nr in pattern.match(line).groups()] for line in f]
    return np.asarray(inp)


def part1(inp):
    return np.sum(np.abs(np.sort(inp[:, 0]) - np.sort(inp[:, 1])))


def part2(inp):
    matches = inp[:, 0] == inp[:, 1][np.newaxis].T
    frequencies = matches.sum(axis=0)
    return np.sum(inp[:, 0] * frequencies)


if __name__ == "__main__":
    input = parse_input("input")
    # print(part1(input))
    print(part2(input))
