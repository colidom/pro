"""
Dada una lista, genere otra lista eliminando el segundo elemento de forma repetida.
"""


def run(items: list) -> list:
    filter = []
    for i in range(len(items)):
        if i % 2 == 0:
            filter.append(items[i])
    return filter
