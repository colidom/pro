# *************
# SUMANDO FILAS
# *************
from pathlib import Path


def run(data_path: str) -> tuple:
    rsum = []
    with open(data_path, "r") as f:
        for row in f:
            numbers = [int(n) for n in row.strip().split()]
            rsum.append(sum(numbers))
    return tuple(rsum)


if __name__ == "__main__":
    run("data/sum_rows/data1.txt")
