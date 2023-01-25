# *******************
# CONSONANTES COMUNES
# *******************


def run(text1: str, text2: str) -> str:
    # Solución 1
    VOWELS = "aeiou"
    cconst = {sentence for sentence in text1}
    print(cconst)
    cconst = "output"

    return cconst


if __name__ == "__main__":
    run("Flat is better than nested", "Readability counts")
