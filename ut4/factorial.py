# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    val = n
    if val == 0:
        return 1
    elif val == -1:
        return None

    for i in range(1, val):
        val *= i
    return val
