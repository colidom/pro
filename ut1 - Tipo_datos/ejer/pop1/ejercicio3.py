import sys

import pycheck

CHECK_CASES = [
    [['e', 2, 'diferencia'], 'diforoncia'],
    [['u', -2, 'uruguay'], 'irigiay'],
    [['a', 4, 'anatolia'], 'unutoliu'],
]


def run(target_vowel: str, target_offset: int, input_text: str) -> str:
    # TU CÓDIGO AQUÍ
    return output_text


if __name__ == '__main__':
    pycheck.check(run, CHECK_CASES, sys.argv)
