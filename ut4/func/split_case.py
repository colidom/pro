# *********************************
# SEPARANDO MAY�SCULAS Y MIN�SCULAS
# *********************************


def split_case(words: list[str]) -> list[str]:
    words_lower = []
    words_upper = []

    for word in words:
        if word.islower():
            words_lower.append(word)
        elif word.isupper():
            words_upper.append(word)

    return words_lower, words_upper
