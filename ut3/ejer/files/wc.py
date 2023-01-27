# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
    with open(input_path, "r") as f:
        for line in f:
            num_lines = []

            print(line)
            break

    num_lines = num_words = num_bytes = "output"

    return num_lines, num_words, num_bytes


if __name__ == "__main__":
    run("data/wc/lorem.txt")
