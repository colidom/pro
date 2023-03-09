# *****************
# ALFABETO CIRCULAR
# *****************


def cycle_text(text: str, max_letters: int) -> int:
    for i in range(max_letters):
        current_pos = i % len(text)
        yield text[current_pos]


def run(max_letters: int) -> str:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    return "".join(cycle_text(ALPHABET, max_letters))


if __name__ == "__main__":
    run(0)
