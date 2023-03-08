# *****************
# NÚMEROS PERFECTOS
# *****************


def is_perfect(n: int) -> bool:
    div = own_divisors(n)
    operation = 0
    for i in div:
        operation += i
    if n == operation:
        return True
    else:
        return False


def own_divisors(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return divisors
