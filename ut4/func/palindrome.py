# **********
# PALÍNDROMO
# **********


def is_palindrome(text: str) -> bool:
    phrase = text.lower().replace(" ", "")

    if phrase == phrase[::-1]:
        return True
    else:
        return False
