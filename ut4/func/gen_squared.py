# *******************
# GENERANDO CUADRADOS
# *******************
""" 
Escriba una función que reciba un parámetro n y que incluya una expresión generadora para calcular los n primeros números enteros elevados al cuadrado.                                          │
│                                                                                                                                                                                                  │
│ Notas:                                                                                                                                                                                           │
│                                                                                                                                                                                                  │
│  • La función debe devoler una lista de los valores al cuadrado.                                                                                                                                 │
│  • n ∈ {0, ℤ+}  
 """


def gen_sq(n: int) -> list:
    evens_gen = (i**2 for i in range(0, n))
    result = [i for i in evens_gen]
    return result
