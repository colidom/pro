import re

# 1. Escriba un programa en Python que encuentre todas las palabras que comiencen por vocal en un texto dado.
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
reguar_expression = r"\b[aeiou]\w*\b"


def vowel_words(text):
    # Pasamos 3º parámetro para incluir mayúsculas
    return re.findall(reguar_expression, text, re.I)


words = vowel_words(zen)
print(f"Count vowels: {len(words)}")
print(f"Vowels finded: {words} \n")
