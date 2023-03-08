# ********
# PANGRAMA
# ********


def is_pangram(text: str) -> bool:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    phrase = text.lower().replace(" ", "")
    for letter in ALPHABET:
        if letter not in phrase:
            return False
    return True
