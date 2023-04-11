# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
    with open(input_path, "r") as file_input:
        num_lines = num_words = num_bytes = 0

        for line in file_input:
            num_lines += 1
            num_words += len(line.strip().split())
            num_bytes += len(line.encode("utf8"))
    return num_lines, num_words, num_bytes


if __name__ == "__main__":
    run("data/wc/lorem.txt")
