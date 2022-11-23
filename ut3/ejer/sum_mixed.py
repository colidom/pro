"""
Dada una lista de enteros y enteros como cadenas de texto, calcule la suma de todos los
valores de la lista como si todos sus elementos fueran números.
"""


def run(items: list) -> int:

    # Por comprención
    sum_items = sum([int(item) for item in items])

    # # Normal
    # sum_items = 0
    # for item in items:
    #     sum_items += int(item)
    return sum_items
