"""
Dada una lista, genere otra lista eliminando el segundo elemento de forma repetida.
"""


def run(items: list) -> list:
    # Option 1
    # filter = []
    # for i in range(len(items)):
    #     if i % 2 == 0:
    #         filter.append(items[i])

    # Option 2
    filter = items[::2]
    return filter
