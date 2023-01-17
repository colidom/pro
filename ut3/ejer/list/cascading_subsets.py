# ***********************
# SUBCONJUNTOS EN CASCADA
# ***********************


def run(values: list, size: int) -> list:
    cascading = []
    for i in range(len(values) - size + 1):
        cascading.append(values[i : i + size])

    return cascading


if __name__ == "__main__":
    run([1, 2, 3, 4], 3)
