import sys

import pycheck

CHECK_CASES = [
    [['A131F7'], '(161,49,247)'],
    [['FF11FF'], '(255,17,255)'],
    [['123456'], '(18,52,86)'],
]


def run(hex_color: str) -> str:
    # TU CÓDIGO AQUÍ
    return rgb_color


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
