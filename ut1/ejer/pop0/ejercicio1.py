import sys

import pycheck

CHECK_CASES = [
    [[31256], (8, 40, 56)],
    [[3601], (1, 0, 1)],
    [[9099], (2, 31, 39)],
]


def run(seconds: int) -> tuple:
    # TU CÓDIGO AQUÍ
    return hours, minutes, seconds


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
