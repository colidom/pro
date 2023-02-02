# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    UNNEEDED_CHARS = ".:;()'¡!-"
    with open(data_path, "r") as file_input:
        for line in file_input:
            stripped_line = line.strip(UNNEEDED_CHARS).split(",")
            print(stripped_line)
    matches = "output"

    return matches


if __name__ == "__main__":
    run("data/find_words/bzrp.txt", "persona")
