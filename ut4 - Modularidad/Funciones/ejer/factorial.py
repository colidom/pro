# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    if n < 0:
        result = None
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
    return result
