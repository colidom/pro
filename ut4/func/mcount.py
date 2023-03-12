# *******************
# CONTANDO SIN CONTAR
# *******************


def mcount(items: tuple[int], target: int) -> int:
    """
    Cuenta el número de veces que aparece un valor determinado en una tupla.

    Args:
        t (tuple[int]): La tupla de valores enteros.
        value (int): El valor a contar en la tupla.

    Returns:
        int: El número de veces que aparece el valor en la tupla.
    """
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count
