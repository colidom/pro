# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
    with open(input_path, "r") as file_input:
        num_lines = 0
        num_words = 0

        for line in file_input:
            num_lines += 1
            lines = line.strip().split()
            for line in lines:
                num_words += 1

    # len(s.encode('utf8'))
    num_bytes = "output"

    return num_lines, num_words, num_bytes


if __name__ == "__main__":
    run("data/wc/lorem.txt")
