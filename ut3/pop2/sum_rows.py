# *************
# SUMANDO FILAS
# *************
from pathlib import Path


def run(data_path: Path) -> tuple:
    rsum = []
    with open(data_path, "r") as f:
        for row in f:
            values = [int(val) for val in row.strip().split()]
            rsum.append(sum(values))
    rsum = tuple(rsum)
    return rsum


if __name__ == "__main__":
    run("data/sum_rows/data1.txt")
