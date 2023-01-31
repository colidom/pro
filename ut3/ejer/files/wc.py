# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
    with open(input_path, "r") as f:
        num_lines = 0
        for _ in f:
            num_lines += 1

    # len(s.encode('utf8'))
    num_words = num_bytes = "output"

    return num_lines, num_words, num_bytes


if __name__ == "__main__":
    run("data/wc/lorem.txt")
