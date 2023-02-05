# ********************
# LA PALABRA MÁS LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    UNNEEDED_CHARS = ",.;:()"
    longest_word = ""
    with open(input_path, "r") as file_input:
        for line in file_input:
            splitted_text = line.split()
            for word in splitted_text:
                stripped_word = word.strip(UNNEEDED_CHARS)
                if len(stripped_word) >= len(longest_word):
                    longest_word = stripped_word

    return longest_word


if __name__ == "__main__":
    run("data/longest_word/python.txt")
