import re

"""5. Escriba un programa en Python que obtenga el resultado de una operación entre números enteros positivos.
Las operación puede ser suma, resta, multiplicación o división, y puede haber espacios (o no) entre los
operandos y el operador."""

regex = r"\s*(\d+(?:\.[_\d]+)?\s*([+\-*/])\s*(\d+(?:\.[_\d+])?)\s*$"

