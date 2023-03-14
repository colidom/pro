# *****************
# SUMA DE COCIENTES
# *****************


def sum_quot(n: int) -> float:
    if n == 1:
        return 1
    return 1 / +sum_quot(n - 1)
