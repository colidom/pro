# Dada una lista de strings, obtenga otra lista que contenga todos los caracteres de cada
# uno de los strings de la lista de entrada.


def run(texts: list) -> list:

    chars = []

    for text in texts:
        for letter in text:
            chars.append(letter)
            # print(chars)
    return chars
