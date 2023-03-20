# **************************
# BARICENTRO DE UN TRIÁNGULO
# **************************


def run(A: list, B: list, C: list) -> tuple:
    x = (A[0] + B[0] + C[0]) / 3
    y = (A[1] + B[1] + C[1]) / 3
    return (round(x, 4), round(y, 4))


if __name__ == "__main__":
    run([4, 6], [12, 4], [10, 10])
