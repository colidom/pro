""" 
Dada una variable year con un valor entero, compruebe si dicho año es bisiesto o no lo es.
Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100,
o bien si es divisible entre 400. Puedes hacer la comprobación en esta lista de años bisiestos.

Ejemplo
Entrada: 2008

Salida: Es un año bisiesto
"""
year = 2022
division4 = (year % 4 == 0) or (year % 100 != 0)
division400 = year % 400 == 0

if division4 or division400:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
