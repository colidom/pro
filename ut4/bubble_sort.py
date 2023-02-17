# **********************
# ORDENANDO CON BURBUJAS
# **********************


def bubble(items):
    values = items.copy()
    length_val = len(values)

    for i in range(0, length_val - 1):
        for j in range(length_val - 1):
            if values[j] > values[j + 1]:
                matraca = values[j]
                values[j] = values[j + 1]
                values[j + 1] = matraca
    return values


items = [2, 1, 2]
bubble(items)
