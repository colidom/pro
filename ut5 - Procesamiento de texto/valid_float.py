import re

# 3. Escriba un programa en Python que indique si un determinado número es o no un flotante válido en Python.

number = 3.14
regular_expression = r"\d+\.\d+"


def valid_float(num):
    return re.findall(regular_expression, num)


float_num = valid_float(number)
print(f"Correct emails finded: {float_num} \n")
