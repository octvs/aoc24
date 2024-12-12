import sys

import numpy as np

from part1 import check_report, parse_input


def check_singular_failure(line):
    for i in range(len(line)):
        _safe = check_report(np.delete(line, i))
        if np.all(_safe):
            return True
    return False


def main(inp):
    safe_reports = 0
    for line in inp:
        line = np.array(line)
        safe = check_report(line)
        if not safe:
            safe = check_singular_failure(line)
        safe_reports += safe
    return safe_reports


if __name__ == "__main__":
    input = parse_input(sys.stdin.read())
    print(main(input))
