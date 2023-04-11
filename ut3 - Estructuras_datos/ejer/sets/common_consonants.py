# *******************
# CONSONANTES COMUNES
# *******************


def run(text1: str, text2: str) -> str:
    VOWELS = "aeiou"

    text1 = text1.replace(" ", "")
    text2 = text2.replace(" ", "")
    set1 = {char for char in text1 if char not in VOWELS}
    set2 = {char for char in text2 if char not in VOWELS}
    result_set = set1 & set2
    cconst = "".join(sorted(result_set))
    return cconst


if __name__ == "__main__":
    run("Flat is better than nested", "Readability counts")
