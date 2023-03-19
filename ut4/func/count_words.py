# *******************************
# CONTANDO PALABRAS (EN RECURSIVO)
# *******************************


def count_words(text: list[str]) -> int:
    if len(text) == 0:
        return 0

    # Se va extrayendo cada palabra de la lista de entrada(pila) empezando por indice 0("Hola")
    dato = len(text[0]) + count_words(text[1:])
    return dato


print(count_words(["Hola", "Mundo", "vamos"]))
