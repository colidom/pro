import sys

import pycheck

CHECK_CASES = [
    [[99], 4],
    [[201], 4],
    [[3219], 6],
]


def run(number: int) -> int:
    # TU CÓDIGO AQUÍ
    return count_ones


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
