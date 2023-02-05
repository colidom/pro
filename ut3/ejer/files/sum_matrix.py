# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = "data/sum_matrix/result.dat"
    matrix1 = []
    matrix2 = []
    result = []
    line_result = []

    with open(matrix1_path, "r") as file_input1:
        for line in file_input1:
            matrix_line = line.strip().split()
            matrix1.append(matrix_line)

    with open(matrix2_path, "r") as file_input2:
        for line in file_input2:
            matrix_line = line.strip().split()
            matrix2.append(matrix_line)

    with open(result_path, "w") as f:
        index = 0
        for i, values in enumerate(matrix1):
            for _ in values:
                operation = int(matrix1[i][index]) + int(matrix2[i][index])
                result.append(str(operation))
                index += 1
            line_result.append(result)
            index = 0
            result = []
        for values in line_result:
            line_values = " ".join(values)
            f.write(f"{line_values}\n")

    return filecmp.cmp(result_path, "data/sum_matrix/.expected", shallow=False)


if __name__ == "__main__":
    run("data/sum_matrix/matrix1.dat", "data/sum_matrix/matrix2.dat")
