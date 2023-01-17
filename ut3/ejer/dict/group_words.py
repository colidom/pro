# ******************
# AGRUPANDO PALABRAS
# ******************


def run(words: list) -> dict:
    group_words = {}
    word_start = []
    repeated_letter = []
    no_repeated_letter = []

    for word in words:
        if word[0] not in word_start:
            word_start += word[0]
            repeated_letter.append(word)
            group_words[word[0]]: repeated_letter
        else:
            no_repeated_letter.append(word)

    return group_words


if __name__ == "__main__":
    run(
        [
            "mesa",
            "móvil",
            "barco",
            "coche",
            "avión",
            "bandeja",
            "casa",
            "monitor",
            "carretera",
            "arco",
        ]
    )
