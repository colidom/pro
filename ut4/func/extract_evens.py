# *******************
# EXTRACCIÓN DE PARES
# *******************


def run(values: int) -> list:
    evens = [value for value in values if value % 2 == 0]

    return evens
