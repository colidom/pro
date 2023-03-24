# *******************
# GENERANDO CUADRADOS
# *******************


def gen_sq(n: int) -> list:
    evens_gen = (i**2 for i in range(0, n))
    return list(evens_gen)
