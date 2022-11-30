# ***************************
# BUSCANDO LA MAYOR DISTANCIA
# ***************************


def run(values: list, target: int) -> int:
    max_diff = []
    operation = []
    for value in values:
        operation.append(value - target)
        print(operation)
    return max_diff


if __name__ == "__main__":
    run([7, 3, 1, 12, 21, 4], 8)
