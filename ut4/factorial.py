# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    if n < 0:
        val = None
    else:
        val = 1
        for i in range(2, n + 1):
            val *= i
    return val
