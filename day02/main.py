#!/usr/bin/env python

import numpy as np


def parse_input(input_file):
    with open(input_file, "r") as f:
        return [[int(x) for x in line.split(sep=" ")] for line in f]


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


def part1(input):
    safe_reports = 0
    for report in input:
        report = np.array(report)
        safe_reports += check_report(report)
    return safe_reports


def check_singular_failure(line):
    for i in range(len(line)):
        _safe = check_report(np.delete(line, i))
        if np.all(_safe):
            return True
    return False


def part2(inp):
    safe_reports = 0
    for line in inp:
        line = np.array(line)
        safe = check_report(line)
        if not safe:
            safe = check_singular_failure(line)
        safe_reports += safe
    return safe_reports


if __name__ == "__main__":
    input = parse_input("input")
    print(part1(input))
    # print(part2(input))
