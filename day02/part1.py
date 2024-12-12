import sys

import numpy as np


def parse_input(inp):
    return [[int(x) for x in line.split(sep=" ")] for line in inp.splitlines()]


def get_diff(line):
    window = np.eye(len(line))
    shifted = np.roll(window, shift=1, axis=1)
    return (window - shifted)[:-1] @ line


def check_report(line):
    diff = get_diff(line)
    trend = diff >= 0
    if np.average(trend) < 0.5:
        trend = ~trend
    return np.all(trend & (abs(diff) >= 1) & (abs(diff) <= 3))


def main(input):
    safe_reports = 0
    for report in input:
        safe_reports += check_report(np.array(report))
    return safe_reports


if __name__ == "__main__":
    input = parse_input(sys.stdin.read())
    print(main(input))
