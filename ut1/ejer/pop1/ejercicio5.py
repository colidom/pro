import sys

import pycheck

CHECK_CASES = [
    [['hola probando'], 'hola-probando'],
    [['áéíóú'], 'aeiou'],
    [['TWIST & SHOUT'], 'twist-&-shout'],
]


def run(text: str) -> str:
    # TU CÓDIGO AQUÍ
    return slug


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
