# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = "data/sum_matrix/result.dat"
    int_matrix1 = []
    int_matrix2 = []
    with open(matrix1_path, "r") as file_input1:
        for line in file_input1:
            for value in line.strip().split():
                int_value = int(value)
                int_matrix1.append(int(int_value))

    with open(matrix2_path, "r") as file_input2:
        for line in file_input2:
            for value in line.strip().split():
                int_value = int(value)
                int_matrix2.append(int(int_value))

    with open(result_path, "w") as file_output:
        for value1, value2 in zip(int_matrix1, int_matrix2):
            result = value1 + value2
            file_output.write(f"{result}\n")

    return filecmp.cmp(result_path, "data/sum_matrix/.expected", shallow=False)


if __name__ == "__main__":
    run("./data/sum_matrix/matrix1.dat", "./data/sum_matrix/matrix2.dat")
