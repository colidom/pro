# *******************************
# CONTANDO PALABRAS (EN RECURSIVO)
# *******************************


def count_words(text: str) -> int:

    if len(text) == 0:
        return 0

    return len(text[0]) + count_words(text[1:])


print(count_words(["Hola", "Mundo", "vamos"]))
