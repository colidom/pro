import sys

import pycheck

CHECK_CASES = [
    [['GGTTACCAACCCAGTCGAAAATTTGGTCAGGG'], (28.125, 28.125, 21.875, 21.875)],
    [['ATGGGATCCTAGCCCCTTAG'], (20.0, 25.0, 25.0, 30.0)],
    [['GGATTCTGAGAATCCGCTAATGCC'], (25.0, 25.0, 25.0, 25.0)],
]


def run(adn: str):
    # TU CÓDIGO AQUÍ
    return adenines_rate, guanines_rate, thymines_rate, cytosines_rate


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
