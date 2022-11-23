"""
Dada una lista de enteros y enteros como cadenas de texto, calcule la suma de todos los
valores de la lista como si todos sus elementos fueran números.
"""


def run(items: list) -> int:
    sum_items = []
    for item in items:
        int_item = int(item)
        sum_items.append(int_item)
    sum_items = sum(sum_items)
    return sum_items
