# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = "data/sum_matrix/result.dat"
    with open(matrix1_path, "r") as file_input1:
        matrix1 = [number.strip() for number in file_input1]

    with open(matrix2_path, "r") as file_input2:
        matrix2 = [number.strip() for number in file_input2]

    with open(result_path, "w") as file_output:
        for value1, value2 in zip(matrix1, matrix2):
            int_val1 = [int(str_val1) for str_val1 in value1.split(" ")]
            int_val2 = [int(str_val2) for str_val2 in value1.split(" ")]
            suma = sum(int_val1 + int_val2)
            file_output.write(f"{suma}\n")

    return filecmp.cmp(result_path, "data/sum_matrix/.expected", shallow=False)


if __name__ == "__main__":
    run("data/sum_matrix/matrix1.dat", "data/sum_matrix/matrix2.dat")
