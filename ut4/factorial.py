# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


factorial(5)
