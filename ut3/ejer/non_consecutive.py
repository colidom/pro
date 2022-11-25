"""
El objetivo es encontrar el primer número no consecutivo dentro de una lista de valores
numéricos enteros. Si todos los valores son consecutivos entonces el resultado es None.
"""


def run(values: list) -> int:
    target = values[0]
    for value in values:
        if target >= value:
            target = value + 1
        else:
            target = value
            break

    return target


if __name__ == "__main__":
    run([1, 2, 3, 4, 6, 7, 8])
