# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************


def count_vowels(text: str) -> int:
    VOWELS = "aeiou"

    if text[0] in VOWELS:
        return count_vowels(text[1:]) + 1
    return text[0]
