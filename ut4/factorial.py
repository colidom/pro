# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    result = n
    if n == 0:
        return 1

    for i in range(1, result):
        result *= i
    return result
