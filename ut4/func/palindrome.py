# **********
# PALÍNDROMO
# **********


def is_palindrome(text: str) -> bool:
    word = ""
    for letter in text.replace(" ", ""):
        word += letter
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False
