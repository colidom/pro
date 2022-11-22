import sys

BASE = 2
n = 3
result = []


def powerof2(n):
    for i in range(n):
        result.append(BASE**i)
        print(result)


powerof2(n)
