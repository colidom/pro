# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************


def count_vowels(text: str) -> int:
    VOWELS = "aeiou"

    # Condición de parada
    if len(text) == 0:
        return 0

    if text[0] in VOWELS:
        return count_vowels(text[1]) + 1
