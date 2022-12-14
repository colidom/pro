BASE = 2
# Solución 1
n = 10
result = []
for i in range(n + 1):
    result.append(BASE**i)
print(result)


# # No se puede usar funciones ya que no lo hemos dado
import sys

# Solución 2
n = 10
result = []


def powerof2(n):
    for i in range(n + 1):
        result.append(BASE**i)
    print(result)


powerof2(n)

# Solución 3
n = 10
exponent_number = [BASE**i for i in range(n + 1)]
print(exponent_number)
