import re

"""
    1. Escriba un programa en Python que encuentre todas las palabras que comiencen por vocal en un texto dado.
    2. Escriba un programa en Python que encuentre todas las URLs en un texto dado.
    3. Escriba un programa en Python que indique si un determinado número es o no un flotante válido en Python.
    4. Escriba un programa en Python que determine si un email dado tiene el formato correcto.
    5. Escriba un programa en Python que obtenga el resultado de una operación entre números enteros positivos. Las operación puede ser suma, resta, multiplicación o división, y puede haber espacios (o no) entre los operandos y el operador.

"""
regex = r"\b[aeiou]\w*\b"
zen = """
Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
Plano es mejor que anidado.
Espaciado es mejor que denso.
La legibilidad es importante.
Los casos especiales no son lo suficientemente especiales como para romper las reglas.
Sin embargo la practicidad le gana a la pureza.
Los errores nunca deberían pasar silenciosamente.
A menos que se silencien explícitamente.
Frente a la ambigüedad, evitar la tentación de adivinar.
Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
A pesar de que eso no sea obvio al principio a menos que seas Holandés.
Ahora es mejor que nunca.
A pesar de que nunca es muchas veces mejor que *ahora* mismo.
Si la implementación es difícil de explicar, es una mala idea.
Si la implementación es fácil de explicar, puede que sea una buena idea.
Los espacios de nombres son una gran idea, ¡tengamos más de esos!
"""


def vowel_count(text):
    return re.findall(regex, text)


words = vowel_count(zen)
print(words)
