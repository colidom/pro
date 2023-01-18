# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    all_same = True
    index = []
    for value in items.values():
        index.append(value)
        if value == index[0]:
            all_same = True
        else:
            all_same = False
            break
    return all_same


if __name__ == "__main__":
    run({"a": 1, "b": 1, "c": 1, "d": 1})
