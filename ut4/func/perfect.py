# *****************
# NÚMEROS PERFECTOS
# *****************


def is_perfect(n: int) -> bool:
    operation = 0
    for i in range(1, n):
        if n % i == 0:
            operation += i
        if n == operation:
            return True
    return False
