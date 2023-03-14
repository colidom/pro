# ****************************
# DECORANDO LA SUMA DE VALORES
# ****************************
"""
En este ejercicio el dato de entrada es una lista "supuestamente" de valores enteros. Debe crear una función 
que sume los valores de dicha lista, pero con ciertos matices:

1.  La función principal debe chequear que todos los valores de la lista sean valores enteros. Si alguno no es 
entero esto supone un error. Usar la función is_instance() para la comprobación de tipos.                                                                 │
2.  La función principal debe devolver dos valores (como una tupla):                                                                    │
  • El primero es el estado: True si todo fue bien o False si hubo algún error.                                                      │
  • El segundo es el resultado: Si todo fue bien devolver la suma de los valores, si hubo algún error devolver 
  la cadena "Not int value found".
3. Se debe crear una función auxiliar (decorador) llamada result_as_status() que convierta la salida de la función principal en un     │
  diccionario con claves status y result.  
"""

def run():
    # TU CÓDIGO AQUÍ

